# Faça um algoritmo para ler: número da conta do cliente,
# saldo, débito e crédito. Após, calcular e escrever o
# saldo atual (saldo atual = saldo - débito + crédito). Também
# testar se saldo atual for maior ou igual a zero escrever
# a mensagem 'Saldo Positivo', senão escrever a mensagem
# 'Saldo Negativo'.

# declaracao de variaveis
# current_balance vai receber o valor calculado do Saldo
# account_balance_status vai receber a string com o status da conta
current_balance = None
account_balance_status = None

# input
account_id = input('Numero da conta: ')
old_balance = float(input('Saldo: '))
credit = float(input('Credito: '))
debt = float(input('Debito: '))

# processamento
# account_balance_status vai receber o status da conta de acordo
# com a comparacao do saldo atual com 0
current_balance = old_balance + credit - debt
if current_balance < 0:
    account_balance_status = 'negativo'
else:
    account_balance_status = 'positivo'

# output
# mostra o saldo atual e o status da divida
print(f'Saldo atual: {current_balance}. Saldo {account_balance_status}.')
