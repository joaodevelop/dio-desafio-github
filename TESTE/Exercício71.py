print('\033[1;32mExercício 71 - Caixa eletrônico')
valor = int(input('Qual valor você quer sacar: '))
notas = valor//50
if notas >1:
    print(f'Você receberá {notas} cédulas de R$50,00')
notas = valor%50
while notas != 0:
    if notas >=20:
        print(f'Você receberá {notas//20} cédulas de R$20,00')
    notas = notas%20
    if 20>notas>1:
        print(f'Você receberá {notas//1} cédulas de R$1,00')
    notas = notas%1

