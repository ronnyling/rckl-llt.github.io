import csv
import xlrd
import os
import re

from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from pathlib import Path
from functools import reduce
from sys import platform


class CsvLibrary(object):
    promotion_data_directory = "\\setup\\testdata\\"

    @keyword("user retrieve test data from \"${filename}\" located at \"${directory}\" folder")
    def retrieve_test_data(self, filename, foldername):
        filepath = self.get_script_path() + CsvLibrary.promotion_data_directory + foldername + "\\" + filename
        if platform == "linux" or platform == "linux2":  # check OS type
            filepath = filepath.replace('\\', '/')
        data = self.read_data_from_file(filepath)
        print("File location: " + filepath)
        BuiltIn().set_test_variable("${file_data}", data)
        return data

    # @keyword('read data from file ${filepath}')
    def read_data_from_file(self, filepath):
        if '.xlsx' in filepath:
            data2 = self.read_excel(filepath)
            return data2
        else:
            data = self.read_csv(filepath)
            return data

    def read_csv(self, filepath):
        ## Read csv and assign to structured dictionary
        data = {}
        with open(filepath) as myfile:
            firstline = True
            for line in myfile:
                if firstline:
                    mykeys = "".join(line.rstrip()).split(
                        ',')  # rstrip() will remove trailing \n but ignore whitespaces
                    firstline = False  # first row of csv file will be used as header (key for dictionary values)
                else:
                    newvalues = []
                    values = re.split(''',(?=(?:[^'"]|'[^']*'|"[^"]*")*$)''',
                                      line.rstrip())  # each time it finds a comma, the lookahead scans the entire remaining string, making sure there's an even number of single-quotes and an even number of double-quotes. (Single-quotes inside double-quoted fields, or vice-versa, are ignored.) If the lookahead succeeds, the comma is a delimiter.
                    for value in values:
                        value = value.replace('""', '"')
                        if str.isdigit(value) is True:
                            value = int(value)
                            newvalues.append(value)
                        else:
                            newvalues.append(value.strip('""'))

                    data.update({values[0]: {mykeys[n]: newvalues[n] for n in
                                             range(0, len(mykeys))}})  # the first column will be used as key
                    # return read data as a dictionary of dictionaries
        return data

    def read_csv_data(self, filepath):
        ## This will return the type as an Ordered Dictionary.   # optional use
        data = []
        with open(filepath, "rt", encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                data.append(row)
        # self.builtin.set_test_variable("${return_data}", data)    # assign read data to global using PageObject
        return data

    def read_excel(self, filepath):
        ## this function is for excel file usage
        workbook = xlrd.open_workbook(os.path.normpath(filepath), on_demand=True)       # normpath is required to resolve double back-slash (\\) character
        worksheet = workbook.sheet_by_index(0)                                          # used in path and turn to OS compatible forward slash.
        first_row = []  # the row storing the name of the column
        for col in range(worksheet.ncols):
            first_row.append(worksheet.cell_value(0, col))
        ## transform the workbook to a list of dictionaries
        data = []
        for row in range(1, worksheet.nrows):
            elm = {}
            for col in range(worksheet.ncols):
                elm[first_row[col]] = worksheet.cell_value(row, col)
            data.append(elm)
            ## return as list of dictionaries
        print(data)
        return data

    def get_script_path(self):      # returns path for current class file's directory's parent (during run-time)
        source_file = Path(__file__).resolve()
        source_dir = source_file.parent
        root_dir = source_dir.parent
        return str(root_dir.parent)

    # common helper methods

    def dequote(self, string):
        if (string[0] == string[-1]) and string.startswith(("'", '"')):
            return string[1:-1]
        return string

    def remove_prefix(self, text, prefix):
        return text[text.startswith(prefix) and len(prefix):]

    def deep_get(self, dictionary, keys, default=None):
        return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split("."), dictionary)
