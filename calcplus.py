#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 13:12:35 2018

@author: ylillo
"""
import sys
import calcoohija

fichero = './fichero'


if __name__ == "__main__":
    fd = open("fichero", encoding='utf-8', mode="r")
    try:
        micalchija = calcoohija.CalculadoraHija()
    except ValueError:
        sys.exit("Error: Non numerical parameters")
    for line in fd:
        lista = line.split(',')
        listanumeros = list(map(int, lista[1:]))

        op1 = listanumeros[0]
        if lista[0] == 'suma':
            for op2 in listanumeros[1:]:
                op1 = micalchija.plus(op1, op2)
        elif lista[0] == "resta":
            op1 = listanumeros[0]
            for op2 in listanumeros[1:]:
                op1 = micalchija.minus(op1, op2)
        elif lista[0] == 'multiplica':
            for op2 in listanumeros[1:]:
                op1 = micalchija.multiplication(op1, op2)
        elif lista[0] == 'divide':
            for op2 in listanumeros[1:]:
                if op1 == 0 or op2 == 0:
                    print('Division by zero is not allowed')
                else:
                    op1 = micalchija.division(op1, op2)

        else:
            sys.exit('Operación sólo puede ser sumar o restar.')

        print(lista[0], op1)
    fd.close()
