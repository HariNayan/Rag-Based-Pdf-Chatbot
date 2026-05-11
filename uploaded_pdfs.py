from PyPDF2 import PdfReader

def PDFloader(uploaded_pdfs):
    my_text = ""
    for uploaded_pdf in uploaded_pdfs:
        try:
            print(f"Found Reading {uploaded_pdf}")
            reader = PdfReader(uploaded_pdf)
            for page in reader.pages:
                page_text = page.extract_text()
                if not page_text:
                    continue
                my_text = my_text + page_text
        except Exception:
            print("Invalid Pdf, Skipping")
            continue
    my_text = my_text.splitlines()
    clean_lines = []
    for line in my_text:
        if line.strip():
            clean_lines.append(line)

    return clean_lines