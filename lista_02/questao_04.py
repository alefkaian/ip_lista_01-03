# Ler as notas da 1a. e 2a. avaliações de um
# aluno. Calcular a média aritmética simples
# e escrever uma mensagem que diga se o aluno foi
# ou não aprovado (considerar que nota igual ou
# maior que 6 o aluno é aprovado). Escrever também
# a média calculada.

# declaracao de variaveis
# result vai receber a resposta final
# avg vai receber a media calculada do aluno
result = None
avg = None

# input
# notas do aluno
test_result_01 = float(input('Digite a primeira nota: '))
test_result_02 = float(input('Digite a segunda nota: '))

# processamento
# result vai receber a string de acordo com a comparacao da media com 6
avg = (test_result_01 + test_result_02)/2
if avg < 6:
    result = 'reprovado'
else:
    result = 'aprovado'

# output
# fstring pra concatenar
print(f'Aluno {result}. Media: {avg}.')
