#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 13:12:35 2018

@author: ylillo
"""
import sys
import calcoohija

fichero = './fichero'


with open(fichero, 'r') as reader:
    for line in reader:
        lista = line.split(',')
        lista = lista[:-1]
        listanumeros = list(map(int, lista[1:]))
        print(listanumeros)
        
        
 
        

                
             
       
        
 