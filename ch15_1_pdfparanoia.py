'''
Create encrypted copies of all pdfs in a folder. Include all files in subfolders.
If PDfs exist in target location, they will be over-written.
'''

import PyPDF2, os.path

# File paths of PDFs to be copied from and to. End file path with '/'
folder_location = 'C:/Users/.../Automate the Boring Stuff 2e/PDF stack/' # Use your local file path
target_location = 'C:/Users/.../Automate the Boring Stuff 2e/Encrypted Stack/' # Use your local file path

for path, subfolders, files in os.walk(folder_location):
    for i in files:
        # print("File inside %r" % (path) + i)
        # Use 'path', not 'subfolders', for PdfFileReader file location
        pdf_reader = PyPDF2.PdfFileReader(open(path + '/' + i, 'rb'))
        # Start up PDF Writer Object
        pdf_writer = PyPDF2.PdfFileWriter()
        # Copy all reader pages to writer object using .addPage
        for page_num in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page_num))
        # Set password
        pdf_writer.encrypt('dayoldcroissant')
        # Create result PDF shell
        print(target_location + i + '_encrypted', 'wb')
        result_pdf = open(target_location + i + '_encrypted', 'wb')
        # Write to it
        pdf_writer.write(result_pdf)
        # Close it
        result_pdf.close()
