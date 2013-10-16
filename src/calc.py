#!usr/bin/env python
#-*-coding:utf-8-*-

from utils import *

class Calc():

    @classmethod
    def calcula(self, expressao):
        aux = Utils.trim(expressao)
        aux = self.eliminaParenteses(aux)
        return float(self.calculaExpressao(aux))

    @classmethod
    def eliminaParenteses(self, expressao):
        aux = expressao
        while(Utils.find(aux, '(') != -1):
            aux = self.calculaParenteses(aux)
        return aux

    @classmethod
    def calculaParenteses(self, expressao):
        aux = expressao
        pos_inicial = Utils.find(aux, '(')
        if pos_inicial != -1:   
            pos_final = Utils.find(aux, ')', pos_inicial)
            valor_parenteses = aux[pos_inicial:pos_final+1]
            resultado = self.calculaExpressao(valor_parenteses[1:-1])
            aux = Utils.replace(aux, valor_parenteses, '%s'%resultado)
        return aux

    @classmethod
    def calculaOperacao(self, expressao, operacao):
        aux = expressao
        operador = Utils.find(aux, operacao)
        inicio = False
        fim = False
        pos_ini = operador -1
        pos_fim = operador +1
        for e in xrange(len(expressao)):
            if pos_ini > -1 and aux[pos_ini].isdigit():
                pos_ini -= 1
            else:
                inicio = True
            if pos_fim < len(aux) and aux[pos_fim].isdigit():
                pos_fim += 1
            else:
                fim = True
            if inicio and fim:
                valor = aux[pos_ini+1:pos_fim]
                resultado = self.efetuaOperacao(valor)
                aux = Utils.replace(aux, valor, '%d'%resultado)    
                break
        return aux

    @classmethod
    def eliminaSomaSubtracao(self, expressao):
        aux = expressao
        valores = Utils.split(expressao, '+')
        total = 0
        for val in valores:
            total += self.efetuaOperacao(val)
        return '%d'%total
        
    @classmethod
    def calculaExpressao(self, expressao):
        aux = expressao
        for op in ('*', '/'):
            while(Utils.find(aux, op) != -1):
                aux = self.calculaOperacao(aux, op)
        copiaAux = ''
        while(copiaAux != aux):
            copiaAux = Utils.trim(aux)
            aux = self.eliminaSomaSubtracao(aux)
            
        return aux    

    @classmethod
    def efetuaOperacao(self, expressao):
        total = 0
        pos_padrao = 1
        if Utils.find(expressao,'*',1) >= pos_padrao:
            val = Utils.split(expressao, '*')
            total = float(val[0]) * float(val[1])
        elif Utils.find(expressao,'/',1) >= pos_padrao:
            val = Utils.split(expressao, '/')
            total = float(val[0]) / float(val[1])
        elif Utils.find(expressao,'+',1) >= pos_padrao:
            val = Utils.split(expressao, '+')
            total = float(val[0]) + float(val[1])
        elif Utils.find(expressao,'-',1) >= pos_padrao:
            val = Utils.rsplit(expressao, '-',1)
            total = float(val[0]) - float(val[1])        
        else:
            total = float(expressao)
        return total
            

