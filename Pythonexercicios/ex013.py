nome = " DESAFIO 013 "
print('{:=^40}\n'.format(nome))

print('OOOOba!!! Você foi bem visto na empresa e terá um aumento de 15% no salário')
salario = float(input('Quanto você recebe hoje: R$ '))
novo = salario + (salario/100) * 15
print('Parabéns! Você recebia R${:.2f}, a partir desse mês você receberá {:.2f}'.format(salario, novo))
