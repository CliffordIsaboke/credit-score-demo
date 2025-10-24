from fastapi import APIRouter, UploadFile, File, Form, HTTPException, Request
from services.pdf_processor import PDFProcessor
from services.analysis_service import analysis_service
from services.ml_service import ml_service
from database.models import AnalysisResponse
from utils.file_handling import save_results_to_db, get_analysis_count
import tempfile
import os

router = APIRouter(prefix="/analysis", tags=["analysis"])

@router.post("/", response_model=AnalysisResponse)
async def analyze_pdf(
    request: Request,
    file: UploadFile = File(...),
    loan_amount: float = Form(...),
    password: str = Form(None)
):
    """Analyze PDF for loan scoring"""
    temp_path = None
    try:
        # Create temp file
        async with aiofiles.tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            content = await file.read()
            await temp_file.write(content)
            temp_path = temp_file.name
        
        # Process PDF
        df, client_name, client_phone, monthly_inflow, monthly_outflow, parse_status = await process_pdf_async(temp_path, password)
        
        # Extract client info
        client_info = PDFProcessor.extract_client_info(df, file.filename, client_name, client_phone)
        
        # Run analyses
        loan_data = analysis_service.detect_mobile_loans(df)
        betting_data = analysis_service.detect_betting_transactions(df)
        
        # Extract features and predict
        features = analysis_service.extract_features(df, monthly_inflow, monthly_outflow)
        score = ml_service.predict(features)
        score_percent = round(score * 100, 1)
        eligible = score < 0.7
        
        # Prepare results
        results = await prepare_analysis_results(
            df, client_info, loan_data, betting_data, 
            features, financial_metrics, score_percent, eligible, loan_amount
        )
        
        # Save to database
        analysis_count = await get_analysis_count()
        result_id = await save_results_to_db(results, client_info, loan_amount, score_percent, eligible)
        
        return AnalysisResponse(
            success=True,
            result_id=result_id,
            results=results,
            client_info=client_info,
            score=score_percent,
            eligible=eligible,
            analysis_count=analysis_count
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")
    finally:
        if temp_path and os.path.exists(temp_path):
            os.unlink(temp_path)