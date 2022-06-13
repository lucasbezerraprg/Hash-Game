import os

jogarNovamente = "s"
jogadas = 0
vezJogador = 1
maxJogadas = 9
escolhaUsuario1 = "X"
escolhaUsuario2 = "O"
winner = "n"
hash = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def Jogo():
    global hash
    global jogadas
    os.system("cls")
    print("     0   1   2")
    print("0:   " + hash[0][0] + " | " + hash[0][1] + " | " + hash[0][2])
    print("    -----------")
    print("1:   " + hash[1][0] + " | " + hash[1][1] + " | " + hash[1][2])
    print("    -----------")
    print("2:   " + hash[2][0] + " | " + hash[2][1] + " | " + hash[2][2])
    print("Jogadas: " + str(jogadas))


def jogadorUmJoga():
    global jogadas
    global vezJogador
    global maxJogadas

    if vezJogador == 1 and jogadas < maxJogadas:
        try:
            print("Jogador 1 jogando.")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            while hash[linha][coluna] != " ":
                print("Linha e/ou coluna já marcada. Por favor, tente novamente.")
                linha = int(input("Linha: "))
                coluna = int(input("Coluna: "))
            hash[linha][coluna] = escolhaUsuario1
            vezJogador = 2
            jogadas += 1
        except:
            print("Linha e/ou coluna inválida.")
            os.system("pause")


def jogadorDoisJoga():
    global jogadas
    global vezJogador
    global maxJogadas

    if vezJogador == 2 and jogadas < maxJogadas:
        try:
            print("Jogador 2 jogando.")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            while hash[linha][coluna] != " ":
                print("Linha e/ou coluna já marcada. Por favor, tente novamente.")
                linha = int(input("Linha: "))
                coluna = int(input("Coluna: "))
            hash[linha][coluna] = escolhaUsuario2
            vezJogador = 1
            jogadas += 1
        except:
            print("Linha e/ou coluna inválida.")
            os.system("pause")


def verificarVitoria():
    global hash
    vit = "n"
    simbolos = ["X", "O"]

    for s in simbolos:
        vit = "n"

        # Verificar vitória em linhas
        iDiagL = iDiagC = 0

        while iDiagL < 3:
            soma = 0
            iDiagC = 0
            while iDiagC < 3:
                if hash[iDiagL][iDiagC] == s:
                    soma += 1
                iDiagC += 1
            if soma == 3:
                vit = s
                break
            iDiagL += 1

        if vit != "n":
            break

        # Verificar vitória em colunas
        iDiagL = iDiagC = 0

        while iDiagC < 3:
            soma = 0
            iDiagL = 0
            while iDiagL < 3:
                if hash[iDiagL][iDiagC] == s:
                    soma += 1
                iDiagL += 1

            if soma == 3:
                vit = s
                break
            iDiagC += 1

        if vit != "n":
            break

        # Verificar viótira na diagonal principal 1
        soma = 0
        iDiagL = 0
        iDiagC = 0

        while iDiagL < 3:
            if hash[iDiagL][iDiagC] == s:
                soma += 1
            iDiagL += 1
            iDiagC += 1

        if soma == 3:
            vit = s
            break

        # Verificar diagonal secundária 2
        soma = 0
        iDiagL = 0
        iDiagC = 2

        while iDiagC >= 0:
            if hash[iDiagL][iDiagC] == s:
                soma += 1
            iDiagL += 1
            iDiagC -= 1

        if soma == 3:
            vit = s
            break
    return vit


def reset():
    global hash
    global jogadas
    global vezJogador
    global maxJogadas
    global winner
    global escolhaUsuario1
    global escolhaUsuario2
    jogadas = 0
    vezJogador = 1
    maxJogadas = 9
    escolhaUsuario1 = "X"
    escolhaUsuario2 = "O"
    winner = "n"
    hash = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


while jogarNovamente.lower() == "s": #.lower = Caso o "S" seja maiusculo, ele é convertido em minusculo "s".
    while True: #looping funcionando infinitamente até que um break pare ele.
        Jogo() #atualiza o tabuleiro
        jogadorUmJoga() #jogada do jogador 1
        Jogo() #atualiza o tabuleiro
        jogadorDoisJoga() #jogada do jogador 2
        Jogo() #atualiza o tabuleiro
        winner = verificarVitoria() #Sempre n, ate que alguém ganhe.
        if (winner != "n") or (jogadas >= maxJogadas): #Caso não seja atendido, o loop continua.
            break #Para o loop caso o if seja atendido.

    print("Fim de jogo!")
    if winner == "X" or winner == "O":
        print("O jogador",winner,"venceu!")
    else:
        print("Deu velha!")

    jogarNovamente = input("Jogar novamente? [s/n]:")
    reset()
    print("Obrigado por jogar!!!") 