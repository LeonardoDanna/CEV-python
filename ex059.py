opcao = 0
while opcao != 5:
    x1 = int(input('Primeiro valor: '))
    x2 = int(input('Segundo valor: '))
    opcao = int(input('[ 1 ] somar\n'
                      '[ 2 ] multiplicar\n'
                      '[ 3 ] maior\n'
                      '[ 4 ] novos números\n'
                      '[ 5 ] sair do programa\n'
                      '> Qual é a sua opção? '))
    if opcao == 1:
        print(f'A soma entre {x1} e {x2} é igual a {x1+x2}')
    elif opcao == 2:
        print(f'A multiplicação entre {x1} e {x2} é igual a {x1 * x2}')
    elif opcao == 3:
        MaiorX = 0
        if x1 > x2:
            MaiorX = x1
        else:
            MaiorX = x2
        print(f'O maior número entre {x1} e {x2} é o {MaiorX}')
    elif opcao == 4:
        pass
    elif opcao == 5:
        print('Obrigado por utilizar o programa!')
        opcao = 5
    else:
        print('Opção inválida. Tente novamente')
