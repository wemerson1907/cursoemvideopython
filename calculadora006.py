n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
s = n1 + n2

#print('A soma entre', n1, ' e ', n2, 'é igual a', s) // metodo convencional

#usando o .format
print('A soma entre {} e {} é igual a {}'.format(n1, n2, s))


