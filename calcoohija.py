#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 09:40:20 2018

@author: ylillo
"""

import sys
import calcoo


class CalculadoraHija(calcoo.Calculadora):
    def multiplication(self, op1, op2):
        return op1 * op2

    def division(self, op1, op2):
        try:
            return op1 / op2
        except ZeroDivisionError as err:
            return 'Division by zero is not allowed'


if __name__ == "__main__":
    micalchija = CalculadoraHija()
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        Total = micalchija.plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        Total = micalchija.minus(operando1, operando2)
    elif sys.argv[2] == 'multiplica':
        Total = micalchija.multiplication(operando1, operando2)
    elif sys.argv[2] == 'divide':
        Total = micalchija.division(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print(Total)
