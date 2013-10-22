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
                if self.validar_alfabeto(i, 'Caracter inválido no estado 0 : Coluna %d' % count): # verificar caracter valido
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
                        raise Exception('Sequência de caracter inválido. : Coluna %d' % count)
            elif self._estado == 1:
                if self.validar_alfabeto(i, 'Caracter inválido no estado 1 : Coluna %d' % count): # verificar caracter valido
                    if i.isdigit():
                        lexema += i
                        self.final(count, len(expressao) - 1, 1, lexema) # verifica estado final
                    elif self._operadores.find(i) != -1:
                        self._tokens.append(Token(lexema, 'numero'))
                        lexema = ''
                        self._tokens.append(Token(i, 'operador'))
                        self._estado = 2
                    else:
                        raise Exception('Sequência de caracter inválido. : Coluna %d' % count)
            elif self._estado == 2:
                if self.validar_alfabeto(i, 'Caracter inválido no estado 2 : Coluna %d' % count): # verificar caracter valido
                    if i.isdigit():
                        lexema += i
                        self.final(count, len(expressao) - 1, 1, lexema) # verifica estado final
                    elif i == '(':
                        self._tokens.append(Token(i, 'parenteses'))
                        self._estado = 4
                    else:
                        raise Exception('Sequência de caracter inválido. : Coluna %d' % count)
            elif self._estado == 3:
                if self.validar_alfabeto(i, 'Caracter inválido no estado 3 : Coluna %d' % count): # verificar caracter valido
                    if i.isdigit():
                        lexema += i
                        self.final(count, len(expressao) - 1, 1, lexema) # verifica estado final
                    else:
                        raise Exception('Sequência de caracter inválido. : Coluna %d' % count)
            elif self._estado == 4:
                if self.validar_alfabeto(i, 'Caracter inválido no estado 4 : Coluna %d' % count): # verificar caracter valido
                    if i.isdigit():
                        lexema += i
                        self._estado = 5
                    elif self._status.find(i) != -1:
                        lexema += i
                        self._estado = 7
                    else:
                        raise Exception('Sequência de caracter inválido. : Coluna %d' % count)
            elif self._estado == 5:
                if self.validar_alfabeto(i, 'Caracter inválido no estado 5 : Coluna %d' % count): # verificar caracter valido
                    if i.isdigit():
                        lexema += i
                        self._estado = 5
                    elif self._operadores.find(i) != -1:
                        self._tokens.append(Token(lexema, 'numero'))
                        lexema = ''
                        self._tokens.append(Token(i, 'operador'))
                        self._estado = 4
                    elif i == ')':
                        self._tokens.append(Token(lexema, 'numero')) # adicionado lexema antes, pois se trata de parenteses
                        lexema = '' # esvazia lexema, para não ser adicionada no estado final
                        self.final(count, len(expressao) - 1, 6, lexema) # verifica estado final
                        self._tokens.append(Token(i, 'parenteses'))
                    else:
                        raise Exception('Sequência de caracter inválido. : Coluna %d' % count)
            elif self._estado == 6:
                if self.validar_alfabeto(i, 'Caracter inválido no estado 6 : Coluna %d' % count): # verificar caracter valido
                    if self._operadores.find(i) != -1:
                        self._tokens.append(Token(i, 'operador'))
                        self._estado = 2
                    else:
                        raise Exception('Sequência de caracter inválido. : Coluna %d' % count)
            elif self._estado == 7:
                if self.validar_alfabeto(i, 'Caracter inválido no estado 7 : Coluna %d' % count): # verificar caracter valido
                    if i.isdigit():
                        lexema += i
                        self._estado = 5
                    else:
                        raise Exception('Sequência de caracter inválido. : Coluna %d' % count)
                    
    def validar_alfabeto(self, char, msg):
        if self._alfabeto.find(char) != -1:
            return True
        else:
            raise Exception(msg)

    def final(self, count, condicao, estado, lexema):
        if count == condicao:
            if lexema != '':
                self._tokens.append(Token(lexema, 'numero'))
        else:
            self._estado = estado
   
    def get_tokens(self):
        return self._tokens
                


class Token(object):

    def __init__(self, lexema, token):
        self.lexema = lexema
        self.token = token

def main():
    expressao = '-3*3+(+3-5)/3'
    analise = Analise()
    analise.lexica(expressao)
    for i in analise.get_tokens():
        print "Lexema: %s\tToken: %s" % (i.lexema, i.token)

if __name__ == '__main__':
    main()
