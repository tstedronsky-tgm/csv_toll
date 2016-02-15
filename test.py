import unittest
from Model import Model

class CSVTest(unittest.TestCase):
    def setUp(self):
        self.model = Model()

    def testsetDelimiter(self):
        self.model.setDelimiter(',')
        self.assertEqual(self.model.delimiter, ',')

    def testsetName(self):
        self.model.read_csv('data.csv')
        self.assertEqual(self.model.name,'data.csv')

    def testsetName_None(self):
        self.assertRaises(TypeError, self.model.read_csv)

    def testsetContent(self):
        self.model.setDelimiter(',')
        self.model.read_csv('data.csv')
        self.assertEqual(self.model.csv_content, 'Year,Make,Model,Length,\n1997,Ford,E350,2.34,\n2000,Mercury,Cougar,2.38,\n')

    def testsetDelimiter_None(self):
        self.assertRaises(TypeError, self.model.setDelimiter)

if __name__ == "__main__":
    unittest.main()