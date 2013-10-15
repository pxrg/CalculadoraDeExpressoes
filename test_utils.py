#!usr/bin/env python
#-*-coding:latin1-*-

import unittest
from utils import *

class utilsTest(unittest.TestCase):

    def test_find(self):
        text = "3/5-(3+5-9)*3"
        find = '('
        self.assertEqual(text.find(find), Utils.find(text, find))

    def test_findIndex(self):
        text = "3/5-(3+5-9)*3+(-3*8)"
        find = ')'
        self.assertEqual(text.find(find,4), Utils.find(text, find, 4))

    def test_findNotFound(self):
        text = "3/5-(3+5-9)*3"
        find = '&'
        self.assertEqual(text.find(find), Utils.find(text, find))

    def test_replaceInitial(self):
        text = "3/5-(3+5-9)*3"
        value = "3/5"
        replace = "AA"
        self.assertEqual(text.replace(value, replace), Utils.replace(text, value, replace))

    def test_replaceMiddle(self):
        text = "3/5-(3+5-9)*3"
        value = "(3+5-9)"
        replace = "AA"
        self.assertEqual(text.replace(value, replace), Utils.replace(text, value, replace))

    def test_replaceFinal(self):
        text = "3/5-(3+5-9)*3"
        value = "9)*3"
        replace = "AA"
        self.assertEqual(text.replace(value, replace), Utils.replace(text, value, replace))

    def test_is_digitsSemPotuacao(self):
        text = "356"
        self.assertEqual(text.isdigit(), Utils.is_digit(text))

    def test_is_digitsSemPotuacaoComLetra(self):
        text = "356a"
        self.assertEqual(text.isdigit(), Utils.is_digit(text))

    def test_split(self):
        text = "5698*96"
        split = "*"
        self.assertEqual(text.split(split), Utils.split(text, split))

    def test_splitNotFound(self):
        text = "569896"
        split = "*"
        self.assertEqual(text.split(split), Utils.split(text, split))

    def test_rsplit(self):
        text = "-569-896"
        split = "-"
        self.assertEqual(text.rsplit(split, 1), Utils.rsplit(text, split, 1))

    def test_rsplitComMaisQuebras(self):
        text = "-56-989-656"
        split = "-"
        self.assertEqual(text.rsplit(split, 2), Utils.rsplit(text, split, 2))

    def test_rsplitNotFound(self):
        text = "56989656"
        split = "-"
        self.assertEqual(text.rsplit(split, 1), Utils.rsplit(text, split, 1))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(utilsTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    main()
