nome = " DESAFIO 012 "
print('{:=^40}\n'.format(nome))

print('Hoje é dia de liquidação! Tudo com 5% de Desconto!!!')

preço = float(input('Digite o valor do seu produto e veja quanto custará com o desconto: R$ '))

novo_preço = preço - (preço/100)*5

print('Seu produto normalmente custaria R$ {:.2f}, mas hoje ele vai custar R$ {:.2f}'.format(preço, novo_preço))
