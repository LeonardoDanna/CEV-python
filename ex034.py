x = float(input('Qual o salário do funcionário? R$'))

if x <= 1250:
    print(f'Quem ganhava R${x} passa a ganhar R${x/100 * 15 + x} agora')
if x > 1250:
    print(f'Quem ganhava R${x} passa a ganhar R${x/100 * 10 + x} agora')