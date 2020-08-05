import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_conbiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(r"processedpdf\mergepdf.pdf")


pdf_conbiner(inputs)