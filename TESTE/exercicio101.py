print('\033[1;32m Exercício Data de votação com função')
ano = int(input('Qual o ano em que você nasceu?: '))
from datetime import date
idade = 0


def votacao(ano):
    idade = date.today().year - ano
    if idade < 18:
        return f'Com {idade} você ainda não pode votar!'
    elif 18 <= idade <= 24:
       return f'Com {idade} seu voto é FACULTATIVO'
    elif 24 < idade < 70:
       return f'Com {idade} seu voto é obrigatório!'
    else:
        return f'Com {idade} seu voto é mais uma vez facultativo'

print(votacao(ano))
