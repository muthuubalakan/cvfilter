#!/usr/bin/env python3
import sys
from collections import Counter
import os
from format_checker import FormatChecker


class Textfinder(FormatChecker):
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

    def scan_file(self, filename):
        FormatChecker.check_format(filename)
        container = []
        with open(filename) as f:
            for line in f:
                for word in line.split():
                    container.append(word)

        if len(container) != 0:
            counts = Counter(container)
            return counts

    def search_word(self, filename, word_list):
        counts_dict = self.scan_file(filename)
        # Words in the file
        result = []
        words = counts_dict.keys()
        for word in word_list:
            if word in words:
                result.append(word)
        if len(result) != 0:
            for key in result:
                print("The file : {} has the word: {}  repeated: {}".
                      format(filename, key, counts_dict[key]))

    def main(self):
        word_list = sys.argv[1]
        filename = [filename for filename in self.load_files()]
        for filename in filename:
            if filename.endswith('.txt'):
                filename = os.path.join(os.getcwd, filename)
                self.search_word(filename, word_list)


if __name__ == '__main__':
    A = Textfinder()
    A.main()
