import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
import pandas as pd

# === Import your logic functions ===
from credit_utils import parse_mpesa_pdf, extract_features, score_credit


# === Dashboard logic ===
def launch_dashboard():
    def update_result(result, eligible):
        result_text.set(result)
        result_label.config(fg="green" if eligible else "red")

    def process_pdf(file_path):
        try:
            df = parse_mpesa_pdf(file_path)
            if df.empty:
                root.after(0, lambda: messagebox.showwarning("Warning", "No valid transactions found in PDF."))
                return

            features = extract_features(df)
            score, eligible = score_credit(features)

            result = f"Loan Score: {score*100:.1f}%\nEligible: {'✅ Yes' if eligible else '❌ No'}"
            root.after(0, lambda: update_result(result, eligible))

        except Exception as e:
            root.after(0, lambda: messagebox.showerror("Error", f"Failed to process PDF:\n{e}"))
        finally:
            root.after(0, lambda: (progress_bar.stop(), progress_bar.pack_forget()))

    def upload_pdf_and_score():
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if not file_path:
            return
        progress_bar.pack(pady=10, fill='x', padx=40)
        progress_bar.start(10)
        threading.Thread(target=process_pdf, args=(file_path,), daemon=True).start()

    # === GUI Setup ===
    root = tk.Tk()
    root.title("Demulla: M-Pesa AI Loan Scoring")
    root.geometry("420x320")

    tk.Label(root, text="Upload Your M-Pesa PDF Statement", font=("Helvetica", 14)).pack(pady=10)
    tk.Button(root, text="Upload PDF", command=upload_pdf_and_score, font=("Arial", 12)).pack(pady=5)

    progress_bar = ttk.Progressbar(root, mode='indeterminate')

    global result_text, result_label
    result_text = tk.StringVar()
    result_label = tk.Label(root, textvariable=result_text, font=("Arial", 14))
    result_label.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    launch_dashboard()
