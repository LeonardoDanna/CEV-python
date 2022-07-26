x = int(input('Qual a velocidade atual do carro? '))

multa = 7 * (x-80)

if x > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h ')
    print(f'Você deve pagar uma multa de R${multa:.2f}.')

print('Tenha um bom dia! Dirija com segurança')
