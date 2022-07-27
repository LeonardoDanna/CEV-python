print('---- lojas leoroq ----')

preco = float(input('Preço das compras: R$'))

opcao = int(input('FORMAS DE PAGAMENTO\n'
              '[ 1 ] à vista dinheiro/cheque\n'
              '[ 2 ] à vista cartão\n'
              '[ 3 ] 2x no cartão\n'
              '[ 4 ] 3x ou mais no cartão\n'
              'Qual a opção? '))

if opcao == 1:
    print(f'Você recebeu um desconto de 10%!')
    print(f'Sua compra de R${preco} vai custar R${preco - ((preco / 100) * 10)}')

elif opcao == 2:
    print(f'Você recebeu um desconto de 5%!')
    print(f'Sua compra de R${preco} vai custar R${preco - ((preco / 100) * 5)}')

elif opcao == 3:
    print(f'Sua compra será parcelada em 2x de R${preco / 2} SEM JUROS.')

elif opcao == 4:
    z = int(input('Quantas parcelas? (até 12x) '))

    if z <= 12:
        print(f'Sua compra será parcelada em {z}x de {(preco + (preco * 20 / 100)) / z} COM JUROS.')
        print(f'Sua compra de {preco} vai custar {preco + (preco * 20 / 100)}')

    else:
        print('Não será possível parcelar mais do que 12x.')

else:
    print('Opção não existente')
