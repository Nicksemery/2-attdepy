# Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também
# testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.

conta = int(input("numero da conta "))
saldo = int(input("saldo "))
debito = int(input("debito "))
credito = int(input("credito "))
saldoatual = saldo - debito + credito
if saldoatual >=0 :
    print ("saldo positivo")
else:
    print ("saldo negativo")