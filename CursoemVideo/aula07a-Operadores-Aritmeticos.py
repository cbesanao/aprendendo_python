# 1 ()
# 2 **
# 3 *  /  //  %
# 4 +  -
'''
nome = input("Qual é o seu nome? ")
print('Prazer em te conhecer {:20}!\n'.format(nome))     # agora a parte do nome terá 20 espaços
print('Prazer em te conhecer {:>20}!\n'.format(nome))    # agora a parte do nome terá 20 espaços e será alinhado à DIREITA
print('Prazer em te conhecer {:<20}!\n'.format(nome))    # agora a parte do nome terá 20 espaços e será alinhado à ESQUERDA
print('Prazer em te conhecer {:^20}!\n'.format(nome))    # agora a parte do nome terá 20 espaços e será CENTRALIZADO
print('Prazer em te conhecer {:=^20}!\n'.format(nome))   # agora a parte do nome terá 20 espaços e será CENTRALIZADO entre "
'''

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, a multiplicação é {} e a divisão {:.3f}'.format(s, m, d), end=' ')
print('A divisão inteira é {} e a potência é {}'.format(di, e))

# para quebrar a linha ou um enter, digita \n
# para juntar as linha ou dois prints digita , end=' '