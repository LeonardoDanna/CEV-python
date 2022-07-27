from datetime import date

x = str(input('Você se identifica como parte do gênero MASCULINO [M] ou FEMININO? [F] '))
if x == "M":
    nasc = int(input('Ano de nascimento: '))
    atual = date.today().year
    idade = atual - nasc
    alistamento = nasc + 18

    print(f'Quem nasceu em {nasc} tem {atual - nasc} anos em 2022.')
    if idade > 18:
        print(f'Você já deveria ter se alistado há {atual - alistamento} anos.')
        print(f'Seu alistamento foi em {alistamento}.')
    if idade < 18:
        print(f'Ainda faltam {alistamento - atual} anos para o alistamento.')
        print(f'Seu alistamento será em {alistamento}.')
    if idade == 18:
        print('Você deve se alistar imediatamente.')
if x == "F":
    print('Você não tem a obrigação de se alistar.')
