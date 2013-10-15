#!usr/bin/env python
#-*-coding:latin1-*-

import unittest
from analise import *

class analiseTest(unittest.TestCase):

    def test_lexica(self):
        expressao = "2+5.$-9/8*2+(8-2+a)"
        self.assertRaises(LexicaError, Analise.lexica, expressao)

    def test_lexicaValido(self):
        expressao = "2+5-9/8*2+(8-2)"
        self.assertEqual(True, Analise.lexica(expressao))

    def test_sintatica(self):
        expressao = "*2+5-9/8*2+(8-2)"
        self.assertRaises(SintaticaError, Analise.sintatica, expressao)

    def test_sintaticaSequenciaOperadores(self):
        expressao = "2+5--9/8*2+(8-2)"
        self.assertRaises(SintaticaError, Analise.sintatica, expressao)

    def test_sintaticaOperadorNoFinal(self):
        expressao = "2+5-9/8*2+(8-2)+6+"
        self.assertRaises(SintaticaError, Analise.sintatica, expressao)

    def test_sintaticaParentesesAberto(self):
        expressao = "2+5-9/8*2+(8-2)+(6"
        self.assertRaises(SintaticaError, Analise.sintatica, expressao)

    def test_sintaticaValido(self):
        expressao = "2+5-9/8*2+(8-2)+(6)"
        self.assertEqual(True, Analise.sintatica(expressao))
    
def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(analiseTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    main()
