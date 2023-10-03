# Crie um programa em Python que solicite um número do
# usuário, depois some este número com 1357, multiplique
# por 8, divida por 5 e eleve ao quadrado.

# input
# original_number recebe o valor que vai ser usado nos calculos
original_number = int(input('Digite um numero (inteiro!): '))

# processamento
output_number = ((original_number + 1357)*8)**2;

# output
# fstring concatena mais limpo
print(f'(({original_number} + 1357)*8)^2 = {output_number}')
