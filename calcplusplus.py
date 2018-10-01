#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 15:47:35 2018

@author: ylillo
"""

import sys
import csv
import calcoohija

fichero = './fichero'


if __name__ == "__main__":
    with open(fichero, 'r') as csvfd:
        entrada = list(csv.reader(csvfd, delimiter=','))
        try:
            micalchija = calcoohija.CalculadoraHija()
        except ValueError:
            sys.exit("Error: Non numerical parameters")
        for line in entrada:
            listanumeros = list(map(int, line[1:]))

            op1 = listanumeros[0]
            if line[0] == 'suma':
                for op2 in listanumeros[1:]:
                    op1 = micalchija.plus(op1, op2)
            elif line[0] == "resta":
                for op2 in listanumeros[1:]:
                    op1 = micalchija.minus(op1, op2)
            elif line[0] == 'multiplica':
                for op2 in listanumeros[1:]:
                    op1 = micalchija.multiplication(op1, op2)
            elif line[0] == 'divide':
                for op2 in listanumeros[1:]:
                    if op1 == 0 or op2 == 0:
                        print('Division by zero is not allowed')
                    else:
                        op1 = micalchija.division(op1, op2)
            else:
                sys.exit('Operación sólo puede ser sumar o restar.')

            print(line[0], op1)
