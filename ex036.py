x = float(input('Valor da casa: R$'))
y = float(input('Salário do comprador: R$'))
z = float(input('Quantos anos de financiamento? '))

valorMinimo = (y / 100) * 30
prestacao = x / (z * 12)

print(f'Para pagar uma casa de R${x} em {z} anos a prestação será de R${prestacao:.2f}')

if prestacao > valorMinimo:
    print('Empréstimo negado')
else:
    print('Empréstimo aprovado')
