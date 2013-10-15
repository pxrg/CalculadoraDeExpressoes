#!usr/bin/env python
#-*-coding:latin1-*-

class Utils():

    @classmethod
    def find(self, expressao, character, index = 0):
        for i in xrange(index, len(expressao)):
            if expressao[i] == character:
                return i;
        return -1;

    @classmethod
    def replace(self, expressao, value, rep):
        novaExpressao = ""
        i = -1
        while (i < (len(expressao) - 1)):
            i += 1
            if expressao[i] == value[0]:
                validate = True
                for j in xrange(1, len(value)):
                    pos = i+j
                    if pos < len(expressao):
                        if not (expressao[pos] == value[j]):
                            novaExpressao += expressao[i]
                            validate = False
                            break
                    else:
                        novaExpressao += expressao[i]
                        validate = False
                        break
                if validate:
                    pos = i + (len(value) -1)
                    if pos < len(expressao):
                        novaExpressao += rep
                        i = pos
            else:
                novaExpressao += expressao[i]
        return novaExpressao

    @classmethod
    def is_digit(self, expressao):        
        for i in expressao:
            if not (i >= '0' and i <= '9'):
                return False
        return True

    @classmethod
    def split(self, expressao, character):
        values = []
        value = ""
        for i in expressao:
            if i == character:
                values.append(value)
                value = ""
            else:
                value += i
        if value != "":
            values.append(value)
        return values

    @classmethod
    def rsplit(self, expressao, character, count = 0):
        values = []
        value = ""
        iterator = 0
        for i in xrange(len(expressao), 0, -1):
            if (expressao[i-1] == character) and (iterator < count):
                values.insert(0, value)
                value = ""
                iterator += 1
            else:
                value = expressao[i-1] + value
        if value != "":
            values.insert(0, value)
        return values
                
    @classmethod
    def trim(self, expressao):
        newExpression = ""
        for i in expressao:
            if i != " ":
                newExpression += i
        return newExpression
        
