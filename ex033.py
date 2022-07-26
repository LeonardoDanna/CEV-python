x1 = int(input('Primeiro valor: '))
x2 = int(input('Primeiro valor: '))
x3 = int(input('Primeiro valor: '))

# Verificando quem é o menor
menor = x1
if x2 < x1 and x2 < x3:
    menor = x2
if x3 < x1 and x3 < x2:
    menor = x3
print(f'O menor valor digitado foi {menor}')

# Verificando quem é o maior
maior = x1
if x2 > x1 and x2 > x3:
    maior = x2
if x3 > x1 and x3 > x2:
    maior = x3
print(f'O maior valor digitado foi {maior}')
