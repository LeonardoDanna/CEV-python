from datetime import date
x = int(input('Que ano quer analisar? Coloque 0 para analizar o ano atual: '))
if x == 0:
    x = date.today().year
if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
    # se o ano não terminar em 00 e for divisível por 4 dizemos que ele é bissexto
    print(f'O ano {x} é bissexto')
else:
    print(f'O ano {x} não é bissexto')
