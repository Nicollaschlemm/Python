#Escreva um programa para exibir na tela o nome e a categoria de um lutador. O programa deve ler
#um string para o nome e um número real para o peso. Conforme o peso ocorrerá o enquadramento
#na categoria, segundo esta tabela (fictícia):

nome = input("Digite o nome: ")
peso = float(input("Digite o peso: "))

if peso < 52:
    categoria = ""
elif peso < 65:
    categoria = "Pena"
elif peso < 72:
    categoria = "Leve"
elif peso < 79:
    categoria = "Ligeiro"
elif peso < 86:
    categoria = "Meio-medio"
elif peso < 90:
    categoria = "Medio"
elif peso < 100: 
    categoria = "Meio-pesado"
else:
    categoria = "Pesado"

if categoria != "":
    print(f"O lutador {nome} pesa {peso:.3f} kg se enquadra na categoria {categoria}")
else:
    print(f"Peso invalido: {peso}")
