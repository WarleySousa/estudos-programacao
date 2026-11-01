from time import sleep

distancia = float(input("Digite a distância da sua viagem?: "))
print('CALCULANDO DISTÂNCIA...')
sleep(3)
print(f'Você está prestes a começar uma viagem de {distancia}Km.')
if distancia <= 200:
    preço = distancia * 0.50
    print(f'O preço da sua passagem será de R${preço:.2f}')
else:
    preço = distancia * 0.45
    print(f'O preço da sua passagem será de R${preço:.2f}')