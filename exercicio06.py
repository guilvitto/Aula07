num=[""]*5
for i in range(len(num)):
    num[i]= input(f"Digite o número {i+1}: ")
for j in range(len(num)-1,-1,-1):
    print(num[j], end=" ")