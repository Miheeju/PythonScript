# Concept: Take a PDF and save a copy of it with all pages rotated by 90 or 180 degrees
# I will use the "Washington Driver Guide 2023.pdf"

# Step 1: Import library
import PyPDF2 as pypdf2

folder_location = 'C:/.../Python/Automate the Boring Stuff 2e/' # Your file path here
target_location = 'C:/.../Automate the Boring Stuff 2e/' # Your file path here
# Step 2: Create pdf reader object to open or read the existing PDF file
orig_file = open(folder_location + 'Washington Driver Guide 2023.pdf', 'rb')
pdf_reader = pypdf2.PdfFileReader(orig_file)

# Step 3: Create page object - for single page
# page_obj = pdf_reader.getPage(0)

# Step 4: Rotate page - for single page
# page_obj.rotateCounterClockwise(90)

# Step 5: Create PDF writer object
pdf_writer = pypdf2.PdfFileWriter()

# Step 6: Add rotated page to writer object
# Copy all reader pages to writer object using .addPage
# Combine with creating page object and rotating for all pages in the PDF
for page_num in range(pdf_reader.numPages):
    pdf_writer.addPage(pdf_reader.getPage(page_num).rotateCounterClockwise(180))

# Step 7: Create new PDF shell
result_file = open(target_location + 'rotated_file.pdf', 'wb')

# Step 8: Write rotated page to PDF shell using PDF writer object
pdf_writer.write(result_file)

# Step 9: Close PDF that was being read and copied and new PDF being written
result_file.close()
orig_file.close()
