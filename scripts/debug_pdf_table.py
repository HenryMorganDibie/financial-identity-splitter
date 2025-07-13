import pdfplumber

pdf_path = "data/5703007018 - Henry Dibie’s Bank statement.pdf"

with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages):
        print(f"\n📄 Page {i+1}")
        table = page.extract_table()
        if table:
            for row in table[:5]:  # print only the first 5 rows of the page
                print(row)
