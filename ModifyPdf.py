from PyPDF2 import PdfReader, PdfWriter

def modify_pdf(input_path: str, output_path:str)->None:
    reader = PdfReader(input_path)
    writer = PdfWriter()
    
    for page in reader.pages:
        page.rotate(90)
        writer.add_page(page)
        
    with open(output_path, "wb") as output_file:
        writer.write(output_file)
        
modify_pdf("pdfs/sample.pdf", "pdfs/modifiedPdf.pdf")