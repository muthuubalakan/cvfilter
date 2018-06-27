"""FormatChecker just check the file format.

Identify the file
Arguments:
    filename
    fm -- predefined format.
"""

class FormatChecker:
    def __init__(self, filename, fm=None):
        self.filename = filename
        self._check = fm

    def check_format(self):
        if self.filename.endswith('.txt'):
            print("Text file")
            return True
        elif self.filename.endswith('.pdf'):
            print("Pdf file")
        elif self.filename.endswith('.docx'):
            print("Word file")
            return True
        else:
            print("File not in required format")
            return False
