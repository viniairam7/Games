import tkinter as tk
from tkinter import messagebox
import random

class JogoFutebolGUI:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Jogo de Futebol")

        self.canvas = tk.Canvas(janela, width=800, height=400, bg="green")
        self.canvas.pack()

        self.time1 = self.canvas.create_oval(50, 200, 100, 250, fill="blue")
        self.time2 = self.canvas.create_oval(750, 200, 800, 250, fill="red")

        self.pontuacao_label = tk.Label(self.janela, text="Placar: 0 - 0", font=("Arial", 14))
        self.pontuacao_label.pack(pady=10)

        self.pontuacao_time1 = 0
        self.pontuacao_time2 = 0

    def chutar_gol(self, time):
        chance_acertar = random.random()  # Chance de acertar o gol
        if chance_acertar > 0.5:  # 50% de chance de acertar o gol
            if time == self.time1:
                self.pontuacao_time1 += 1
                self.canvas.move(self.time1, 20, 0)
            else:
                self.pontuacao_time2 += 1
                self.canvas.move(self.time2, -20, 0)
        self.atualizar_placar()

    def iniciar_jogo(self):
        while self.pontuacao_time1 < 3 and self.pontuacao_time2 < 3:
            self.chutar_gol(self.time1)
            if self.pontuacao_time1 >= 3:
                vencedor = f"O time azul venceu!"
                messagebox.showinfo("Fim de Jogo", vencedor)
                break
            self.chutar_gol(self.time2)
            if self.pontuacao_time2 >= 3:
                vencedor = f"O time vermelho venceu!"
                messagebox.showinfo("Fim de Jogo", vencedor)

    def atualizar_placar(self):
        placar_atual = f"Placar: {self.pontuacao_time1} - {self.pontuacao_time2}"
        self.pontuacao_label.config(text=placar_atual)

# Criar janela
janela = tk.Tk()
app = JogoFutebolGUI(janela)

btn_iniciar = tk.Button(janela, text="Iniciar Jogo", command=app.iniciar_jogo)
btn_iniciar.pack(pady=10)

janela.mainloop()

