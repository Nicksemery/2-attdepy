# Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que
# nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.

nota1 = float(input("nota "))
nota2 = float(input("nota 2 "))
soma = (nota1+nota2) /2
if soma >= 6:
    print ("aprovado", soma)
else:
    print ("reprovado", soma)