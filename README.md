# PDF Handling Project

A collection of Python scripts for various PDF operations using PyPDF2 and PyMuPDF (fitz).

## Features

- PDF Reading and Information Extraction ([openingPDF.py](openingPDF.py))
- PDF Merging ([mergePDF.py](mergePDF.py) and [MergerPdf.py](MergerPdf.py))
- PDF Modification - Page Rotation ([ModifyPdf.py](ModifyPdf.py))
- PDF Page Extraction ([ExtractionOfPDF.py](ExtractionOfPDF.py))
- PDF Creation with Text and Images ([CreatingPdfs.py](CreatingPdfs.py))
- Advanced PDF Operations - Image Extraction and Annotations ([AdvanceOptions.py](AdvanceOptions.py))

## Requirements

```
PyPDF2
PyMuPDF (fitz)
reportlab
```

## Usage

### Reading PDF Information
```python
python openingPDF.py
```
Reads and displays PDF metadata and text content.

### Merging PDFs
```python
python mergePDF.py
# or
python MergerPdf.py
```
Combines multiple PDF files into a single document.

### Modifying PDFs
```python
python ModifyPdf.py
```
Rotates PDF pages by 90 degrees.

### Extracting Pages
```python
python ExtractionOfPDF.py
```
Extracts specific pages from a PDF file.

### Creating PDFs
```python
python CreatingPdfs.py
```
Creates a new PDF with text, shapes, and images.

### Advanced Operations
```python
python AdvanceOptions.py
```
Extracts images from PDFs and adds annotations.

## File Structure

```
├── AdvanceOptions.py
├── CreatingPdfs.py
├── ExtractionOfPDF.py
├── mergePDF.py
├── MergerPdf.py
├── ModifyPdf.py
├── openingPDF.py
└── pdfs/
    ├── annotated.pdf
    ├── beans.101.pdf
    ├── createdPdf.pdf
    ├── extracted_pdf.pdf
    ├── extracted_pdf1.pdf
    ├── mergedPdfs.pdf
    ├── modifiedPdf.pdf
    ├── output_of_merge.pdf
    └── sample.pdf
```

## Output Files

- `annotated.pdf` - PDF with added annotations
- `createdPdf.pdf` - New PDF created with reportlab
- `extracted_pdf1.pdf` - PDF with specific extracted pages
- `mergedPdfs.pdf` - Result of PDF merging
- `modifiedPdf.pdf` - PDF with rotated pages
- `output_of_merge.pdf` - Another