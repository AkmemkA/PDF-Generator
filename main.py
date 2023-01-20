from fpdf import FPDF
import pandas as pd

df = pd.read_csv('topics.csv')
pdf = FPDF(orientation="P", unit="mm", format="A4")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(12, 40, 100)
    page_header = row['Topic']
    number_of_pages = int(row['Pages'])
    pdf.cell(w=0, h=12, txt=page_header, align="L", ln=1)
    pdf.line(10, 20, 200, 20)
    for page in range(1, number_of_pages):
        pdf.add_page()
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(12, 40, 100)
        page_header = row['Topic']
        number_of_pages = int(row['Pages'])
        pdf.cell(w=0, h=12, txt=page_header, align="R", ln=1)
        pdf.line(180, 20, 200, 20)

pdf.output("new_pdf.pdf")
