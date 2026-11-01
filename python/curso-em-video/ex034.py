salario = float(input("Digite o salário do funcionário: "))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f'O salário do funcionário com o aumento será de R${novo:.2f}.')