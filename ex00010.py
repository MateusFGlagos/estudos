from random import choice
n1 = str(input('Digite um aluno: '))
n2 = str(input('Digite um aluno: '))
n3 = str(input('Digite um aluno: '))
n4 = str(input('Digite um aluno: '))
lista = [n1,n2,n3,n4]
escolhido = choice(lista)
print(escolhido)