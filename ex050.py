resultado = 0
for i in range(0,6):
    x = int(input(f'[ {i+1} ] Digite um número: '))
    if x % 2 == 0:
        resultado += x
print(f'A soma dos valores pares é igual a {resultado}')
