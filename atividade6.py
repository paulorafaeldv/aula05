# ler 2 valores e digitar a média. se o valor for abaixo de 0 e acima de 10, pedir novamente

nota1 = float(input("Informe a primeira nota: "))

while nota1 < 0 or nota1 > 10:
    nota1 = float(input("Valor inválido. Digite novamente: "))

nota2 = float(input("Informe a segunda nota: "))

while nota2 < 0 or nota2 > 10:
    nota2 = float(input("Valor inválido. Digite novamente: "))

media = (nota1 + nota2) / 2
print (f"A média é {media}")
