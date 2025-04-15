# ler 10 valores, calcular e escrever a média aritmetica desses valores lidos usando o while

cont = 1
soma = 0
while cont < 11:
    va = int(input(f"Informe o {cont}º valor: "))
    soma += va
    cont += 1
media = soma/10
print (f"A média dos 10 valores é {media}")