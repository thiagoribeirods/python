import random
import time
#Gera uma mensagem chamada pelo main()
def msg():
    print("\t\t\t\tPYTHON NAVAL \n\n\n\n")
#São as regras para iniciar a partida
def regras():
    print("A tropa soviética resolveu invadir o Brasil e só você pode derrotar esse feroz inimigo.")
    print("Você terá que encontrar os barcos inimigos e destruí-los o quanto antes!!!!")
    print("Você verá o mapa com as cordenadas para disparar contra as embarcações inimigas. Mas seja cuidadoso! Você terá 35 tiros.")
    print("Cada acerto será apresentado como um 'X'. Os erros serão apresentados com '0'")
    print('''
                                                    O inimigo terá 5 embarcações:
                                                    Submarino - 1x2 (Tamanho)
                                                    Fragata - 1x3 (Tamanho)
                                                    Destroyer - 1x4 (Tamanho)
                                                    Cruzador - 1x5 (Tamanho)
                                                    Seu país conta com você!!! ''')
    print("Você terá 25 tentativas.")
    
    iniciar = input("Pressione qualquer tecla para prosseguir.")
    jogar()
#Gera o mapa do jogo usando as matrizes
def mapaJogo():
    mapa = []
    for i in range(11):
        linha = []
        for j in range(11):
            linha.append("!")
        mapa.append(linha)
    for i in range(11):
        mapa[i][0] = i
    for j in range(11):
        mapa[0][j]= j
    return mapa

#Exibe o mapa
def gerando_mapa(mapinha):
    for i in range(11):
        for j in range(11):
            print(mapinha[i][j], end=" ")
        print("\t\n")

#Início da criação dos objetos
def cruzador(mapa,linha,coluna,vertical):
    if vertical == True and linha>6 or vertical == False and coluna>6:
         return False
    else:
        if vertical == True:
            for x in range(linha,linha+5):
                if mapa[x][coluna] != "!":
                    return False
            for x in range(linha,linha+5):
                mapa[x][coluna] = "C"
            return True
        else:
            for x in range(coluna,coluna+5):
                if mapa[linha][x] != "!":
                    return False
            for x in range(coluna,coluna+5):
                mapa[linha][x] = "C"
            return True

def destroyer(mapa,linha,coluna,vertical):
    if vertical == True and linha>7 or vertical == False and coluna>7:
         return False
    else:
        if vertical == True:
            for x in range(linha,linha+4):
                if mapa[x][coluna] != "!":
                    return False
            for x in range(linha,linha+4):
                mapa[x][coluna] = "D"
            return True
        else:
            for x in range(coluna,coluna+4):
                if mapa[linha][x] != "!":
                    return False
            for x in range(coluna,coluna+4):
                mapa[linha][x] = "D"
            return True

def fragata(mapa,linha,coluna,vertical):
    if vertical == True and linha>8:
         return False
    elif vertical == False and coluna>8:
        return False
    else:
        if vertical == True:
            for x in range(linha,linha+3):
                if mapa[x][coluna] != "!":
                    return False
            for x in range(linha,linha+3):
                mapa[x][coluna] = "F"
            return True
        else:
            for x in range(coluna,coluna+3):
                if mapa[linha][x] != "!":
                    return False
            for x in range(coluna,coluna+3):
                mapa[linha][x] = "F"
            return True

def submarino(mapa,linha,coluna,vertical):
    if vertical == True and linha>9 or vertical == False and coluna>9:
         return False
    else:
        if vertical == True:
            for x in range(linha,linha+2):
                if mapa[x][coluna] != "!":
                    return False
            for x in range(linha,linha+2):
                mapa[x][coluna] = "S"
            return True
        else:
            for x in range(coluna,coluna+2):
                if mapa[linha][x] != "!":
                    return False
            for x in range(coluna,coluna+2):
                mapa[linha][x] = "S"
            return True
#fim da criação dos objetos
        
def atirar(mapa,linha,coluna,mapa_es):
    if mapa[linha][coluna] == "!":
        mapa[linha][coluna] = "o"
        mapa[linha][coluna] = "o"
        print("\n\nTIRO NA ÁGUA!!!!! CUIDADO! n\n")
        print("Mapa de batalha: ")
        gerando_mapa(mapa_es)
        return True,False
    elif mapa[linha][coluna] == "o" or mapa[linha][coluna] == "O":
        print("\n\nNão desperdice suas munições onde você já jogou!\n\n")
        return False,True
    else:
        mapa[linha][coluna] = "O"
        mapa_es[linha][coluna] = "O"
        print("\n\n Belo tiro, Soldado!\n\n")
        print("Mapa de batalha: ")
        gerando_mapa(mapa_es)
        return True,True
    
#jogar, gerando aleatoriamente.    
def jogar():      
        pontos = 0
        tiros = 25
        mapa = mapaJogo()
        mapa_es = mapaJogo()
        print("Mapa de batalha: \n\n")
        gerando_mapa(mapa_es)
        verifica = cruzador(mapa,random.randint(1,10),random.randint(1,10),False)
        while verifica == False:
            verifica = cruzador(mapa,random.randint(1,10),random.randint(1,10),False)
        verifica = destroyer(mapa,random.randint(1,10),random.randint(1,10),True)
        while verifica == False:
            verifica = destroyer(mapa,random.randint(1,10),random.randint(1,10),True)
        verifica = fragata(mapa,random.randint(1,10),random.randint(1,10),False)
        while verifica == False:
            verifica = fragata(mapa,random.randint(1,10),random.randint(1,10),False)
        verifica = submarino(mapa,random.randint(1,10),random.randint(1,10),True)
        while verifica == False:
            verifica = submarino(mapa,random.randint(1,10),random.randint(1,10),True)
        while pontos<14 and tiros>0:
            print("Você tem: ",tiros)
            linha = int(input("Digite a coordenada horizontal: "))
            while linha < 1 or linha > 10:
                linha = int(input("\nNão tente trair seu país!!!!! \n\nDigite a coordenada correta da sua jogada : "))
            coluna = int(input("Digite a coordenada vertical da sua jogada: "))
            while coluna <1 or coluna> 10:
                coluna = int(input("\n Você pode acabar com seu país agindo desse jeito!!\n\nDigite a coordenada vertical da sua jogada: "))
            tiro,verifica = atirar(mapa,linha,coluna,mapa_es)
            if tiro == True and verifica == True:
                pontos +=1
                tiros -= 1
            elif tiro == True and verifica == False:
                tiros -= 1
        if pontos == 14:
            print("\n\nVocê venceu! Os Soviéticos foram aniquilidados. Seu país agradece.")
        else:
            print("\n\nSem munição! Veja a destruição: \n")
#método principal
def main():
    msg()
    print("O jogo está sendo carregado, por favor, aguarde.")
    time.sleep(5)
    escolha = int(input("MENU -> PYTHON NAVAL \n1 - Regras \n2 - Jogar \n\n"))
    if escolha == 1:
        print("Carregando tropas...")
        time.sleep(1)
        print("Colocando navios na água...")
        time.sleep(1)
        print("Preparando navio...")
        time.sleep(1)
        print("Apontando...")
        time.sleep(1)
        print("Pronto para partir!")
        time.sleep(1)      
        regras()
    else:
        print("Carregando tropas...")
        time.sleep(1)
        print("Colocando navios na água...")
        time.sleep(1)
        print("Preparando navio...")
        time.sleep(1)
        print("Apontando...")
        time.sleep(1)
        print("Pronto para partir!")
        time.sleep(1)      
        jogar()
    
main()    
