nome = " DESAFIO 008 "
print('{:=^40}\n'.format(nome))

print('Você sabe converter metros em centímetros e milímetros?\n')
m = int(input('Coloque sua distância em metros: '))

km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000

print("A medida de {}m corresponde à:".format(m))
print('São {} km'.format(km))
print('São {} hm'.format(hm))
print('São {} dam'.format(dam))
print('São {} dm'.format(dm))
print('São {} cm'.format(cm))
print('São {} mm'.format(mm))
