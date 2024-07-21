from PyPDF2 import PdfReader

reader = PdfReader("./pdf_word/my_pdf.pdf")
no_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()


print(no_of_pages)
print(page)
print(text)
