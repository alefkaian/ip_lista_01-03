# Faça um programa que lê as duas notas parciais
# obtidas por um aluno numa disciplina ao longo
# de um semestre, e calcule a sua média. A atribuição
# de conceitos obedece à tabela abaixo:
#
# Média de Aproveitamento Conceito
# Entre 9.0 e 10.0           A
# Entre 7.5 e 9.0            B
# Entre 6.0 e 7.5            C
# Entre 4.0 e 6.0            D
# Entre 4.0 e zero           E
#
# O algoritmo deve mostrar na tela: as notas, a média,
# o conceito correspondente e a mensagem “APROVADO”
# se o conceito for A, B ou C ou “REPROVADO” se o
# conceito for D ou E.

# declaracao de variaveis
# avg vai receber a media calculada
# tier vai receber o conceito
# pass_status vai receber a mensagem de aprovado/reprovado
avg = None
tier = None
pass_status = None

# input
test_result_01 = float(input('Digite a primeira nota: '))
test_result_02 = float(input('Digite a segunda nota: '))

# processamento
# a logica condicional so funciona se a nota estiver entre 0 e 10
avg = (test_result_01 + test_result_02)/2
if avg < 4:
    tier = 'E'
    pass_status = 'REPROVADO'
elif avg < 6:
    tier = 'D'
    pass_status = 'REPROVADO'
elif avg < 7.5:
    tier = 'C'
    pass_status = 'APROVADO'
elif avg < 9:
    tier = 'B'
    pass_status = 'APROVADO'
else:
    tier = 'A'
    pass_status = 'APROVADO'

# output
print(f'Notas: {test_result_01} e {test_result_02}')
print(f'Media: {avg}')
print(f'Conceito: {tier}')
print(pass_status)
