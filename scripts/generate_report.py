# 3D_Modeling_Project/scripts/generate_report.py

from fpdf import FPDF
import pandas as pd
import logging
import argparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levellevelname)s - %(message)s'))
logger = logging.getLogger()
file_handler = logging.FileHandler('generate_report.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Simulation Analysis Report', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

def create_pdf_report(data, output_path):
    """Create a PDF report from analysis data."""
    try:
        pdf = PDFReport()
        pdf.add_page()

        pdf.chapter_title("Summary of Analysis")
        body = (f"Mean Height: {data['mean_height']}
"
                f"Max Height: {data['max_height']}
"
                f"Min Height: {data['min_height']}
")
        pdf.chapter_body(body)

        pdf.output(output_path)
        logger.info(f"PDF report generated at {output_path}")
    except Exception as e:
        logger.error(f"Error generating PDF report: {e}")
        raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate PDF report from analysis results.")
    parser.add_argument('--input', type=str, required=True, help="Path to the analysis results CSV file.")
    parser.add_argument('--output', type=str, required=True, help="Path to save the PDF report.")

    args = parser.parse_args()

    try:
        df = pd.read_csv(args.input)
        data = df.to_dict(orient='records')[0]
        create_pdf_report(data, args.output)
    except Exception as e:
        logger.error(f"Failed to generate report: {e}")
