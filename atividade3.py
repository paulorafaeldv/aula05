nalunos = int(input("Quantos alunos tem na sala? "))
total = 1
soma = 0
while total <= nalunos:
    notas = float(input(f"Informe {total}ª nota: "))
    soma += notas
    total += 1
media = soma/nalunos
print (f"A média da sala é {media}")