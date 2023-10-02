'''
Goal: Combine many pdfs, excluding cover sheet page 1 in each file
1. Find all PDF files in directory
2. Sort files names alphabetically
3. Write each page minus cover page to output file
'''

import PyPDF2 as pypdf2, os.path

folder_location = 'C:/.../Automate the Boring Stuff 2e/PDF Stack/' # your file path here
target_location = 'C:/.../Automate the Boring Stuff 2e/' # your file path here

# Step 1: Select PDF Files

pdf_files = []

# os.listdir() returns a list of every file in the directory
for filename in os.listdir(folder_location):
    if filename.endswith('.pdf'):
        pdf_files.append(filename)
# Step 1.1: Sort list in ascending alphabetical order
pdf_files.sort(key = str.lower)
# Step 1.2: Create PdfFileWriter object to hold combined PDF pages
pdf_writer = pypdf2.PdfFileWriter()

# Step 2: Create pdf reader object to loop through and read existing PDF files
for filename in pdf_files:
    pdf_file_obj = open(folder_location+filename, 'rb')
    pdf_reader = pypdf2.PdfFileReader(pdf_file_obj)

    # Step 3: Create page object - loop through each page minus the first
    for page_num in range(1, pdf_reader.numPages):
        page_obj = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page_obj)

# Step 4: Save results
# Create new PDF shell
# Write copied pages to PDF shell using PDF writer object
# Close new PDF that was being written
pdf_output = open(target_location+'combined.pdf', 'wb')
pdf_writer.write(pdf_output)
pdf_output.close()
