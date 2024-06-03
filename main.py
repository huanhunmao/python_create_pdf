from fpdf import FPDF
import pandas as pd
import add_lines as al

pdf = FPDF(orientation='P', unit='mm', format='A4')
# 设置主文档
pdf.set_auto_page_break(auto=False, margin=0)

# print(type(pdf)) # <class 'fpdf.fpdf.FPDF'>
df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    # 添加主页面
    pdf.add_page()
    pdf.set_font(family='Times', style='I', size=12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)

    al.add_lines(pdf)

    # 设置主页面的页脚
    pdf.ln(265)
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

    # 生成空白页并设置页脚
    for i in range(row['Pages'] - 1):
        pdf.add_page()
        al.add_lines(pdf)
        pdf.ln(277)
        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align='R')
pdf.output('output.pdf')
