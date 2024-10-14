qtdaluno = int(input('Digite quantos alunos: '))
valor = int(input('Digite o valor: '))
faturamento = qtdaluno * valor
lucro = faturamento * 0.8
custos = faturamento * 0.2
turma = qtdaluno / 3
print('O faturamento previsto é de {}, os custos vão ficar em {} e você recebera um lucro de {}'.format(faturamento,custos,lucro))
print('A quantidade de alunos por turma é {}'.format(turma))