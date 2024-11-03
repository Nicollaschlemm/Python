#Escreva um programa que mostre na tela a tabuada do número inteiro N que deve ser lido do teclado.
cont = 1
num = int(input("Digite o numero da tabuada que gostaria: "))
while cont <= 10:
    Resultado = cont * num
    print(f"{cont} x {num} = {Resultado}")
    cont += 1

