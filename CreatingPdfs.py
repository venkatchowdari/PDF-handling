from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


def create_pdf(output_path: str)-> None:
    c = canvas.Canvas(output_path, pagesize=letter)
    
    c.drawString(100, 750, "HelloWorld!")
    
    c.rect(100, 700, 100, 50)
    
    c.drawImage("image.jpg", 100, 500, width=200, height=200)
    
    c.save()
    
create_pdf("pdfs/createdPdf.pdf")