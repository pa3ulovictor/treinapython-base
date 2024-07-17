#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10.

Tabuada do 1
1
2
3
...
_________________

Tabuada do 2
2
4
...
_________________

"""
__version__ = "0.1.0"
__author__ = "Paulo Victor"

#  numeros = [1,2,3,4,5,6,7,8,9,10]
numeros =list(range(1, 11))

# Iterable (pecorriveis)

# para cada numero em numeros
for numero in numeros:
    print("Tabuada do:", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("____________")

