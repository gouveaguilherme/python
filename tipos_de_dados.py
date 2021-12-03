
'''
tipos de dados em python
 - Os tipos de dado em python sao definidos atraves da sintaxe, nao e preciso dizer o tipo do dado. Porem se necessario e possivel definir o tipo do dado, assim como no exeplo abaixo;

'''

#DADOS NUMERICOS (INT e FLOAT)

n1 = 12
n2 = 12.5
n3 = int(13.9)
n4 = float(12)

#DADOS DO TIPO TEXTO (STRING)

w1 = "Pode ser usado aspas duplas"
w2 = 'Mas tbm pode ser usado aspas simples'
w3 = "No caso de precisar usar algo com apostrofe como a palavra d'agua, utilizamos aspas duplas"
w4 = str('epecificando o tipo de dado')

#LISTAS, TUPLAS E DICIONARIOS

lista = ['Maria', 32,] # No array e possivel, adicionar, remover e alterar elementos

tupla = ('Rosa', 43) # A tupla funciona da mesma forma que o array, porem ela e imutavel. Ou seja, nao e possivel adicionar, remover ou alterar elementos.

dicionario = {  'Nome':'Alice', # o dicionario tambem semelhante ao array, porem no caso dele sua estrutura e sempre composta de uma chave e de um valor.
                'Idade':25
                }

#BOOLEAN (verdadeiro ou falso) tipo de dado logico

condicao = True

#OBS: E POSSIVEL DECLARAR VARIAVEIS POR JUSTAPOSICAO, COMO NO EXEMPLO ABAIXO

name, age, race = 'Legolas', 300, 'Elf'

print(  'Nome: ',name,'\n'
        'Idade: ',age,'\n'
        'Race: ',race)
