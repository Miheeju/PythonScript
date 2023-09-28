# Goal: Overlay a 'confidential' watermark over first 3 pages of Driver Guide PDF document. Save as new PDF.
# Note: The book exercise is with an overlay over 1 page only. I wanted to try this with multiple pages.

# Step 1: Import Library
import PyPDF2 as pypdf2

folder_location = 'C:/.../Python/Automate the Boring Stuff 2e/' # Your file path here
target_location = 'C:/.../Python/Automate the Boring Stuff 2e/' # Your file path here

# Step 2: Create pdf reader object to read the existing PDF file 1
#         and Create page(s) object of pages to get overlay
orig_file = open(folder_location+'Washington Driver Guide 2023.pdf', 'rb')
pdf_reader = pypdf2.PdfFileReader(orig_file)

# Step 3: Create overlay object from PDF 2
pdf_watermark_reader = pypdf2.PdfFileReader(open(folder_location+'watermark.pdf', 'rb'))

# Step 5: Create PDF writer object
pdf_writer = pypdf2.PdfFileWriter()

# Step 4: Use mergePage() method on page objects. Select overlay page with getPage.
for i in range(0, 3):
    first_page = pdf_reader.getPage(i)
    first_page.mergePage(pdf_watermark_reader.getPage(0))
    # Step 6a: Add overlaid page to writer object
    pdf_writer.addPage(first_page)

# Step 6b: Add the rest of pages, non-overlaid, to writer object
for page_num in range(3, pdf_reader.numPages):
    page_obj = pdf_reader.getPage(page_num)
    pdf_writer.addPage(page_obj)


# Step 7: Create new PDF shell
result_file = open(target_location + 'overlaid_file.pdf', 'wb')

# Step 8: Write rotated page to PDF shell using PDF writer object
pdf_writer.write(result_file)

# Step 9: Close PDF that was being read and copied and new PDF being written
result_file.close()
orig_file.close()
