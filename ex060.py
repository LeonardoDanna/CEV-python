x = int(input('Digite um número para calcular seu fatorial: '))

contador = x
f = 1

print(f'Calculando {x}! = ', end='')
while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    f *= contador
    contador -= 1
print(f'{f}')
