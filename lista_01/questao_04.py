# Crie um programa em Python que imprima um convite
# para uma festa como nome do usuário que for digitado.
# O nome do usuário precisará ser apresentado todo
# em caixa alta.

# input
# username recebe o nome do usuario
username = input('Digite seu nome: ')

# processamento
# transforma todas as letras em caps
username = username.upper()

# output
# mensagem de convite
print('\n---------------------------------------------------------')
print(f'\nSaudacoes, {username}. Voce foi convidado para minha festa.')
print('A comida e por minha conta, a bebida cada um leva a sua.')
print('\nLocal: Minha Casa')
print('Horario: A partir das 21:00')
print('\nTe aguardo la.')
print('\n---------------------------------------------------------')
