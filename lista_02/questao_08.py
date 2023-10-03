# Faça um algoritmo para ler: quantidade atual em
# estoque, quantidade máxima em estoque e quantidade
# mínima em estoque de um produto. Calcular e escrever
# a quantidade média
# ((quantidade média = quantidade máxima + quantidade mínima)/2).
# Se a quantidade em estoque for maior ou igual a
# quantidade média, escrever a mensagem 'Não efetuar compra',
# senão escrever a mensagem 'Efetuar compra'.

# declaracao de variaveis
# refill_stock vai receber a resposta final
# avg_stock vai receber a quantidade media em estoque do produto
refill_stock = None
avg_stock = None

# input
current_stock = int(input('Digite a quantidade atual em estoque: '))
max_stock = int(input('Digite a quantidade maxima em estoque: '))
min_stock = int(input('Digite a quantidade minima em estoque: '))

# processamento
avg_stock = (max_stock + min_stock)/2
if current_stock < avg_stock:
    refill_stock = 'Efetuar compra'
else:
    refill_stock = 'Nao efetuar compra'

# output
print(f'Quantidade media de estoque: {avg_stock}. {refill_stock}.')
