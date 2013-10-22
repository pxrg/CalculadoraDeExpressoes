#!usr/bin/env python
#-*-coding:latin1-*-

class Analise(object):

    _tokens = []
    _alfabeto = '0123456789*/+-()'
    _operadores = '*/+-'
    _status = '+-'
    _estado = 0

    def lexica(self, expressao):
        lexema = ''
        for count in xrange(0, len(expressao)):
            i = expressao[count]
            if self._estado == 0:
                if self.validar_alfabeto(i, 'Caracter inválido no estado 0'): # verificar caracter valido
                    if i.isdigit():
                        lexema += i
                        self._estado = 1
                    elif self._status.find(i) != -1:
                        lexema += i
                        self._estado = 3
                    elif i == '(':
                        lexema += i
                        self._estado = 4
                    else:
                        raise Exception('Esse caracter não tem próximo estado.')
            elif self._estado == 1:
                if self.validar_alfabeto(i, 'Caracter inválido no estado 1'): # verificar caracter valido
                    if i.isdigit():
                        lexema += i
                        self.final(count, len(expressao) - 1, 1, lexema) # verifica estado final
                    elif self._operadores.find(i) != -1:
                        self._tokens.append(lexema)
                        lexema = ''
                        self._tokens.append(i)
                        self._estado = 2
                    else:
                        raise Exception('Esse caracter não tem próximo estado.')
            elif self._estado == 2:
                if self.validar_alfabeto(i, 'Caracter inválido no estado 2'): # verificar caracter valido
                    if i.isdigit():
                        lexema += i
                        self.final(count, len(expressao) - 1, 1, lexema) # verifica estado final
                    elif i == '(':
                        self._tokens.append(i)
                        self._estado = 4
                    else:
                        raise Exception('Esse caracter não tem próximo estado.')
            elif self._estado == 3:
                if self.validar_alfabeto(i, 'Caracter inválido no estado 3'): # verificar caracter valido
                    if i.isdigit():
                        lexema += i
                        self.final(count, len(expressao) - 1, 1, lexema) # verifica estado final
                    else:
                        raise Exception('Esse caracter não tem próximo estado.')
            elif self._estado == 4:
                if self.validar_alfabeto(i, 'Caracter inválido no estado 4'): # verificar caracter valido
                    if i.isdigit():
                        lexema += i
                        self._estado = 5
                    elif self._status.find(i) != -1:
                        lexema += i
                        self._estado = 7
                    else:
                        raise Exception('Esse caracter não tem próximo estado.')
            elif self._estado == 5:
                if self.validar_alfabeto(i, 'Caracter inválido no estado 5'): # verificar caracter valido
                    if i.isdigit():
                        lexema += i
                        self._estado = 5
                    elif self._operadores.find(i) != -1:
                        self._tokens.append(lexema)
                        lexema = ''
                        self._tokens.append(i)
                        self._estado = 4
                    elif i == ')':
                        self._tokens.append(lexema) # adicionado lexema antes, pois se trata de parenteses
                        lexema = '' # esvazia lexema, para não ser adicionada no estado final
                        self.final(count, len(expressao) - 1, 6, lexema) # verifica estado final
                        self._tokens.append(i)
                    else:
                        raise Exception('Esse caracter não tem próximo estado.')
            elif self._estado == 6:
                if self.validar_alfabeto(i, 'Caracter inválido no estado 6'): # verificar caracter valido
                    if self._operadores.find(i) != -1:
                        self._tokens.append(i)
                        self._estado = 2
                    else:
                        raise Exception('Esse caracter não tem próximo estado.')
            elif self._estado == 7:
                if self.validar_alfabeto(i, 'Caracter inválido no estado 7'): # verificar caracter valido
                    if i.isdigit():
                        lexema += i
                        self._estado = 5
                    else:
                        raise Exception('Esse caracter não tem próximo estado.')
                    
    def validar_alfabeto(self, char, msg):
        if self._alfabeto.find(char) != -1:
            return True
        else:
            raise Exception(msg)

    def final(self, count, condicao, estado, lexema):
        if count == condicao:
            if lexema != '':
                self._tokens.append(lexema)
        else:
            self._estado = estado
   
    def get_tokens(self):
        return self._tokens
                


class Token(object):

    def __init__(self, lexema, token):
        self.token = token
        self.lexema = lexema

def main():
    expressao = '-3*3+(+3-5)/3'
    analise = Analise()
    analise.lexica(expressao)
    print analise.get_tokens()

if __name__ == '__main__':
    main()
