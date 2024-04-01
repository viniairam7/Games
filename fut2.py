
import tkinter as tk
from tkinter import messagebox
import random

class JogoFutebolGUI:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Jogo de Futebol")

        self.frame = tk.Frame(janela)
        self.frame.pack(padx=20, pady=20)

        self.label_time1 = tk.Label(self.frame, text="Time 1:")
        self.label_time1.grid(row=0, column=0, padx=5, pady=5)
        self.entry_time1 = tk.Entry(self.frame)
        self.entry_time1.grid(row=0, column=1, padx=5, pady=5)

        self.label_time2 = tk.Label(self.frame, text="Time 2:")
        self.label_time2.grid(row=1, column=0, padx=5, pady=5)
        self.entry_time2 = tk.Entry(self.frame)
        self.entry_time2.grid(row=1, column=1, padx=5, pady=5)

        self.start_button = tk.Button(self.frame, text="Iniciar Jogo", command=self.iniciar_jogo)
        self.start_button.grid(row=2, columnspan=2, padx=5, pady=5)

        self.resultado_label = tk.Label(self.frame, text="")
        self.resultado_label.grid(row=3, columnspan=2, padx=10, pady=5)

        self.pontuacao_label = tk.Label(self.frame, text="")
        self.pontuacao_label.grid(row=4, columnspan=2, padx=10, pady=5)

        self.pontuacao_time1 = 0
        self.pontuacao_time2 = 0

    def chutar_gol(self, time):
        mensagem = f"Você deseja chutar a gol, {time}? (s/n)"
        resposta = messagebox.askyesno("Chutar Gol", mensagem)
        if resposta:
            self.resultado_label.config(text=f"{time} chutou a gol!")
            chance_acertar = random.random()  # Chance de acertar o gol
            if chance_acertar > 0.5:  # 50% de chance de acertar o gol
                if time == self.entry_time1.get():
                    self.pontuacao_time1 += 1
                else:
                    self.pontuacao_time2 += 1
            else:
                self.resultado_label.config(text=f"{time} errou o gol!")
        else:
            self.resultado_label.config(text=f"{time} não chutou a gol!")
        self.atualizar_placar()

    def iniciar_jogo(self):
        time1 = self.entry_time1.get()
        time2 = self.entry_time2.get()
        if not time1 or not time2:
            messagebox.showwarning("Atenção", "Por favor, insira os nomes dos times.")
            return

        while self.pontuacao_time1 < 3 and self.pontuacao_time2 < 3:
            self.chutar_gol(time1)
            if self.pontuacao_time1 >= 3:
                vencedor = f"O time {time1} venceu!"
                self.resultado_label.config(text=vencedor)
                break
            self.chutar_gol(time2)
            if self.pontuacao_time2 >= 3:
                vencedor = f"O time {time2} venceu!"
                self.resultado_label.config(text=vencedor)

    def atualizar_placar(self):
        placar_atual = f"Placar atual: {self.entry_time1.get()} {self.pontuacao_time1} - {self.pontuacao_time2} {self.entry_time2.get()}"
        self.pontuacao_label.config(text=placar_atual)

# Criar janela
janela = tk.Tk()
app = JogoFutebolGUI(janela)
janela.mainloop()

