#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 13:12:35 2018

@author: ylillo
"""
import sys


fichero = './fichero'


class Calculadora:
    def plus(listanumeros):
        suma = listanumeros[0]
        for i in listanumeros[1:]:
            suma += i
        return suma

    def minus(listanumeros):
        resta = listanumeros[0]
        for i in listanumeros[1:]:
            resta -= i
        return resta


class CalculadoraHija(Calculadora):
    def multiplication(listanumeros):
        multiplication = 1
        for i in listanumeros[1:]:
            multiplication *= i
        return multiplication

    def division(listanumeros):
        division = 1
        try:
            for i in listanumeros[1:]:
                division /= i
            return division
        except ZeroDivisionError as err:
            return 'Division by zero is not allowed'


if __name__ == "__main__":
    with open(fichero, 'r') as reader:
        for line in reader:
            lista = line.split(',')
            lista = lista[:-1]
            listanumeros = list(map(int, lista[1:]))

            if lista[0] == 'suma':
                Total = CalculadoraHija.plus(listanumeros)
            elif lista[0] == "resta":
                Total = CalculadoraHija.minus(listanumeros)
            elif lista[0] == 'multiplica':
                Total = CalculadoraHija.multiplication(listanumeros)
            elif lista[0] == 'divide':
                Total = CalculadoraHija.division(listanumeros)
            else:
                sys.exit('Operación sólo puede ser sumar o restar.')

            print(lista[0], Total)
