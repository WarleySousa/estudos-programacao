salário = float(input('Digite o salário do funcionário: R$'))
aumento = salário*0.15
salário_final = salário + aumento
print('O salário do funcionário é R${:.2f}, com o aumento de 15% R${:.2f} o salário final será de R${:.2f}!' .format(salário, aumento, salário_final))
