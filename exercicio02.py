nomes=[""]*5
for i in range(len(nomes)):
    nomes[i]= input("Digite o nome do aluno: ")
for x in range(len(nomes)):
    print(f"Encontrei o {nomes[x]} na posição {x}")