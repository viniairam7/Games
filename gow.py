import time
import webbrowser

def batalha():
    print("Você encontra um terrível Minotauro!")
    print("Kratos está pronto para a batalha!")

    while True:
        acao = input("O que Kratos deve fazer? (atacar/fugir): ").lower()

        if acao == "atacar":
            print("Kratos parte para o ataque!")
            time.sleep(1)
            print("Você derrota o Minotauro com sua lâmina do caos!")
            break
        elif acao == "fugir":
            print("Kratos tenta fugir, mas o Minotauro o alcança!")
            time.sleep(1)
            print("Você foi derrotado!")
            break
        else:
            print("Ação inválida. Tente novamente.")

def main():
    print("Kratos está em uma jornada épica, pronto para enfrentar qualquer desafio.")

    input("Pressione Enter para iniciar a batalha...")
    batalha()

    print("Fim do Jogo.")

if __name__ == "__main__":
    main()

def contar_historia():
    historia = """
    Kratos é um guerreiro espartano que, após perder sua família, jura vingança contra os deuses do Olimpo. 
    Ele é o protagonista da série de jogos God of War, conhecido por sua ferocidade e busca por redenção.
    Ao longo de sua jornada, Kratos enfrenta diversos desafios e inimigos mitológicos, 
    enquanto luta para superar seu passado e controlar sua raiva desenfreada.
    """
    print(historia)

def abrir_video():
    url = "https://www.youtube.com/watch?v=pyYseKtlXD4&pp=ygUSZ29kIG9mIHdhciBoaXN0b3J5"  # Link para o vídeo do YouTube
    webbrowser.open(url)

def main():
    print("Bem-vindo ao Jogo de God of War!")
    input("Pressione Enter para continuar e ouvir a história de Kratos...")
    contar_historia()
    input("Pressione Enter para assistir ao vídeo mais visualizado sobre God of War...")
    abrir_video()
    print("Espero que tenha gostado!")

if __name__ == "__main__":
    main()
