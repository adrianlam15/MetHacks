from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


def extract_text(pdf_path):
    resource_manager = PDFResourceManager()
    output_string = StringIO()
    laparams = LAParams()
    device = TextConverter(resource_manager, output_string, laparams=laparams)
    fp = open(pdf_path, "rb")
    interpreter = PDFPageInterpreter(resource_manager, device)
    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
    fp.close()
    device.close()
    text = output_string.getvalue()
    output_string.close()
    return text
