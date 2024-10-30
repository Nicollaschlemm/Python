#Escreva um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar. Lembrando
#que para saber a paridade de um inteiro é preciso calcular o resto da sua divisão por 2. Se o resto for
#0 o número é par, se o resto for 1 o número é ímpar

#Recebe o numero
num = int(input("Digite um numero: "))

#Faz a divisão e salva o resustado do resto
resto = num % 2

#valida se o o resto da divisão é 1 ou 0
if resto == 0:
    print(f"O numero {num} e par")
elif resto == 1:
    print(f"O numero {num} e impar")
else:
    print("Numero Invalido")