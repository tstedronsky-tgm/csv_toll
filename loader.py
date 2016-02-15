from PySide.QtCore import *
from PySide.QtGui import *
import view,sys
import csv

class    loader(QMainWindow):
    """ CSV-Module Application
        Autor: Thomas Stedronsky
        :param parent:
        """
    def __init__(self, parent=None):

        super().__init__(parent)
        self.form = view.Ui_MainWindow()
        self.form.setupUi(self)
        self.csv_content=''
        self.name=''
        self.csv_file=''

        self.form.pushButton.clicked.connect(self.clicked)

    def read_csv(self, file):
        self.name = file
        with open(file, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                for x in row:
                    self.csv_content +=x +','
                self.csv_content += '\n'

    def get_text_line(self):
        self.csv_file = self.form.lineEdit.text()

    def clicked(self):
        self.csv_content = ''
        self.get_text_line()
        self.read_csv(self.csv_file)
        self.form.label_2.setText(self.name)
        self.form.textEdit.setText(self.csv_content)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = loader()
    c.show()
    sys.exit(app.exec_())
