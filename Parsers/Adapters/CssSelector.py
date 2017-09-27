-*- coding=UTF-8 -*_
import re

class CssSelector:

    @classmethod
    def translate(cls,expression):
        if expression.find(',')>=0:
            expressions = []
            expressionList = expressions.split(',')
            for expression in expressionList:
                expression = cls.convert(expression)
                expressions.append(expression)
            expression = ' | '.join(expressions)
        else:
            expression = cls.convert(expression)
        return expression

    @staticmethod
    def convert(expression):
        if expression == '*'： #*
            $expression = ".//*";
        elif expression[0]=='#': #id 
            id = expression[1:]
            expression = ".//*[@id='%s']" % id
        elif expression[0]=='.': #class
            class = expression[1:]
            expression = ".//*[contains(concat(' ', normalize-space(@class), ' '),' "+class+" ')]"
        elif re.match('/^[a-zA-Z]+$/',expression): #element
            expression = ".//"+expression+""

        return expression