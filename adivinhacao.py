import random


def jogar():


    print("---------------------------------")
    print("Bem vindo ao jogo de adivinhação!")
    print("---------------------------------")

    numero_secreto = round(random.randrange(1, 101))
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nivel de dificuldade?")
    print("(1) Fácil (2) Medio (3) Dificil")

    nivel = int(input("Define o nível:"))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
         total_de_tentativas = 4


    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}:".format(rodada, total_de_tentativas))
        chute_str = input("Digite um numero entre 1 e 100: ")
        print("Voce digitou: ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um numero entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto


        if (acertou):
            print("Voce acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! Seu chute foi maior que o desejado.")
            elif (menor):
                print("Você errou! Seu chute foi menor que o desejado.")


            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            rodada = rodada + 1


    print("Final do jogo, o numero secreto é {}!".format(numero_secreto))


if(__name__ == "__main__"):
    jogar()