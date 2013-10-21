#!usr/bin/env python
#-*-coding:latin1-*-

import unittest
from gramatica import *

class testGramatica(unittest.TestCase):

    def testGramaticaGerarTokens(self):
        expressao = '3+45*2-7'
        esperado = ['3','+','45','*','2','-','7']
        self.assertEquals(esperado, Gramatica.gerarTokens(expressao))

    def testGramaticaGerarTokensPrimeiroNumeroNegativo(self):
        expressao = '-3+45*2-7'
        esperado = ['-3','+','45','*','2','-','7']
        self.assertEquals(esperado, Gramatica.gerarTokens(expressao))

    def testGramaticaGerarTokensComParenteses(self):
        expressao = '-3+(45*2)-7'
        esperado = ['-3','+','(','45','*','2',')','-','7']
        self.assertEquals(esperado, Gramatica.gerarTokens(expressao))

    def testGramaticaGerarTokensUmNumero(self):
        expressao = '-3'
        esperado = ['-3']
        self.assertEquals(esperado, Gramatica.gerarTokens(expressao))

    def testGramaticaNumeroValido(self):
        numero = '56'
        self.assertEquals(True, Gramatica.numero(numero))

    def testGramaticaNumeroValidoNegatico(self):
        numero = '-56'
        self.assertEquals(True, Gramatica.numero(numero))
        
def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(testGramatica)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()
