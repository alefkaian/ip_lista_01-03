# As maçãs custam 1,30 cada se forem compradas
# menos de uma dúzia e e 1,00 seforem compradas
# pelo menos 12. Escreva um programa que leia
# o número de maçãs compradas, calcule e escreva
# o custo total da compra.

# declaracao de variaveis
# unitary_price eh o valor de cada maca
# checkout vai ser o valor a ser pago
unitary_price = 1.3
checkout = 9999999999999999999

# input
# apple_quantity vai receber o numero comprado de macas
apple_quantity = int(input('Digite o numero de macas: '))

# processamento
# ha um desconto se forem compradas 12 ou mais macas
# como o valor default de unitary_price eh 1.30, o
# else pode ser omitido aqui
if apple_quantity >= 12:
    unitary_price = 1

checkout = apple_quantity*unitary_price

# output
# concatena o numero de macas e o valor a ser pago com fstring
print(f'Preco total pelas {apple_quantity} macas: {checkout} reais.')
