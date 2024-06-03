from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')

# print(type(pdf)) # <class 'fpdf.fpdf.FPDF'>

pdf.add_page()

pdf.set_font(family='Times', style='B', size=12)
pdf.cell(w=0,h=12,txt='Hello, there', align='L', ln=1)
pdf.cell(w=0,h=12,txt='HHHAHHH, here', align='L', ln=1)

pdf.add_page()

pdf.output('output.pdf')