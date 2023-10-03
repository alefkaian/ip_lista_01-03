# Faça um cadastro de usuários com nome, idade e
# email, utilizando apenas o que você aprendeu
# até agora.

# ALERTA: NAO COLOQUEI TRY EXCEPT, ENTAO NAO ESCOLHA UM VALOR DE USUARIO
# QUE NAO ESTA CADASTRADO


# declaracao de variaveis
# exit eh a variavel auxiliar para sair do loop do programa
# users eh a lista de usuarios
exit = 0
users = []

# declaracao de funcoes e classes

# classe para os usuarios
# init: metodo de inicializacao
# __init__: metodo chamado quando o objeto eh chamado como string
class UserData:

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __str__(self):
        return f'\nNome: {self.name}\nIdade: {self.age}\nE-mail: {self.email}'

# funcao para registro dos usuarios
# append: adiciona ao fim da lista um objeto novo com as informacoes dadas
def register():
# debug    print('0')
    n = input('Digite o nome: ')
    a = input('Digite a idade: ')
    e = input('Digite o e-mail: ')

    users.append(UserData(n, a, e))

# funcao para mostrar a lista de usuarios cadastrados
# index: retorna o indice da lista correspondente ao argumento
def show_list_of_users():
    print('\nLISTA DE USUARIOS CADASTRADOS')
    for user in users:
        print(f'{users.index(user)}- {user.name}')

# funcao para mostrar os dados de um usuario especifico
# o if nao deixa o usuario preso no input se nao tiver ninguem cadastrado
def visualize():
# debug    print('1')
    if len(users) == 0:
        print('\nNenhum usuario cadastrado!')
    else:
        show_list_of_users()
        user_index = int(input('\nEscolha um numero para visualizar os dados: '))
        print(users[user_index])

# funcao para remover um usuario
# o if nao deixa o usuario preso no input se nao tiver ninguem cadastrado
# pop: remove o valor da lista na posicao do argumento
def remove():
# debug    print('2')
    if len(users) == 0:
        print('\nNenhum usuario cadastrado!')
    else:
        show_list_of_users()
        user_index = int(input('\nEscolha um numero para remover o usuario: '))
        users.pop(user_index)

# loop
while exit == 0:
    # input
    print('\nMENU')
    print('0- Cadastrar usuario')
    print('1- Visualizar informacoes dos usuarios')
    print('2- Remover usuario')
    print('3- Sair')
    menu_input = input('\nEscolha uma opcao (numero): ')

    # selecionar opcao (default: volta pro menu)
    if menu_input == '0':
        register()
    elif menu_input == '1':
        visualize()
    elif menu_input == '2':
        remove()
    elif menu_input == '3':
# debug        print('3')
        exit = 1
