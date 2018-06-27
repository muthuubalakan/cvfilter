#!/usr/bin/env python3
import sys
import os
import argparse
from content_extractor import PDFContent


class Textfinder(PDFContent):
    """Textfinder search word in the all the files.

    Searching all the files for requested word
    return the word and number of time repeated.
    Textfinder.search_word(filename, word_list) will return words and file.
    """
    def load_files(self, path=None):
        files_total = []
        if not path:
            path = os.getcwd()
        path = path
        dir_path = os.listdir(path)
        for files in dir_path:
            files_total.append(files)
        return files_total


    def search_word(self, filename, word_file):
        if not word_file.endswith('.txt'):
            sys.stderr.write("Text file required")
            sys.exit(1)
        data = PDFContent.get_list(filename)
        # Words in the file
        result = []
        for word in word_file:
            if word in data:
                result.append(word)
        if len(result) != 0:
            for key in result:
                print("The file : {} has the word: {}  repeated: {}".
                      format(filename, key))

    def init_search(self, word_list, path):
        filename = [filename for filename in self.load_files(path)]
        for filename in filename:
            if filename.endswith('.pdf'):
                self.search_word(filename, word_list)


def get_files():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', "--path", help="Resume directory", type=str)
    parser.add_argument('-t', "--textfile", help="Text file", type=str)
    parser.add_argument('-v', "--verbose", help="verbose", action='store_true')
    args = parser.parse_args()
    if not (args.resumefile and args.textfile):
        sys.stderr.write("Resume directory and textfile required. Stopping..\n")
        sys.exit(1)
    return args


if __name__ == '__main__':
    args = get_files()
    path = args.path
    word_file = args.textfile
    finder = Textfinder()
    sys.stdout("Textfinder - Version 0.1")
    finder.init_search(word_file, path)

