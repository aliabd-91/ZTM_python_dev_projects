# My Solution:
import PyPDF2

path_prefix = './Pdf_files/'
super_pdf = PyPDF2.PdfReader(f'{path_prefix}super.pdf')
stamp_pdf = PyPDF2.PdfReader(f'{path_prefix}wtr.pdf')
writer = PyPDF2.PdfWriter()

for page in super_pdf.pages:
    page.merge_page(stamp_pdf.pages[0])
    writer.add_page(page)

writer.write(f'{path_prefix}super_watermarked.pdf')
