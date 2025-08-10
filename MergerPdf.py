from PyPDF2 import PdfMerger

def merger_pdfs(pdf_list:list, output_path:str)->None:
    merger = PdfMerger()
    
    for pdf in pdf_list:
        merger.append(pdf)
        
    with open(output_path, "wb") as output_file:
        merger.write(output_path)
        
    
merger_pdfs(["pdfs/sample.pdf", "pdfs/modifiedPdf.pdf"], "pdfs/mergedPdfs.pdf")