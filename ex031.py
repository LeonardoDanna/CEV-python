x = float(input('Qual a distância da viagem? '))
print(f'Você está prestes a começar uma viagem de {x}km')
#preço = x * 0.50 if x <= 200 else x * 0.45
if x < 200:
    print(f'E o preço da sua passagem será de R${x*0.5:.2f}')
if x > 200:
    print(f'E o preço da sua passagem será de R${x*0.45:.2f}')