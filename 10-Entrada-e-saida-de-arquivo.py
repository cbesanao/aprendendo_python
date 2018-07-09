
print("#"*40)
print(' Programa de controle de convidados 1.0')
print("#"*40)
festa_do = input("\n\o/ De quem será a festa: ")


try:
    quantidade = int(input("Quantos serão convidados: "))
except ValueError:
    print("Você não digitou um NUMERO INTEIRO de convidados")
    quantidade = int(input("Quantos serão convidados: "))

lista_de_convidados = set()

i = 1

while len(lista_de_convidados) <= quantidade-1:
    convidado = input("Convidado(a)#"+str(i)+":")
    lista_de_convidados.add(convidado)
    i += 1

print("\nA festa do(a)", festa_do, 'terá', quantidade, 'convidados.\nSão eles:\n')

for x in lista_de_convidados:
    print(x+";")

try:
    arquivo = open(festa_do + '.doc', 'r+')
    texto = arquivo.readlines()
    arquivo = open(festa_do + ".doc", 'w+')
    texto.append(lista_de_convidados)
    arquivo.writelines(str(texto))

except FileNotFoundError:
    arquivo = open(festa_do+".doc", 'w+')
    arquivo.writelines("\n"+str(lista_de_convidados))
arquivo.close()



"""
arquivo = open(festa_do+'.txt', 'r+')
l1 = arquivo.readline()

conteudo.append(str(lista_de_convidados))
arquivo = open(festa_do+'.txt', 'w')
for item in conteudo:
    arquivo.writelines("\n"+str(item))
arquivo.close()
"""


'''
arquivo = open(festa_do+'.doc', 'w')
arquivo.write("A festa do(a) ")
arquivo.write(festa_do)
arquivo.write(' terá ')
arquivo.write(str(quantidade))
arquivo.write(' convidados.\nSao eles:')
arquivo.write('\n'+str(lista_de_convidados))
'''