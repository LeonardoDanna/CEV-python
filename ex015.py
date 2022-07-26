x = int(input('Quantos dias alugados? '))
y = int(input('Quantos KM rodados? '))
pago = (x * 60) + (y * 0.15)
print(f'O total a pagar é de R${pago:.2f}')