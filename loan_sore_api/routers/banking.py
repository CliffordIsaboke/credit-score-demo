from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from services.banking_service import banking_service
from services.pdf_processor import PDFProcessor
from database.models import BankAnalysisResponse
import aiofiles
import tempfile
import os

router = APIRouter(prefix="/banks", tags=["banks"])

@router.get("/")
async def get_all_banks():
    """Get all banks and financial institutions"""
    return banking_service.get_all_banks()

@router.post("/analyze-bank", response_model=BankAnalysisResponse)
async def analyze_specific_bank(
    file: UploadFile = File(...),
    bank_name: str = Form(...),
    password: str = Form(None)
):
    """Analyze transactions for a specific bank"""
    temp_path = None
    try:
        # Process PDF
        async with aiofiles.tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            content = await file.read()
            await temp_file.write(content)
            temp_path = temp_file.name
        
        df, _, _, _, _, _ = await process_pdf_async(temp_path, password)
        
        # Analyze specific bank
        bank_analysis = banking_service.analyze_specific_bank_transactions(df, bank_name)
        
        if bank_analysis is None:
            return BankAnalysisResponse(
                bank_name=bank_name,
                transactions_found=0,
                # ... other default values
            )
        
        return BankAnalysisResponse(**bank_analysis)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Bank analysis failed: {str(e)}")
    finally:
        if temp_path and os.path.exists(temp_path):
            os.unlink(temp_path)