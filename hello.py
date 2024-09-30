#!/usr/bin/env  python3
"""Hello World Multi Linguas
Dependendo da lingua configurada no ambiente o progama exibe a 
correspondente.

Como usar:

Tenha a varíavel de LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.2"
__author__ = "Paulo Victor"
__licinse__ = "Unlicense"

import os 

current_language = os.getenv ("LANG", "en_US") [:5]
# Aqui pegamos a linguagem até o caracter 5 
msg = {
        "en_US" : "Hello world",
        "pt_BR" : "Olá, Mundo!",
        "it_IT" : "Cioa Mondo",
        "es_SP" : " Hola, Mundo",
        "fr_FR" : "Bonjour MOnde",
        }
#Ordem de complexidade O(n)

#if current_language == "pt_BR":
 #   msg = "Olá, Mundo!"
#elif current_language == "it_IT":
 #   msg = "Ciao, Mondo!"
#elif current_language == "es_SP":
#    msg = "Hola, Mundo!"
#elif current_language == "fr_FR":
#    msg = "Bonjour Monde"
    
print(msg[current_language])

