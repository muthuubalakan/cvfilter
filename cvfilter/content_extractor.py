import PyPDF2
import logging
import logging.config
import sys
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

logging.config.fileConfig("config/logging.conf")
logger = logging.getLogger(__name__)

EXIT_SUCCESS = 0
EXIT_FAILURE = 1


class PDFContent:
    def pdf_content(self, filename, mode='rb'):
        data = " "
        if hasattr(PyPDF2, 'PdfFileReader'):
            load_pdf = PyPDF2.PdfFileReader(filename, mode)
            # get pages
            no_of_pages = load_pdf.getNumPages()
            if no_of_pages > 4:
                logging.warn("Allowed only small size of files")
                sys.exit(EXIT_FAILURE)
            for i in range(0, no_of_pages):
                data += load_pdf.getPage(i).extractText() + " "
            data = " ".join(data.replace(u"\xa0", " ").strip().split())
            data = data + "\n"
            return data
        else:
            logging.info("Import PdfFileReader")
            return False

    def get_list(self, filename):
        data = self.pdf_content(filename)
        logging.info("Getting list")
        to_list = word_tokenize(data)
        stop_words = stopwords.words('english')
        filtered = [w for w in to_list if not (w in stop_words)
                    and not (w in string.punctuation)]
        return filtered
