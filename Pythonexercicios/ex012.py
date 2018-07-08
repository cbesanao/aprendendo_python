nome = " DESAFIO 012 "
print('{:=^40}\n'.format(nome))

print('Hoje é dia de liquidação! Tudo com 5% de Desconto!!!')
p = float(input('Digite o valor do seu produto e veja quanto custará com o desconto: '))
print('Seu produto normalmente custaria {:.2f}, mas hoje ele vai custar {:.2f}'.format(p, p-(p/100)*5))
