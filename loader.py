from PySide.QtCore import *
from PySide.QtGui import *
import view,sys
from Model import Model
import csv

class loader(QMainWindow):
    """ CSV-Module Application
        Autor: Thomas Stedronsky
        :param parent:
        """
    def __init__(self, parent=None):

        super().__init__(parent)
        self.form = view.Ui_MainWindow()
        self.form.setupUi(self)
        self.model = Model()
        self.model.setDelimiter(',')

        self.form.pushButton.clicked.connect(self.clicked)

    def get_text_line(self):
        self.model.csv_file = self.form.lineEdit.text()

    def clicked(self):
        self.model.csv_content = ''
        self.get_text_line()
        self.model.read_csv(self.model.csv_file)
        self.form.label_2.setText(self.model.name)
        self.form.textEdit.setText(self.model.csv_content)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = loader()
    c.show()
    sys.exit(app.exec_())
