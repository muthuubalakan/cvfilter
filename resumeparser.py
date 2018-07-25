#!/usr/bin/env python3
import sys
import os
import argparse
from resumeparser import content_extractor

pdf = content_extractor.PDFContent()

FAILURE = 1
SUCCESS = 0

class Textfinder:
    """
    Textfinder

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
            sys.stderr.write("Text file required\n")
            sys.exit(FAILURE)
        data = pdf.get_list(filename)
        # Words in the file
        result = []
        with open(word_file) as word_file:
            for word in word_file:
                if word in data:
                    result.append(word.upper())
                else:
                    print("The word {} is not found in {}".format(word, filename))
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
    if not (args.textfile):
        sys.stderr.write("specify a resume directory and textfile: Required. Stopping..\n")
        sys.exit(FAILURE)
    return args


if __name__ == '__main__':
    args = get_files()
    path = args.path
    word_file = args.textfile
    finder = Textfinder()
    sys.stdout.write("Textfinder - Version 0.1\n")
    finder.init_search(word_file, path)
