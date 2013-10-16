#!usr/bin/env python
#-*-coding:latin1-*-

import unittest
from calc import *

class calcTest(unittest.TestCase):

    def test_calcularSomaSimples(self):
        conta = "5+3"
        resultado = Calc.calcula(conta)
        self.assertEqual(5+3, resultado)

    def test_calcularSubtracaoSimples(self):
        conta = "5-3"
        resultado = Calc.calcula(conta)
        self.assertEqual(5-3, resultado)

    def test_calcularDivisaoSimples(self):
        conta = "6/3"
        resultado = Calc.calcula(conta)
        self.assertEqual(6/3, resultado)

    def test_calcularMultiplicacaoSimples(self):
        conta = "5*3"
        resultado = Calc.calcula(conta)
        self.assertEqual(5*3, resultado)

    def test_calculoComParenteses(self):
        conta = "20-(10+5)+7"
        self.assertEquals("20-15+7", Calc.eliminaParenteses(conta))

    def test_calculoComMaisDeUmParenteses(self):
        conta = "20-(10+5)+7+(9*3)+8+(15-10)"
        self.assertEquals("20-15+7+27+8+5", Calc.eliminaParenteses(conta))

    def test_eliminarParenteses(self):
        conta = "(5)"
        self.assertEquals("5", Calc.eliminaParenteses(conta))

    def test_efetuarCalculoESimplificarExpressao(self):
        conta = "3+9-5*8+1"
        self.assertEquals("3+9-40+1", Calc.calculaOperacao(conta, '*'))

    def test_efetuarCalculoERetornarResultadoFinal(self):
        conta = "3+9-5*8+1"
        self.assertEquals((3+9-5*8+1), Calc.calcula(conta))

    def test_eliminarSomaSubtracao(self):
        conta = "3+9-5*8+1"
        self.assertEquals("12-5*8+1", Calc.eliminaSomaSubtracao(conta))

    def test_efetuarCalculoERetornarResultadoFinalComParenteses(self):
        conta = "3+9-5*8+1+(10/2)-100"
        self.assertEquals((3+9-5*8+1+(10/2)-100), Calc.calcula(conta))

    def test_expressaoValidacaoFinal(self):
        expressao = "1+(3*2+3-1+3)+5*2*(10+5)"
        self.assertEquals((1+(3*2+3-1+3)+5*2*(10+5)), Calc.calcula(expressao))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(calcTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    main()
        
    
