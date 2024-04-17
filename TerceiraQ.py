# As maçãs custam 1,30 cada, se forem compradas menos de uma dúzia, e 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs
# compradas, calcule e escreva o custo total da compra.

maça = int(input("quantas maçãs você quer? "))
n1 = maça *1
n2 = maça *1.3
if maça >= 12 :
    print(f"{maça} maçãs sai por R$ {n1}")
else:
    print(f"{maça} maçãs sai por R$ {n2}")