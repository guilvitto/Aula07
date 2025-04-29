usuarios=["joao","carlos","mario","maria","josefa"]
senhas=[1234,3432,5432,3333,6666]
l= input("Digite seu usuário: ")
s= int(input("Digite sua senha: "))
for j in range(len(usuarios)):
    if l == usuarios[j]:
        print("Usuário aceito!")
        if s == senhas[j]:
            print("Senha aceita!")
            break
        else:
            print("Senha Recusada!")
            break
    else:
        print("Usuário Recusado!")
        break