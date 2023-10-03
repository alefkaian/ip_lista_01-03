# Faça um programa que receba um número e que
# calcule e mostre a tabuada desse número.

# input
numero_tabuada = int(input('Digite um numero (inteiro): '))

# output
print(f'\nTabuada do {numero_tabuada}')
for fator in range(1,11):
    print(f'{numero_tabuada} x {fator} = {numero_tabuada*fator}')
