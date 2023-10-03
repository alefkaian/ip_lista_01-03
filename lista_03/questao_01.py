# Desenvolva um programa que verifique e mostre os números
# entre 1.000 e 2.000 que, quando divididos por 11,
# produzam o resto igual a 5.

# declaracao de variaveis
# numbers_output eh uma lista que vai receber os numeros
# que atendem o criterio
numbers_output = []

# processamento
# o metodo append adiciona o argumento ao final da lista
for number in range(1000,2001):
    if number%11 == 5:
        numbers_output.append(number)

# output
# printa todos os valores da lista
for number in numbers_output:
    print(number)
