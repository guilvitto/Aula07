nomes = ["joão", "carlos", "maria", "luiza", "isabel"]
n = input("Digite o nome do aluno pra saber a posição: ")
for i in range(len(nomes)):
    if n == nomes[i]:
        print(f"Encontrei o {nomes[i]} na posição {i}")