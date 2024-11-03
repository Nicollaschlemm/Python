#Em um determinado momento do dia a cotação de compra das moedas estrangeiras é a seguinte:
#Dólar: US$ 1.00 = R$ 5.87 - Euro: € 1.00 = R$ 6.20 - Libra Esterlina: £ 1.00 = R$ 7.59
#Escreva um programa que leia o tipo (D, E ou L maiúsculo) e o valor de moeda estrangeira que se
#quer comprar e calcule o valor em reais necessario

moeda = input("Digite D(Dolar), E(Euro) ou L(Libra Esterlina): ")
valor = float(input("Digite o valor que deseja trocar: "))

moeda = moeda.upper()

if moeda == "D":
    dolar = valor * 5.87 
    print(f"È necessario R${dolar:.2f} para compar US${valor:.2f}")
elif moeda == "E":
    euro = valor * 6.20
    print(f"È necessario R${euro:.2f} para compar €${valor:.2f}")
elif moeda == "L":
    libra = valor * 7.59
    print(f"È necessario R${libra:.2f} para compar £${valor:.2f}")
else: 
    print("Opção Invalida")