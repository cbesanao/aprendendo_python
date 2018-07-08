print('#####################################')
print("Seja um Militar, confira se você está apto!\n")

idade = input('Digite sua idade: ')
peso = input("Digite seu peso: ")
altura = input("Digite sua altura: ")

if int(idade) >= 18 and float(peso) >= 60 and float(altura) >= 1.70:
    print("\nParabéns! Você tem os requisitos para ser um Militar")
else:
    print('\nInfelizmente você não tem algum dos requisitos!')
