a = input('Digite algo: ')
print('O tipo primitivo desse vale {}'.format(type(a)))
print('Só tem espaços? {}' .format(a.isspace()))
print('É um número? {}' .format(a.isnumeric()))
print('É uma letra do alfabeto? {}' .format(a.isalpha()))
print('É uma letra minúscula? {}' .format(a.islower()))
print('É um numero com letras? {}' .format(a.isalnum()))
print('Está em maiuscula? {}' .format(a.isupper()))

