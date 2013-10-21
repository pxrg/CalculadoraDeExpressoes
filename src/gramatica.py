#!usr/bin/env python
#-*-coding:latin1-*-

class Gramatica(object):

    _operadores = '*/+-'

    @classmethod
    def calcular(self, expressao):
        tokens = self.gerarTokens(expressao)
        exp = ''
        if tokens.count('*') > 0:
            pos = tokens.index('*')
            resultado = int(tokens[pos-1]) * int(tokens[pos+1])
            print resultado
            expressao = expressao.replace((tokens[pos-1] + '*' + tokens[pos+1]), resultado)
        return expressao
            
    @classmethod
    def gerarTokens(self, expressao):
        lista = []
        token = ''
        i = -1
        while (i < len(expressao) -1):
            i += 1
            if i == 0 and (expressao[i] == '-' or expressao[i] == '+'):
                token += expressao[i]
            else:
                if Gramatica.operador(expressao[i]) or expressao[i] == '(' or expressao[i] == ')':
                    if token != '': lista.append(token)
                    token = ''
                    lista.append(expressao[i])
                else:
                    token += expressao[i]
                    
        if token != '': lista.append(token)
        return lista

    @classmethod
    def operador(self, caracter):
        for i in self._operadores:
            if caracter == i:
                return True
        return False

    @classmethod
    def numero(self, expressao):
        indice = 0
        if expressao[indice] == '-' or expressao[indice] == '+':
            indice = 1

        for i in xrange(indice, len(expressao)):
            if not (expressao[i] >= '0' and expressao[i] <= '9'):
                return False
        return True

def main():
    expressao = '3+45*2-7'
    print Gramatica.calcular(expressao)

if __name__ == "__main__":
    main()
