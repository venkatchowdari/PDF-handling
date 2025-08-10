import PyPDF2

def extract_pdf(input_pdf:str, output_pdf:str, pages:list)->None:
    reader = PyPDF2.PdfReader(input_pdf)
    writer = PyPDF2.PdfWriter()
    
    for page in pages:
        if 0 <= page < len(reader.pages):
            writer.add_page(reader.pages[page])
        
    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)
        

extract_pdf("pdfs/sample.pdf", "pdfs/extracted_pdf1.pdf", [0, 2])