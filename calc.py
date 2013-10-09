#!usr/bin/env python
#-*-coding:latin1-*-

class Calc():

    _caracteres_validos = "0123456789./*-+()"

    @classmethod
    def calcula(self, expressao):
        aux = self.limpaEspacos(expressao)        
        aux = self.eliminaParenteses(aux)
        return float(self.calculaExpressao(aux))

    @classmethod
    def limpaEspacos(self, string):
        aux = ""
        for e in string:
            if e in Calc._caracteres_validos:
                aux += e
        return aux

    @classmethod
    def eliminaParenteses(self, expressao):
        aux = expressao
        while(aux.find('(') != -1):
            aux = self.calculaParenteses(aux)
        return aux

    @classmethod
    def calculaParenteses(self, expressao):
        aux = expressao
        pos_inicial = aux.find('(')
        if pos_inicial != -1:   
            pos_final = aux.find(')', pos_inicial)
            valor_parenteses = aux[pos_inicial:pos_final+1]
            resultado = self.calculaExpressao(valor_parenteses[1:-1])
            aux = aux.replace(valor_parenteses, '%s'%resultado)            
        return aux

    @classmethod
    def calculaOperacao(self, expressao, operacao):
        aux = expressao
        operador = aux.find(operacao)
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
                aux = aux.replace(valor, '%d'%resultado)    
                break
        return aux

    @classmethod
    def eliminaSomaSubtracao(self, expressao):
        aux = expressao
        pos_fim = -1
        operador = False
        for pos in xrange(len(expressao)):
            if pos == 0:
                continue
            if not aux[pos].isdigit():
                if not operador:
                    operador = True
                else:
                    pos_fim = pos
                    break
        if operador:
            valor = aux[0:pos_fim]
            qtd = len(aux)
            if pos_fim >= (qtd -1) or pos_fim == -1:
                valor = aux[::]         
            resultado = self.efetuaOperacao(valor)
            aux = aux.replace(valor, '%d'%resultado)
        return aux
        

    @classmethod
    def calculaExpressao(self, expressao):
        aux = expressao
        for op in ('*', '/'):
            while(aux.find(op) != -1):
                aux = self.calculaOperacao(aux, op)
        copiaAux = ''
        while(copiaAux != aux):
            copiaAux = aux.strip()
            aux = self.eliminaSomaSubtracao(aux)
            
        return aux    

    @classmethod
    def efetuaOperacao(self, expressao):
        total = 0
        pos_padrao = 1
        if expressao.find('*',1) >= pos_padrao:
            val = expressao.split('*')
            total = float(val[0]) * float(val[1])
        elif expressao.find('/',1) >= pos_padrao:
            val = expressao.split('/')
            total = float(val[0]) / float(val[1])
        elif expressao.find('+',1) >= pos_padrao:
            val = expressao.split('+')
            total = float(val[0]) + float(val[1])
        elif expressao.find('-',1) >= pos_padrao:
            val = expressao.rsplit('-',1)
            total = float(val[0]) - float(val[1])        
        else:
            total = float(expressao)
        return total
            

