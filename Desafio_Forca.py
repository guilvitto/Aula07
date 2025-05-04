segredo = "gui"
dig = ["_"] * len(segredo)    # digitos
t = 6                         # tentativas
while t!=0:
    print(dig)
    letra = input("digite uma letra de A-Z: ").lower()
    for i in range(len(segredo)):
        if letra == segredo[i]:
            dig[i] = letra
            print(f"A Letra {letra} está correta!")
    if letra not in segredo and t!=0:
        print(f"A Letra {letra} está incorreta!", end=" ")
        t-=1
        print(f"Restam {t} tentativas...")
    elif "_" not in dig:
        print(f"Parabéns,você ganhou! A palavra era {segredo.upper()}.")
        break
if t==0:
    boneco = r"""
         _______
        |/      |
        |       0
        |      /|\
        |      / \
        |
      __|_________"""
    print(boneco)
    print("       Game over!       ")





