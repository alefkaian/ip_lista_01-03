# Ler dois valores (considere que não serão lidos
# valores iguais) e escrevê-los em ordem crescente.

# declaracao de variaveis
# numbers_list eh uma lista que vai receber os numeros
numbers_list = []

# input
first_number = float(input('Digite o primeiro valor: '))
second_number = float(input('Digite o segundo valor: '))

# processamento
# o metodo sort ordena uma lista de forma crescente
numbers_list = [first_number, second_number]
numbers_list.sort()

# output
# printa os numero na ordem da lista
for value in numbers_list:
    print(value)
