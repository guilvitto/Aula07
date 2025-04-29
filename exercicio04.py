notas=[""]*5 #ou [0.0]
soma=0
media=0
qtd=0
for i in range(len(notas)):
    notas[i]=float(input(f"Digite a nota do aluno {i+1}: "))
for s in range(len(notas)):
    soma = soma + notas[s]
media=soma/len(notas)
for x in range(len(notas)):
    if notas[x] > media:
        qtd=qtd+1

print(notas)
print(media)
print(qtd)