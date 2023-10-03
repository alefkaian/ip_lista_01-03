# Ler dois valores (considere que não serão
# lidos valores iguais) e escrever o maior
# deles.

# declaracao de variaveis
# higher_value vai receber o maior valor
higher_value = None

# input
first_number = float(input('Digite o primeiro valor: '))
second_number = float(input('Digite o segundo valor: '))

# processamento
# a funcao max retorna o maior valor dentre os argumentos
higher_value = max(first_number, second_number)

# output
print(f'Maior valor: {higher_value}')
