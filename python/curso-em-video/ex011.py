real = float(input('Digite o valor em reais: R$'))
dolar = real/5.04
euro = real/5.86
cad = real/3.64
print('O valor digitado foi R${:.3f} \nSua conversão para dólares é US${:.3f} \nEm euro será de €{:.3f} \nEm Dólar canadense você consiguirá comprar C${:.3f}! \n\n A vida não é fácil, bora trabalhar! ' .format(real, dolar, euro, cad))