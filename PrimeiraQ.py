# Solicite ao usuário um valor numérico, inteiro ou real, e verifique se ele é maior ou menor que 10. O programa deve escrever a mensagem correspondente (maior ou
# menor) e informar o valor digitado pelo usuário.

numero = int(input("digite um numero "))
if numero < 10 :
    print( numero,"menor que dez")
elif numero > 10 :
    print(numero,"maior que dez")
else:
    print(numero, "Dez é dez")