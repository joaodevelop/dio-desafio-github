print('Exercício 29: Programa que leia a velocidade do carro e aplique multa por cada KM além')
vel = float(input('Qual a velocidade do veículo?: '))
print(f'A velocidade foi de {vel}km/h')
if vel >= 80.0:
    print(f'A velocidade está acima do limite. Com isso será aplicada multa de {(vel-80)*7:.2f}')
else:
    print('Velocidade abaixo do limite!')
