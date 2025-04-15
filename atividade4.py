# faça um código para ler 2 valores e realize a divisão do primeiro pelo segundo valor recebido,
# caso o segunto valor digitado seja zero, solicite novamente o valor,
# informando que só aceitaremos valores diferentes de zero

valor1 = int(input("Informe o primeiro valor: "))
valor2 = int(input("Informe o segundo valor: "))
while valor2 == 0:
    valor2 = int(input("Só aceitaremos valores diferentes de zero. "
                       "\nInforme o segundo valor valor: "))
divisão = valor1 / valor2
print (f"A divisão é {divisão}")