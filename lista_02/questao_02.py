# Solicite ao usuário um valor numérico, inteiro
# ou real, e escrever se é positivo ou negativo
# (considere o valor zero como positivo).

# declaracao de variaveis
# answer vai receber a resposta final
answer = None

# input
input_number = float(input('Digite um numero: '))

# processamento
# modifica a string de acordo com a comparacao do numero com 0
if input_number >= 0:
    answer = 'positivo'
else:
    answer = 'negativo'

# output
# fstring pra concatenar a frase com a resposta
print(f'O numero digitado e {answer}.')
