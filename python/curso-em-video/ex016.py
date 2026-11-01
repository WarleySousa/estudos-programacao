dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos Km rodados? Km'))
precopordia = (dias * 60) + (km * 0.15)
print ('O total a pagar é de R${:.2f}, '.format(precopordia))