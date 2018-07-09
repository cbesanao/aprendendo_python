nome = " DESAFIO 011 "
print('{:=^40}\n'.format(nome))

lar = float(input('Qual é a largura da sua parede: '))
alt = float(input('Qual a altura da sua parede: '))

area = lar * alt
tinta = area / 2

print('Sua parede mede {} m por {} m e tem uma área de {}m².'.format(lar, alt, area))
print('Para pintar sua parede, você vai precisar de {} litros de tinta.'.format(tinta))
