import random

def realizar_jogada(time):
    print(f"É a vez do {time} atacar!")
    input("Pressione Enter para chutar a gol...")
    gol_chance = random.randint(1, 10)
    if gol_chance > 5:
        print("GOOOOL!!!")
        return 1
    else:
        print("A bola foi para fora!")
        return 0

def main():
    time1 = input("Digite o nome do Time 1: ")
    time2 = input("Digite o nome do Time 2: ")

    pontuacao_time1 = 0
    pontuacao_time2 = 0

    while True:
        input("Pressione Enter para iniciar a próxima jogada...")
        pontuacao_time1 += realizar_jogada(time1)
        pontuacao_time2 += realizar_jogada(time2)

        print(f"Placar atual: {time1} {pontuacao_time1} - {pontuacao_time2} {time2}")

        continuar = input("Deseja continuar o jogo? (s/n): ")
        if continuar.lower() != 's':
            break

    print("Fim de Jogo!")
    print(f"Placar final: {time1} {pontuacao_time1} - {pontuacao_time2} {time2}")

if __name__ == "__main__":
    main()



