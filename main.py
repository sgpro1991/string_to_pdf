from fpdf import FPDF

arg_string = input("Укажите слово \n")
font_type = input("\nУкажите стиль ")
def CreatePdf(arg):
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font('Times',font_type, 24)
    pdf.cell(40,10, arg)
    pdf.output('example.pdf','F')

try:
    CreatePdf(arg_string)
except UnicodeEncodeError:
    print("Напишите на английском")
    arg_string = input("Укажите слово")
    CreatePdf(arg_string)
finally:
    print("Pdf created")
    
def main():
    print("lalalal")