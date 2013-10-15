#!usr/bin/env python
#-*-coding:latin1-*-

from utils import *

class Analise():

    _caracteres_validos = "0123456789./*-+()"
    _operadores_validos = "/*-+"

    @classmethod
    def lexica(self, expressao):
        cont = 0
        for i in expressao:
            if Utils.find(self._caracteres_validos, i) == -1:
                raise LexicaError("Caracter inv�lido na coluna %d" % cont)
            cont += 1
        return True

    @classmethod
    def sintatica(self, expressao):
        if not Utils.is_digit(expressao[0]) and expressao[0] != '+' and expressao[0] != '-':
            raise SintaticaError("Caracter n�o aceito para iniciar express�o : %s" % expressao[0])
        if not Utils.is_digit(expressao[len(expressao)-1]) and expressao[len(expressao)-1] != ')':
            raise SintaticaError("Caracter n�o aceito para terminar express�o : %s" % expressao[len(expressao)-1])

        open_parentheses = 0
        close_parentheses = 0
        pos = []
        
        for i in xrange(len(expressao)):
            if Utils.find(self._operadores_validos, expressao[i]) != -1 and Utils.find(self._operadores_validos, expressao[i+1]) != -1:
                raise SintaticaError("Sequ�ncia de operadores na aceito : col %d" % i)
            if expressao[i] == '(':
                open_parentheses += 1
                pos.append(i)
            if expressao[i] == ')':
                pos.pop(-1)
                close_parentheses += 1

        if open_parentheses != close_parentheses:
            raise SintaticaError("Existe par�nteses n�o fechado. : col %s" %(pos))

        return True
            

class LexicaError(BaseException):

    def __init__(self, message = None):
        if message is not None:
            self.message = message
        else:
            self.message = "Erro na analise l�xica!"

        print self.message

class SintaticaError(BaseException):

    def __init__(self, message = None):
        if message is not None:
            self.message = message
        else:
            self.message = "Erro na analise sintatica!"

        print self.message
