a = input('Digite alguma coisa aí: ')
print("O tipo primitivo desse valor é:", type(a))
print("Só tem espaços?", a.isspace())
print("É um número?", a.isnumeric())
print("É alfabético?", a.isalpha())
print("É alfanumérico?", a.isalnum())
print("Está tudo em maiúscula?", a.isupper())
print("Está tudo em minúscula?", a.islower())


"""
valor1 = a.isalpha()
print(a, 'é/são letras?')
if valor1 == True:
    print('Sim')
else:
    print('Não')

valor2 = a.isnumeric()
print(a, 'é/são números?')
if valor2 == True:
    print('Sim')
else:
    print('Não')

valor3 = a.isalnum()
print(a, 'é/são letras e números?')
if valor3 == True:
    print('Sim')
else:
    print("Não")
"""
