#Escreva um programa que leia dois inteiros e mostre na tela apenas o menor dos dois. Se ambos
#forem iguais, mostre qualquer um deles.
 
num = input("Escreva 1 numero interiro: ")
num2 = input("Escreva 1 numero inteiro: ")

if num < num2:
    print(f"O numero {num} é o menor")
elif num2 < num:
    print(f"O numero {num2} é o menor")
else:
    print(f"O menor numero é {num}")