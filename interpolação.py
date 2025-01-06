#!/user/bin/env python3
"""Impreme a mensagem de um e-mail


NÂO MANDE SPAM!!!
"""
__version__ = "0.1.1"




import sys
import os

arguments = sys.argv[1:]
if not arguments:
    print("informa o nome do arquivo de emails")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename) # emails.txt
templatepath = os.path.join(path,templatename) # email_tmpl.txt

for line in open(filepath):
     name, email = line.split(",")    

     # TODO Substituir por envio de email
     print(f"Enviando email para: {email}")
     print()
     print(
         open(templatepath).read()
          % {
              "nome": name,
              "produtos": "caneta",
              "texto": "escreve muito bem",
              "link": "https://canetaslegias.com",
              "quantidade": 1,
              "preco": 50.0,

         }
    )
     print ("-" * 50)

