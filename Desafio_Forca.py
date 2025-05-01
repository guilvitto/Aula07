segredo = "gui"
dig = ["_"] * len(segredo)    # digitos
t = 6                         # tentativas
while t!=0:
    print(dig)
    l = input("digite uma letra de A-Z: ").lower()
    for i in range(len(segredo)):
        if l == segredo[i]:
            dig[i] = l
            print(f"A Letra {l} está correta!")
    if l not in segredo and t!=0:
        print(f"A Letra {l} está incorreta!",end=" ")
        t-=1
        print(f"Restam {t} tentativas...")
    elif "_" not in dig:
        print(f"Parabéns,você ganhou! A palavra era {segredo.upper()}.")
        break
    elif l not in segredo and t==0:
        print(" Game over!! ")
        break

