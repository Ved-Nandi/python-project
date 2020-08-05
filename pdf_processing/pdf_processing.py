import PyPDF2

with open("processingpdf\dummy.pdf", 'rb') as filee:
    reader = PyPDF2.PdfFileReader(filee)
    #print(reader.getPage(0))
    #print(reader.getPage(0).rotateCounterClockwise(90))
    page = reader.getPage(0).rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open(r"processedpdf\rotetedpdf.pdf",'wb') as new_file:
        writer.write(new_file)

