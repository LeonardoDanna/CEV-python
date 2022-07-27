x = float(input('Qual seu peso? (Kg): '))
x2 = float(input('Qual sua altura? (m): '))

imc = x / (x2 ** 2)

print(f'O IMC dessa pessoa é {imc:.1f}')
print(f'Você está ', end='')

if imc <= 18.5:
    print('abaixo do peso ideal')
elif 18.5 <= imc <= 24.9:
    print('no peso ideal')
elif 25 <= imc <= 30:
    print('acima do peso ideal')
elif 30 <= imc <= 40:
    print('com obesidade')
else:
    print('com obesidade mórbida')
