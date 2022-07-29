mulheresMenor20 = homemCadastrado = deMaior = 0

while True:
    print(15 * '-')
    print('CADASTRE UMA PESSOA')
    print(15 * '-')
    x = int(input('Idade: '))
    if x >= 18:
        deMaior += 1
    y = str(input('Sexo: [M/F]] ')).strip().upper()[0]
    if y == 'M':
        homemCadastrado += 1
    if y == 'F':
        if x <= 20:
            mulheresMenor20 += 1
    z = str(input('Quer continuar? [S/N]] ')).strip().upper()[0]
    if z == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {deMaior}')
print(f'Ao todo temos {homemCadastrado} rapaz(es) cadastrado(s)')
print(f'E temos {mulheresMenor20} mulher(es) com menos de 20 anos.')