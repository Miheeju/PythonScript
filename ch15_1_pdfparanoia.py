'''
Encrypt all pdfs in a folder
Next (to do): Include files in subfolder too
Next 2: Decrypt them
'''

import PyPDF2, os

folder_location = 'C:/Python/Automate the Boring Stuff 2e/PDF stack/' # replace with actual folder path
for folder_name, subfolders, filenames in os.walk(folder_location):
    for j in filenames:
        pdf_reader = PyPDF2.PdfFileReader(open(folder_location + j, 'rb'))
        # Start up PDF Writer Object
        pdf_writer = PyPDF2.PdfFileWriter()
        # Copy all reader pages to writer object using .addPage
        for page_num in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page_num))
        # Set pasword
        pdf_writer.encrypt('dayoldcroissant')
        # Create result PDF shell
        result_pdf = open(folder_location + j + '_encrypted', 'wb')
        # Write to it
        pdf_writer.write(result_pdf)
        # Close it
        result_pdf.close()

    print('THE END')
