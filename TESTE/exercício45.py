print('\033[1;32mExercício 45: JOKENPO')
print('='*25)
print('Escolha entre Pedra, Papel ou Tesoura! Tesoura ganha de Papel, Papel ganha de Pedra e Pedra ganha de Tesoura')
while True:
    escolha = str(input('Pedra Papel Tesoura: ').title())
    lista = ['Pedra', 'Papel', 'Tesoura']
    print('JO')
    from time import sleep
    sleep(1)
    print('Ken')
    sleep(1)
    print('Po')
    from random import choice
    pc = choice(lista)
    print('='*50)
    if escolha == 'Pedra':
        if pc == lista[1]:
            print(f'Voce escolheu {escolha} e o computador escolheu {pc}. Papel come Pedra. Você perdeu')
        elif pc == lista[2]:
            print(f'Você escolheu {escolha} e o computador escolheu {pc}. Pedra quebra Tesoura. Você ganhou!')
        elif pc == lista[0]:
            print(f'Você escolheu {escolha} e computador também escolheu {pc}. Empate!')
    if escolha == 'Papel':
        if pc == lista[0]:
            print(f'Você escolheu {escolha} e o computador escolheu {pc}. Papel come pedra. Você ganhou!')
        elif pc == lista[1]:
            print(f'Você escolheu {escolha} e o computador escolheu {pc}. Empate!')
        elif pc == lista[2]:
            print(f'Você escolheu {escolha} e o computador escolheu {pc}. Tesoura corta papel. Você perdeu')
    if escolha == 'Tesoura':
        if pc == lista[0]:
            print(f'Você escolheu {escolha} e o computador escolheu {pc}. Pedra quebra tesoura. Você perdeu')
        elif pc == lista[1]:
            print(f'Você escolheu {escolha} e o computador escolheu {pc}. Tesoura corta papel. Você ganhou')
        elif pc == lista[2]:
            print(f'Você escolheu {escolha} e o computador também escolheu {pc}. Empate!')
    print('='*50)
    mais  = str(input(('Vamos de novo? (S/N): ')).upper())
    if mais == "N":
        break
