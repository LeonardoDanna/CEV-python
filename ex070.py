prodBaratoCusto = MaisQueMil = preçotot = menor = cont = 0
prodBarato = ''

print(20 * '-')
print('LOJA SUPER BARATÃO')
print(20 * '-')

while True:
    x = str(input('Nome do produto: '))
    y = float(input('Preço: R$'))
    preçotot += y
    cont += 1

    if y >= 1000:
        MaisQueMil += 1

    if cont == 1 or y < menor:
        menor = y
        prodBarato = x

    z = str(input('Quer continuar? [S/N]] ')).strip().upper()[0]
    if z == 'N':
        break

print('--- FIM DO PROGRAMA ---')
print(f'O total da compra foi R${preçotot}')
print(f'Ao todo temos {MaisQueMil} produtos custando mais de R$1000')
print(f'O produto mais barato foi {prodBarato} que custa R${menor:.2f}')