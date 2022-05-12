# faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informaçoes possiveis sobre ele

# Metodos " .is"

# .isnumeric()  - verifica se é um numero
# .isalpha() - verifica se é letra
# .isalnum() - verifica se é alfanumerico
# .isupper()- verifica se esta tudo em maiusculo
# islower() - verifica se ta tudo minusculo


# _________________ Resposta________________________


n = input('Digite algo: ')
print('o tipo primitivo é ', type(n))
print('É um numero?', n.isnumeric())
print('É Alphanumerico?', n.isalnum())
print('É uma letra?', n.isalpha())
print('Esta escrito tudo maiusculo?', n.isupper())
print('Esta escrito tudo minusculo?', n.islower())
