vetorA=[""]*5
vetorM=[""]*5
for i in range(len(vetorA)):
    vetorA[i]=float(input(f"Digite o valor {i+1}: "))
x= float(input("Digite o valor de X para multiplicar: "))
for s in range(len(vetorA)):
    vetorM[s] = x * vetorA[s]
print(vetorM, end=" ")