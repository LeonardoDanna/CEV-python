x = float(input('Qual é o salário do funcionário? R$'))
novox = (x + ((x / 100) * 15))
print(f'O salário que era de R${x:.2f}, agora com aumento de 15%, será de R${novox:.2f}')
