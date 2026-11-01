n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1+n2)/2
print('A sua média foi {:.1f}'.format(média))
if média >= 7:
    print('Você conseguiu. Aprovado!')
else:
    print('Tente novamente. Reprovado!')
