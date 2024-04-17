# Solicite ao usuário um valor numérico, inteiro ou real, e escrever se é positivo ou negativo (considere o valor zero como positivo).

numero = float(input("digite um numero "))
if numero < 0:
    print("negativo")
elif numero >= 0:
    print("positivo")