somaIdade = 0
IdadeMaisVelho = 0
nomeMaisVelho = ''
numMulheres = 0

for i in range(1, 5):
    print(f'--- {i}º PESSOA ---')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo? [M/F] ')).upper().strip()
    somaIdade += idade

    if sexo == 'M' and idade > IdadeMaisVelho:
        IdadeMaisVelho = idade
        nomeMaisVelho = nome

    if sexo == 'F' and idade < 20:
        numMulheres += 1

mediaIdade = somaIdade / 4
print(f'A média de idade do grupo é de {mediaIdade:.2f} anos')
print(f'O homem mais velho tem {IdadeMaisVelho} e se chama {nomeMaisVelho}')
print(f'Ao todo são {numMulheres} mulheres com menos de 20 anos.')