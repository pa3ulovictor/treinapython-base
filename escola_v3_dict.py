#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala que 
frequentas cada uma deas atividades
utilizando dicionario
"""

__version__ = "0.1.2"

from pprint import pprint


#Dados
#sala1 = ["Paulo", "Rachel", "Zoro", "Costela", "Nico"]
escola = {
        "sala1": ["Paulo", "Rachel", "Zoro", "Costela", "Nico"],
        "sala2": ["Clemir", "Anilson", "Jonas", "Cibele"],
 }
#sala2 = ["Clemir", "Jonas", "Anilson", "Cybelle"]

aula = {
        "Ingles": ["Rachel", "Clemir", "Jonas", "Zoro", "Nico"],
        "Musica": ["Rachel", "Paulo", "Costela", "Anilson"],
        "Danca": ["Zoro", "Costela", "Nico", "Anilson"],
 }
#aula_ingles = ["Rachel", "Clemir", "Jonas", "Zoro", "Nico"]
#aula_musica = ["Rachel", "Paulo", "Costela", "Anilson"]
#aula_danca = ["Zoro", "Costela", "Nico", "Anilson"]

#Listar alunos em cada atividade por sala

#Fazer de forma agrupada
Turma ={
        "Aula_ingles": "Ingles"
 }

atividades_ingles = {
#        "Turma": Turma,
        "Ingles": aula ["Ingles"]
#        "Danca": aula_danca,
 }

atividades_musica= {
        "Musica": aula ["Musica"]
 }

atividades_danca= {
        "Danca": aula ["Danca"]
 }

#para_atividades = atividades_ingles["atividades_ingles"]

print(
   f"Os alunos da sala {atividades_ingles['atividades_ingles']}",
   f"Os alunos da sala {'atividades_musica'}", 
   f"Os alunos da sala {'atividade_danca'}",
 )
#pprint(
        atividades_ingles)
#pprint(
          atividades_musica)

#pprint(  atividades_danca
        )

#for nome_atividade, atividade in atividades:
        

#    print(f"Alunos da atividade {nome_atividade}" )
#    print()
    

#sala1 que tem interseção com a atividade


#    atividade_sala1 = set(sala1) & set(atividade)
#    atividade_sala2 = set(sala2).intersection(set(atividade))

#    print(f" sala1 ", atividade_sala1)
#    print(f" sala2 ", atividade_sala2)
#   print()
#   print("-" * 30)













#Exemplo de como fazer o codigo de forma simples, de modo que podesse 
#repetir o mesmo codigo para obter os resultados de outras salas de aula
#Basta copiar o codigo como esta e alterar pelas listas desejadas


#aula_ingles_sala1 = []
#aula_ingles_sala2 = []

#for aluno in aula_ingles:
#    if aluno in sala1:
#        aula_ingles_sala1.append(aluno)
#    elif aluno in sala2:
#        aula_ingles_sala2.append(aluno)

#print("ingles sala1 ", aula_ingles_sala1)
#print("ingles sala2 ", aula_ingles_sala2)



