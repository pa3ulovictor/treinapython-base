#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala que 
frequentas cada uma deas atividades
"""

__version__ = "0.1.1"

#Dados
sala1 = ["Paulo", "Rachel", "Zoro", "Costela", "Nico"]
sala2 = ["Clemir", "Jonas", "Anilson", "Cybelle"]

aula_ingles = ["Rachel", "Clemir", "Jonas", "Zoro", "Nico"]
aula_musica = ["Rachel", "Paulo", "Costela", "Anilson"]
aula_danca = ["Zoro", "Costela", "Nico", "Anilson"]

#Listar alunos em cada atividade por sala

#Fazer de forma agrupada

atividades = [
   ("Ingles", aula_ingles),
   ("Musica", aula_musica),
   ("Danca", aula_danca),
 ]

for nome_atividade, atividade in atividades:
        

    print(f"Alunos da atividade {nome_atividade}" )
    print()
    

#sala1 que tem interseção com a atividade


    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2).intersection(set(atividade))

    print(f" sala1 ", atividade_sala1)
    print(f" sala2 ", atividade_sala2)
    print()
    print("-" * 30)













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



