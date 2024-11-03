#Escreva um programa que permaneça em laço enquanto um valor X lido for diferente de zero. Para 
#cada valor de X apresente na tela se é par ou ímpar.
x=1
while x != 0: 
    x = int(input("Difgite 1 numero: "))

    if x % 2 == 0:
        print(f"O numero {x} e par")
    else:
        print(f"O numero {x} e impar")
