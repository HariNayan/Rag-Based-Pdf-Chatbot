from pdf_loader import PDFloader
clean_lines = PDFloader()
def create_chunker():
    chunks = []
    chunk = ''
    count = 0
    for line in clean_lines:
        chunk = chunk + ' ' + line
        count = count + 1
        if count == 5:
            chunks.append(chunk)
            chunk = ""
            count = 0
    if chunk:
        chunks.append(chunk)
    return chunks