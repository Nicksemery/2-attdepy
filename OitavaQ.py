# Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em estoque e quantidade mínima em estoque de um produto. Calcular e escrever a
# quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2). Se a quantidade em estoque for maior ou igual a quantidade média, escrever a
# mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar compra'.

atual = int(input("qual a quantidade em estoque atualmente? "))
max = int(input("qual a quantidade máxima? "))
min = int(input("qual a quantidade mínima? "))
media = (max + min)/2
if atual >= media :
    print (F"Possuimos {atual} itens de uma média de {media}. Não efetuar compra")
else:
    print (F"Possuimos {atual} itens de uma média de {media}. Efetuar compra")