# Faça um programa que mostre as tabuadas dos números de 1 a 10.

# primeiro for cada numero da tabuada
# segundo for cada fator da tabuada
for numero_tabuada in range(1,11):
    print(f'\nTabuada do {numero_tabuada}')
    for fator in range(1,11):
        print(f'{numero_tabuada} x {fator} = {numero_tabuada*fator}')
