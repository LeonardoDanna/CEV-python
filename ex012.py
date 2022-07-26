x = float(input('Qual é o preço do produto? R$'))
novox = (x - ((x / 100) * 5))
print(f'O produto que custava R${x:.2f}, agora com desconto de 5%, vai custar R${novox:.2f}')
