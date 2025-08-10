import PyPDF2

#This file takes the pdfs and merge them into single file
def merge_pdfs(pdf_files:list, output_path:str)->None:
    merger = PyPDF2.PdfMerger()
    
    for pdf in pdf_files:
        merger.append(pdf)
        
    
    with open(output_path, 'wb') as f:
        merger.write(f)
        

merge_pdfs(["pdfs/beans.101.pdf", "pdfs/sample.pdf"], "pdfs/output_of_merge.pdf")