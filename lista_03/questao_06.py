# Seja criativo ao desenvolver este programa.
# a. Crie uma lista de convidados para um jantar em sua casa, com pelo menos
# 5 celebridades.
# b. Envie um convite para cada uma dessas pessoas. Com a mesma mensagem
# e nome personalizado.
# c. Sabendo que uma dessas pessoas nao podera ir ao seu jantar, voce devera
# enviar novos convites. Imprima o nome das pessoas que nao poderao comparecer.
# d. Modifique sua lista, substitua os desistentes por novos convidados.
# e. Exiba um novo convite para cada pessoa que continua presente em sua lista.

# declaracao de variaveis
celebrities_list = ['Scarlett Johansson', 'Tom Holland', 'Whindersson Nunes', 'Anitta', 'Wagner Moura']

# primeira parte: convites
# funcao para printar o texto pra todo mundo
def invite(name):
    print(f'\nOla, {name}. Voce foi convidado para um jantar particular.')
    print('Algumas celebridades estarao presentes, mas o clima sera descontraido.')
    print('O prato principal sera comida italiana acompanhado de vinho tinto.')
    print('Caso voce seja vegano, me enviar uma mensagem para eu preparar uma refeicao a parte.')
    print('O local sera na minha casa e o horario sera as 20h. Conto com sua presenca.\n')

# manda o convite para todos da lista
for celebrity_name in celebrities_list:
    invite(celebrity_name)

# Whindersson e Anitta nao poderao ir
# pop remove eles da lista
# repete o 2 duas vezes porque o 3 vira o 2 depois do primeiro pop
print(f'\n\n\n{celebrities_list[2]} e {celebrities_list[3]} nao poderao comparecer.')
celebrities_list.pop(2)
celebrities_list.pop(2)

# Chamei Beyonce e Jay-Z
celebrities_list.append('Beyonce')
celebrities_list.append('Jay-Z')

# printa a lista de novo
print('\n\n\n\n\n\n\nNova lista:')

for celebrity_name in celebrities_list:
    invite(celebrity_name)

print(len(celebrities_list))
