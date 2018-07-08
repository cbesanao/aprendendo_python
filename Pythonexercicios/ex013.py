nome = " DESAFIO 013 "
print('{:=^40}\n'.format(nome))

print('OOOOba!!! Você foi bem visto na empresa e terá um aumento de 15% no salário')
s = float(input('Quanto você recebe hoje: '))
print('Parabéns! Você recebia R${:.2f}, a partir desse mês você receberá {:.2f}'.format(s, s + (s/100) * 15))
