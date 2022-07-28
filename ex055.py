maiorPeso = 0
menorPeso = 0

for i in range(0 + 1, 6):
    x = int(input(f'Peso da {i}º pessoa: '))
    if i == 1:
        maiorPeso = x
        menorPeso = x
    else:
        if x > maiorPeso:
            maiorPeso = x
        if x < menorPeso:
            menorPeso = x

print(f'O maior peso lido foi de {maiorPeso}Kg')
print(f'O menor peso lido foi de {menorPeso}Kg')