import tkinter as tk
from tkinter import ttk, messagebox
from jogo import jogo, heroi, inimigo

class InterfaceJogo:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Arena de Batalha")
        self.janela.geometry("800x600")
        
        # Inicializa o jogo
        self.jogo = jogo()
        
        # Configura a interface
        self.criar_interface()
        
    def criar_interface(self):
        # Frame principal
        self.frame_principal = ttk.Frame(self.janela, padding="10")
        self.frame_principal.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Área de status do Herói
        self.frame_heroi = ttk.LabelFrame(self.frame_principal, text="Seu Herói", padding="5")
        self.frame_heroi.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        
        self.label_heroi_status = ttk.Label(self.frame_heroi, text="")
        self.label_heroi_status.grid(row=0, column=0, padx=5, pady=5)
        
        # Área de status do Inimigo
        self.frame_inimigo = ttk.LabelFrame(self.frame_principal, text="Inimigo", padding="5")
        self.frame_inimigo.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        
        self.label_inimigo_status = ttk.Label(self.frame_inimigo, text="")
        self.label_inimigo_status.grid(row=0, column=0, padx=5, pady=5)
        
        # Área de ações
        self.frame_acoes = ttk.LabelFrame(self.frame_principal, text="Ações", padding="5")
        self.frame_acoes.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W)
        
        # Botões de ação
        self.btn_ataque_normal = ttk.Button(self.frame_acoes, text="Ataque Normal", command=self.ataque_normal)
        self.btn_ataque_normal.grid(row=0, column=0, padx=5, pady=5)
        
        self.btn_ataque_especial = ttk.Button(self.frame_acoes, text="Ataque Especial", command=self.ataque_especial)
        self.btn_ataque_especial.grid(row=0, column=1, padx=5, pady=5)
        
        self.btn_ataque_critico = ttk.Button(self.frame_acoes, text="Ataque Crítico", command=self.ataque_critico)
        self.btn_ataque_critico.grid(row=0, column=2, padx=5, pady=5)
        
        self.btn_curar = ttk.Button(self.frame_acoes, text="Curar", command=self.curar)
        self.btn_curar.grid(row=0, column=3, padx=5, pady=5)
        
        self.btn_regenerar = ttk.Button(self.frame_acoes, text="Regenerar Energia", command=self.regenerar)
        self.btn_regenerar.grid(row=0, column=4, padx=5, pady=5)
        
        # Área de log
        self.frame_log = ttk.LabelFrame(self.frame_principal, text="Log de Batalha", padding="5")
        self.frame_log.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        self.text_log = tk.Text(self.frame_log, height=10, width=70)
        self.text_log.grid(row=0, column=0, padx=5, pady=5)
        
        # Inicia o primeiro inimigo
        self.iniciar_batalha()
        
    def atualizar_status(self):
        # Atualiza status do herói
        status_heroi = (
            f"Nome: {self.jogo.heroi.get_nome()}\n"
            f"Vida: {self.jogo.heroi.get_vida()}\n"
            f"Nível: {self.jogo.heroi.get_nivel()}\n"
            f"Energia: {self.jogo.heroi.get_energia()}"
        )
        self.label_heroi_status.config(text=status_heroi)
        
        # Atualiza status do inimigo
        if self.jogo.inimigo:
            status_inimigo = (
                f"Nome: {self.jogo.inimigo.get_nome()}\n"
                f"Vida: {self.jogo.inimigo.get_vida()}\n"
                f"Nível: {self.jogo.inimigo.get_nivel()}\n"
                f"Tipo: {self.jogo.inimigo.get_tipo()}"
            )
            self.label_inimigo_status.config(text=status_inimigo)
    
    def adicionar_log(self, mensagem):
        self.text_log.insert(tk.END, mensagem + "\n")
        self.text_log.see(tk.END)
    
    def iniciar_batalha(self):
        if self.jogo.proximo_inimigo():
            self.adicionar_log(f"\nNovo inimigo apareceu: {self.jogo.inimigo.get_nome()}!")
            self.atualizar_status()
        else:
            messagebox.showinfo("Fim de Jogo", "Parabéns! Você venceu todos os inimigos!")
            self.janela.quit()
    
    def verificar_fim_batalha(self):
        if self.jogo.heroi.get_vida() <= 0:
            messagebox.showinfo("Fim de Jogo", "Você foi derrotado!")
            self.janela.quit()
        elif self.jogo.inimigo.get_vida() <= 0:
            self.adicionar_log(f"\nVocê derrotou {self.jogo.inimigo.get_nome()}!")
            self.jogo.heroi._personagem__nivel += 1
            self.jogo.heroi._personagem__vida = 100
            self.jogo.heroi._heroi__energia = 50
            self.adicionar_log(f"Seu herói subiu para o nível {self.jogo.heroi.get_nivel()}!")
            self.iniciar_batalha()
    
    def acao_inimigo(self):
        import random
        if self.jogo.inimigo.get_vida() > 0:
            acao = random.randint(1, 4)
            if acao == 1:
                self.jogo.inimigo.atacar(self.jogo.heroi)
            elif acao == 2:
                self.jogo.inimigo.ataqueFurtivo(self.jogo.heroi)
            elif acao == 3:
                self.jogo.inimigo.investidaPoderosa(self.jogo.heroi)
            else:
                self.jogo.inimigo.regenerarEnergia()
            self.atualizar_status()
    
    # Métodos para as ações do jogador
    def ataque_normal(self):
        self.jogo.heroi.atacar(self.jogo.inimigo)
        self.adicionar_log(f"{self.jogo.heroi.get_nome()} usou Ataque Normal!")
        self.atualizar_status()
        self.acao_inimigo()
        self.verificar_fim_batalha()
    
    def ataque_especial(self):
        self.jogo.heroi.ataqueEspecial(self.jogo.inimigo)
        self.adicionar_log(f"{self.jogo.heroi.get_nome()} usou Ataque Especial!")
        self.atualizar_status()
        self.acao_inimigo()
        self.verificar_fim_batalha()
    
    def ataque_critico(self):
        self.jogo.heroi.ataqueCritico(self.jogo.inimigo)
        self.adicionar_log(f"{self.jogo.heroi.get_nome()} usou Ataque Crítico!")
        self.atualizar_status()
        self.acao_inimigo()
        self.verificar_fim_batalha()
    
    def curar(self):
        self.jogo.heroi.curar()
        self.adicionar_log(f"{self.jogo.heroi.get_nome()} usou Cura!")
        self.atualizar_status()
        self.acao_inimigo()
        self.verificar_fim_batalha()
    
    def regenerar(self):
        self.jogo.heroi.regenerarEnergia()
        self.adicionar_log(f"{self.jogo.heroi.get_nome()} regenerou energia!")
        self.atualizar_status()
        self.acao_inimigo()
        self.verificar_fim_batalha()
    
    def iniciar(self):
        self.janela.mainloop()

if __name__ == "__main__":
    interface = InterfaceJogo()
    interface.iniciar()
