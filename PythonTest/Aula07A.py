nome = input('Qual seu nome? ')
print('Prazer em te conhecer, {:20}!'.format(nome))
print('Prazer em te conhecer, {:_<20}!'.format(nome))
print('Prazer em te conhecer, {:->20}!'.format(nome))
print('{:^20}, {:^20}!'.format('Prazer em te conhecer', nome))

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
print(f'A soma vale {n1 + n2}, \nO produto vale {n1 * n2} \nE a divisão vale {n1 / n2:.3f}, ', end='')
print(f'A divisão inteira vale {n1 // n2}, o resto vale {n1 % n2} e a potência vale {n1 ** n2}')

# Exercícios: 5 - 15
