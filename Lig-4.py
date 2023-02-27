n_col = ['1','2','3','4','5','6','7']
tabuleiro = [['_','_','_','_','_','_','_'],['_','_','_','_','_','_','_'],['_','_','_','_','_','_','_'],['_','_','_','_','_','_','_'],['_','_','_','_','_','_','_'],['_','_','_','_','_','_','_']]

print("*******************")
print("Bem vindo ao Lig-4!")
print("*******************")

print(n_col)
for x in tabuleiro:
    print(x)
print(n_col)

fechou = False
vitoria = False
vez = "X"

while (not fechou and not vitoria): #Faz a "peça cair"
    print(f"Agora é vez de {vez}")
    col = int(input("Selecione a coluna!")) - 1 #'-1' tá aí porque a primeira coluna do Python é zero, mas eu queria que fosse 1.

    i=0
    while (tabuleiro[i][col] == '_' and i<6):
        i += 1

        if (i==5):
            if(tabuleiro[5][col]=="_"):
                i +=1
                break
            else:
                break

    tabuleiro[i-1][col]=vez
    print(n_col)
    for x in tabuleiro:
        print(x)
    print(n_col) #Faz a "peça cair"\

#condição de vitória horizontal
    for x in tabuleiro:
        contador = 0
        for y in x:
            if (y == vez):
                contador += 1
                if (contador == 4):
                    vitoria = True #Falta identificar de quem é a vitória
            else:
                contador = 0

# condição de vitória horizontal (Lógica idêntica ao ciclo anterior, basta transpor a lista)
    for x in list(zip(*tabuleiro)):
        contador = 0
        for y in x:
            if (y == vez):
                contador += 1
                if (contador == 4):
                   vitoria = True  # Falta identificar de quem é a vitória
            else:
                contador = 0

# condição de vitória na diagonal [A FAZER]

    if ('_' not in tabuleiro[0]):
        fechou = True

    if (vez == "X"): #Passa a vez
        vez = "O"
    else:
        vez = "X"

if (fechou):
    print("O Jogo empatou!")

if (vitoria):
    print(f"Vitória das {vez}!")