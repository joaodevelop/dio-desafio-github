print('\033[1;32mExercício 68 Par ou ímpar eterno')
cont = 0
from random import randrange
while True:
    parim = int(input('Escolha 1 para Par ou 2 para Ímpar: '))
    esc = int(input('Escolha seu número para o Par ou Ímpar: '))
    computador = randrange(0,9)
    print(f'Você escolheu {esc} e o computador escolheu {computador}. {esc} + {computador} = {esc+computador}.')
    if (esc+computador)%2==0 and parim == 1:
        print(f'Parabéns {esc+computador} é par, você ganhou!')
        cont+=1
    elif (esc+computador)%2!=0 and parim == 2:
        print(f'Parabéns {esc + computador} é Ímpar, você ganhou!')
        cont += 1
    elif (esc+computador)%2!=0 and parim == 1:
        print(f'Você perdeu. {esc+computador} é Ímpar.')
        break
    else:
        print(f'Você perdeu. {esc+computador} é Par')
print(f'Você conseguiu ganhar um total de {cont} vezes.')