#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from calcoohija import CalculadoraHija


if __name__ == "__main__":
    fichero = sys.argv[1]
    try:
        fichero = open(nombre_fichero)
    except IOError:
        sys.exit("No existe el fichero indicado")
    calculadora1 = CalculadoraHija()

    for line in fichero.readlines():
        operacion_valores = line.split(',')
        acumulador = int(operacion_valores[1])
        if operacion_valores[0] == "suma":
            try:
                for valor in operacion_valores[2:]:
                    acumulador = calculadora1.suma(acumulador, int(valor))
                print(acumulador)
            except ValueError:
                print("Un valor en la suma no es valido")
        elif operacion_valores[0] == "resta":
            try:
                for valor in operacion_valores[2:]:
                    acumulador = calculadora1.resta(acumulador, int(valor))
                print(acumulador)
            except ValueError:
                print("Un valor en la resta no es valido")
        elif operacion_valores[0] == "multiplica":
            try:
                for valor in operacion_valores[2:]:
                    acumulador = calculadora1.mult(acumulador, int(valor))
                print(acumulador)
            except ValueError:
                print("Un valor en la multiplicacion no es valido")
        elif operacion_valores[0] == "divide":
            try:
                for valor in operacion_valores[2:]:
                    acumulador = calculadora1.div(acumulador, int(valor))
                print(acumulador)
            except ValueError:
                print("Un valor en la division no es valido")
        else:
            print("Las operaciones son: suma, resta, multiplica y divide")