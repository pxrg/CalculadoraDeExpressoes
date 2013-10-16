#!usr/bin/env python
#-*-coding:utf-8-*-

from utils import *

class Analise():

    _caracteres_validos = "0123456789./*-+()"
    _operadores_validos = "/*-+"

    @classmethod
    def lexica(self, expressao):
        cont = 0
        for i in expressao:
            if Utils.find(self._caracteres_validos, i) == -1:
                raise LexicaError("Caracter inválido na coluna %d" % cont)
            cont += 1
        return True

    @classmethod
    def sintatica(self, expressao):
        if not Utils.is_digit(expressao[0]) and expressao[0] != '+' and expressao[0] != '-' and expressao[0] != '(':
            raise SintaticaError("Caracter não aceito para iniciar expressão : %s" % expressao[0])
        if not Utils.is_digit(expressao[len(expressao)-1]) and expressao[len(expressao)-1] != ')':
            raise SintaticaError("Caracter não aceito para terminar expressão : %s" % expressao[len(expressao)-1])

        open_parentheses = 0
        close_parentheses = 0
        pos = []
        
        for i in xrange(len(expressao)):
            if Utils.find(self._operadores_validos, expressao[i]) != -1 and Utils.find(self._operadores_validos, expressao[i+1]) != -1:
                raise SintaticaError("Sequência de operadores não aceito : col %d" % i)
            if Utils.is_digit(expressao[i]) and expressao[i+1] == '(':
                raise SintaticaError("Numéro seguido de parenteses não é permitido : col %d" % i)
            if expressao[i] == '(':
                open_parentheses += 1
                pos.append(i)
            if expressao[i] == ')':
                if open_parentheses == 0:
                    raise SintaticaError("Parenteses não foi aberto. : col %d" %(i))
                pos.pop(-1)
                close_parentheses += 1

        if open_parentheses != close_parentheses:
            raise SintaticaError("Existe parênteses não fechado. : col %s" %(pos))

        return True
            

class LexicaError(BaseException):

    def __init__(self, message = None):
        if message is not None:
            self.message = message
        else:
            self.message = "Erro na analise léxica!"

        print self.message

class SintaticaError(BaseException):

    def __init__(self, message = None):
        if message is not None:
            self.message = message
        else:
            self.message = "Erro na analise sintatica!"

        print self.message
