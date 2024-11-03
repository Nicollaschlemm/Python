#Classificação indicativa é um conceito que se aplica à faixa etária para a qual uma obra audiovisual
#se recomenda ou não. Suponha que um filme em cartaz no cinema tenha a Classificação de 16 anos.
#Escreva um programa que leia a idade de uma pessoa e mostre se está de acordo ou não com a
#classificação.

idade = int(input("Digite sua idade: "))

if idade < 16: 
    print("Não esta de acordo com a classificação")
else:
    print("Esta de acordo com a classificação")
