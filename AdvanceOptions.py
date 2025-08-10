import fitz

def process_pdf(pdf_path:str)->None:
    
    doc = fitz.open(pdf_path)
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        images = page.get_images()
        
        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            
            with open(f"image_{page_num}_{img_index}.png", "wb") as img_file:
                img_file.write(image_bytes)
                
    page = doc[0]
    page.draw_rect([100, 100, 200, 200], color=(1, 0, 0))
            
    doc.save("pdfs/annotated.pdf")
    
process_pdf("pdfs/createdPdf.pdf")