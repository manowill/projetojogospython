import random
import jogos

def jogar():
    print("*****************************************")
    print("     Bem vindo ao jogo de Adivinhação!   ")
    print("*****************************************")

    numero_secreto = random.randrange(1, 51)
    total_de_tentativas = 0
    pontos = 500
    revelacao_dos_pontos = numero_secreto

    print("")
    print("Qual o nível de dificuldade?")
    print("")
    print("(1) Fácil (2) Médio (3) Difícil")
    print("")
    nivel = (input("Defina o nível: "))
    print("")

    if (nivel ==  "1"):
        total_de_tentativas = 8
    if (nivel ==  "2"):
        total_de_tentativas = 5
    if (nivel == "3"):
        total_de_tentativas = 3



    for rodada in range(1, total_de_tentativas + 1):

        print("*****************************************")

        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 50: ")
        print("")
        print("")
        print("Você digitou ", chute_str)
        chute = int(chute_str)


        if (chute < 1 or chute > 50):
            print("")
            print("Você deve digitar um número entre 1 e 50!")
            print("")
            continue


        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("")
                print("Você errou! O seu chute foi maior do que o número secreto.")
                print("")
                print("")

            elif (menor):
                print("")
                print("Você errou! O seu chute foi menor do que o número secreto.")
                print("")
                print("")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("o número secreto era:", numero_secreto)
    print("fim do breve jogo")
    acabou = 1

    if (acabou == 1):

        jogos.escolher_jogo()



if(__name__== "__main__"):
    jogar()

