import pdfplumber
import logging


class PDFTextExtractor:
    def __init__(self):
        logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    def extract_text_from_pdf(self, pdf_path: str) -> str:
        """
        Extracts text from a PDF file.

        Args:
            pdf_path (str): The path to the PDF file.

        Returns:
            str: The extracted text from the entire PDF. Returns an empty string if extraction fails.
        """
        text = ""
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
            logging.info(f"Text extracted from PDF at {pdf_path}")
        except Exception as e:
            logging.error(f"Error extracting text from PDF at {pdf_path}: {e}")
            return ""
        return text
