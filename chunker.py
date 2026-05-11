from uploaded_pdfs import PDFloader

def create_chunker(uploaded_pdfs):
    clean_lines = PDFloader(uploaded_pdfs)
    chunks = []
    chunk = ''
    count = 0
    for line in clean_lines:
        chunk = chunk + ' ' + line
        count = count + 1
        if count == 10:
            chunks.append(chunk)
            chunk = ""
            count = 0
    if chunk:
        chunks.append(chunk)
    return chunks