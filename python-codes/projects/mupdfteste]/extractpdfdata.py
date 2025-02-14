import pymupdf

def getPage(doc, page_number):
    page = doc.load_page(page_number)
    
    return page

doc = pymupdf.open("2016_the-linux-command-line_a-complete-introduction.pdf")

print(f"{getPage(doc, 50).get_images()}")