preço = float(input('Digite o preço do produto: R$'))
desconto = preço*0.05
preço_final = preço-desconto            
print('Se o preço do produto é R${:.2f}, com o desconto de 5% o preço final é R${:.2f}!' .format(preço, preço_final))