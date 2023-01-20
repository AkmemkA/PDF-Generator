from fpdf import FPDF
import pandas as pd

df = pd.read_csv('topics.csv')
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    # Add page, header and line
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1)
    # Add footer
    pdf.ln(260)
    pdf.set_font(family="Times", size=10)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="R", ln=1)
    # Create lines on each page
    for y in range(20, 290, 10):
        pdf.line(10, y, 200, y)
    # Add empty pages with footers
    for page in range(1, int(row['Pages'])):
        pdf.add_page()
        pdf.ln(272)
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=row['Topic'], align="R", ln=1)
        # Create lines on each page
        for y in range(20, 290, 10):
            pdf.line(10, y, 200, y)

pdf.output("new_pdf.pdf")
