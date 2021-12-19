import Forca
import advinhacao


def escolher_jogo():
    def escolha_jogo():
        print("")
        print("(1) forca  (2)advinhação ")
        print("")

    print("***********************************************************************************")
    print("                                       escolha o seu jogo                          ")
    print("***********************************************************************************")

    escolha_jogo()


    jogo = (input("escolha o número do jogo desejado: "))

    if (jogo == "1"):
        print("")
        print("")
        print(Forca.jogar())

    elif (jogo == "2"):
        print("")
        print("")
        print(advinhacao.jogar())

    if (jogo != "1" or "2"):
       print("")
       print("******************************DIGITE APENAS OS NÚMEROS APRESENTADOS****************************")
       escolher_jogo()


if (__name__ == "__main__"):
    escolher_jogo()