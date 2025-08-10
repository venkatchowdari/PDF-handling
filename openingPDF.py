import PyPDF2

pdf_file = "sample.pdf"

def read_pdf_info(file_path):
    reader = PyPDF2.PdfReader(file_path)
    
    info = {
        'number_of_page': len(reader.pages),
        'metadata': reader.metadata,
        'is_encrypted': reader.is_encrypted
    }
    
    text = ""
    for page in reader.pages:
        text += page.extract_text()
        if page == 1:
            break
        
    return info, text

json_i, text = read_pdf_info(pdf_file)

print(text)
print(json_i)
