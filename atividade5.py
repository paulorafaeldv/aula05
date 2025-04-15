pin = 1234
tentativas = 0
while tentativas < 3:
    senha = int(input("Digite a senha: "))
    if senha == pin:
        print ("Senha correta!")
        break
    tentativas += 1
if senha != pin:
    print ("CARTÂO BLOQUEADO")
