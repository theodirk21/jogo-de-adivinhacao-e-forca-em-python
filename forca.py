import random




def jogar():

    imprime_mensagem_inicial()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0



    while(not enforcou and not acertou):

        chute = solicita_chute()

        if (chute in palavra_secreta):
            informa_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        if (erros == 7):
            print("Você errou a palavra era {} ".format(palavra_secreta))
            break

        elif ("_" not in letras_acertadas):
            print("Você acertou a palavra {} ".format(palavra_secreta))
            break

        print(letras_acertadas)



def imprime_mensagem_inicial():
    print("---------------------------------")
    print("Bem vindo ao jogo de forca!")
    print("---------------------------------")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo :
        linha = linha.strip()
        palavras.append(linha)  # esse é para percorrer cada linha do arquivo e armazenar

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def solicita_chute():
    chute = input("Qual Letra? ")
    chute = chute.strip().upper()
    return chute

def informa_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1



def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

#para funcionar separadamente no cmd
if(__name__ == "__main__"):
    jogar()