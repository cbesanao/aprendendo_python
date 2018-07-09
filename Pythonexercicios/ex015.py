nome = " DESAFIO 015 "
print('{:=^40}\n'.format(nome))

dias = float(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos Km rodados? '))

v1 = dias * 60
v2 = km * 0.15

print('O total à pagar é R$ {:.2f} reais'.format(v1 + v2))
