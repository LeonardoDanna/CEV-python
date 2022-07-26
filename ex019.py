import random
x1 = str(input('Primeiro aluno: '))
x2 = str(input('Segundo aluno: '))
x3 = str(input('Terceiro aluno: '))
x4 = str(input('Quarto aluno: '))

lista = [x1, x2, x3, x4]
escolhido = random.choice(lista)

print(f'O aluno escolhido foi {escolhido}')
