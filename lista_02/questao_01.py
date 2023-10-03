# Solicite ao usuário um valor numérico, inteiro
# ou real, e verifique se ele é maior ou menor
# que 10. O programa deve escrever a mensagem
# correspondente (maior ou menor) e informar o valor
# digitado pelo usuário.

# declaracao de variaveis
# answer vai receber a resposta final
answer = None

# input
# input_number recebe um numero qualquer
input_number = float(input('Digite um numero: '))

# processamento
# modifica a string de acordo com o valor do numero comparado com 10
if input_number > 10:
    answer = 'maior que'
elif input_number == 10:
    answer = 'igual a'
else:
    answer = 'menor que'

# output
# fstring pra concatenar a frase com o numero e a resposta
print(f'O numero digitado ({input_number}) e {answer} 10.')
