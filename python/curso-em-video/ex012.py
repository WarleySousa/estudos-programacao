largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura*altura
tinta = area/2
print('A largura da parede é {}m, a altura é {}m, a área é {}m², e a quantidade de tinta necessária para pintar a parede é {}L!' .format(largura, altura, area, tinta)) 