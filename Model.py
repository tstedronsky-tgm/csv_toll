import csv

class Model(object):

    def __init__(self):
        self.csv_content=''
        self.name=''
        self.csv_file=''
        self.delimiter=''

    def read_csv(self, file):
        if file is '':
            raise TypeError('')
        self.name = file
        with open(file, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                for x in row:
                    self.csv_content +=x +self.delimiter
                self.csv_content += '\n'

    def setDelimiter(self, delimiter):
        if delimiter is '':
            raise TypeError
        self.delimiter =delimiter

    def getDelimiter(self):
        return self.delimiter