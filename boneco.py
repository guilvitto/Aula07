segredo = "gui"
dig = ["_"] * len(segredo)    # digitos
t = 6
corpo1 =  "O"
corpo2 =  "|"
corpo3 =  ">"
corpo4 =  '<'
corpo5 =  "J"
corpo6 =  "l"
while t!=0:
    print(dig)
    l = input("digite uma letra de A-Z: ").lower()
    for i in range(len(segredo)):
        if l == segredo[i]:
            dig[i] = l
            print(f"A Letra {l} está correta!")
    print(" +---+")
    print(" |   |")
    print(" " + ("O" if t == 5 else " ") + "   |")

    bracos = ""
    if t >= 3:
        bracos = "/|\\"
    elif t == 2:
        bracos = "/|"
    elif t == 1:
        bracos = " |"
    print(bracos.ljust(4) + "|")

    pernas = ""
    if t >= 5:
        pernas = "/ \\"
    elif t == 4:
        pernas = "/"
        print(pernas.ljust(4) + "|")
        print("     |")
        print("=====")
    elif "_" not in dig:
        print(f"Parabéns,você ganhou! A palavra era {segredo.upper()}.")
        break


