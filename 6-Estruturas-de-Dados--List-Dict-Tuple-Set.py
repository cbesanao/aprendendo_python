'''
minha_lista = ["Moises", "Kedma"]       # LISTA ou list, eh mutavel
Minha_tupla = ("Fernando", "Helena")    # TUPLA ou tuple, nao eh mutavel, nao tem append ou remove
meu_dicionario = {'nome': 'Alice', 'idade':3} #DICIONARIO ou dict, chave e valor, posso mod itens (V/C)
meu_conjunto = {"Guilherme", "Davi"}    # CONJUNTO ou set, eh mutavel, porem, nao repete objetos/nomes, nao tem indice
                                          para criar um conjunto vazio eh conjunto = set()
'''




'''
# para criar uma lista eh lista = []
minha_lista = ["Moises", "Kedma"]

nome = input("Descubra se seu nome esta na lista\nDigite seu nome: ")

if nome in minha_lista:
    print("Parabens, Voce esta na lista!!!!")
else:
    print("Infelizmente seu nome nao esta na lista!")
'''




'''
#para criar uma dicionario eh dicionario = dic{}
nome = input("\nDescubra se seu nome esta no dicionario\nDigite seu nome: ")
meu_dicionario = {'nome': 'Alice', 'idade':3}

print(nome)

if nome in meu_dicionario.values():
    print("Esta no dicionario")
else:
    print('Voce nao esta no dicionario!')

chave = input('Adicione uma chave no dicionario: ')
valor = input("Agora adicione um valor: ")

meu_dicionario[chave] = valor

print(meu_dicionario)
'''





# Para criar um cinjunto eh conjunto = set()
nome = input("\nDescubra se seu nome esta no conjunto\nDigite seu nome: ")
meu_conjunto = {"Guilherme", "Davi"}

if nome in meu_conjunto:
    print(nome+"\nSeu nome esta no conjunto!!!")
else:
    print(nome+"\nSeu nome nao esta no conjunto!")





