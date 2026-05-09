from PyPDF2 import PdfReader
from pathlib import Path

def PDFloader():
    Docs = input("Enter Pdfs Here: ")
    Docs_list = Docs.split(";")
    my_text = ""
    for Doc in Docs_list:
        Doc = Doc.strip()
        Docs_path = Path(Doc)
        if not Docs_path.is_file():
            print(f"Skipping {Doc} not found")
            continue
        try:
            print(f"Found Reading {Doc}")
            reader = PdfReader(Doc)
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