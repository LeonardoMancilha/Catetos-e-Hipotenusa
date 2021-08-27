triangulo = float(input('Digite o valor do cateto oposto: '))
cateto = float(input('Digite o valor do cateto adjacente: '))
soma = (triangulo ** 2 + cateto ** 2) ** (1/2)
print('O comprimento da hipotenusa é {:.2f}'.format(soma))