from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
for line in resume_text.split('\n'):
    pdf.multi_cell(0, 10, line)
pdf.output("resume.pdf")