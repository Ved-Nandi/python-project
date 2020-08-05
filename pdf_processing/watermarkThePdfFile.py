import PyPDF2

template = PyPDF2.PdfFileReader(open('processedpdf\mergepdf.pdf','rb'))
watermark = PyPDF2.PdfFileReader(open("processingpdf\water.pdf",'rb'))
outputt = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    outputt.addPage(page)

    with open(r'processedpdf\newWatermarkpdf.pdf','wb') as file:
        outputt.write(file)