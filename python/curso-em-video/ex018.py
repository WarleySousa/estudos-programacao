import math
angulo = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(angulo))
co = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O angulo digitado foi {}. \nO seno do valor digitado é {:.2f}. \nO cosseno é {:.2f}. \nO tagente é {:.2f}.'.format(angulo, seno, co, tan))