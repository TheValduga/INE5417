from email import message
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from turtle import color
from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor

class PlayerInterface(DogPlayerInterface):
  def __init__(self):
    self.main_window = Tk()
    self.main_window.title("Truco")
    self.main_window.geometry("1366x768")
    # self.main_window.attributes("-fullscreen", True)
    # self.main_window.resizable(False, False)
    self.main_window["bg"]="#046307"

    # Frame das cartas do jogador
    self.player1_frame = Frame(self.main_window, padx=150, pady=20, bg="#046307")
    self.player1_frame.grid(row=2, column=1)
        
    self.player2_frame = Frame(self.main_window, padx=10, pady=20, bg="#046307")
    self.player2_frame.grid(row=1, column=0)
    
    self.player3_frame = Frame(self.main_window, padx=150, pady=20, bg="#046307")
    self.player3_frame.grid(row=0, column=1)
    
    self.player4_frame = Frame(self.main_window, padx=10, pady=20, bg="#046307")
    self.player4_frame.grid(row=1, column=2)
    
    self.mesa_frame = Frame(self.main_window, padx=150, pady=80, bg="#046307")
    self.mesa_frame.grid(row=1, column=1)
    
    self.placar_frame = Frame(self.main_window, padx=30, pady=30, bg="#046307")
    self.placar_frame.grid(row=0, column=0)
    
    self.start_frame = Frame(self.main_window, padx=480, pady=250, bg="#046307")
    self.start_frame.grid(row=0, column=0)

    self.allFrames = [self.player1_frame, self.player2_frame, self.player3_frame, self.player4_frame, self.mesa_frame, self.placar_frame, self.start_frame]

    # Imagem verso da carta
    self.back_card = PhotoImage(file="images/back_card2.png") 
    self.front_card = PhotoImage(file="images/a-espada.png") 
    self.card_deck = PhotoImage(file="images/card_deck.png") 

    # Nome do jogador
    self.logo_label = Label(self.player1_frame, text='José', font="arial 24", bg="#046307")
    self.logo_label.grid(row=0, column=3)

    # Imagem das cartas dos jogador 1

    self.botao_correr = Button(self.player1_frame, bd = 3, text="Correr", command=self.correr)
    self.botao_correr.grid(row=1, column=0)

    self.botao_aumentar = Button(self.player1_frame, bd = 3, text="Aumentar", command=self.aumentar)
    self.botao_aumentar.grid(row=1, column=1)

    self.cartas_viradas = Button(self.player1_frame, bd = 3, image=self.front_card)
    self.cartas_viradas.grid(row=1, column=2)

    self.cartas_viradas1 = Button(self.player1_frame, bd = 3, image=self.front_card)
    self.cartas_viradas1.grid(row=1, column=3)

    self.cartas_viradas2 = Button(self.player1_frame, bd = 3, image=self.front_card)
    self.cartas_viradas2.grid(row=1, column=4)

    self.botao_truco = Button(self.player1_frame, bd = 3, text="Truco", command=self.truco)
    self.botao_truco.grid(row=1, column=5)

    self.botao_aceitar = Button(self.player1_frame, bd = 3, text="Aceitar", command=self.aceitar)
    self.botao_aceitar.grid(row=1, column=6)


    # Nome do jogador
    self.logo_label = Label(self.player2_frame, text='Valduga', font="arial 24", bg="#046307")
    self.logo_label.grid(row=0, column=1)

    # Imagem das cartas dos oponentes viradas para baixo
    self.cartas_viradas = Label(self.player2_frame, bd = 0, image=self.back_card)
    self.cartas_viradas.grid(row=1, column=0)

    self.cartas_viradas1 = Label(self.player2_frame, bd = 0, image=self.back_card)
    self.cartas_viradas1.grid(row=1, column=1)

    self.cartas_viradas2 = Label(self.player2_frame, bd = 0, image=self.back_card)
    self.cartas_viradas2.grid(row=1, column=2)

    # Nome do jogador
    self.logo_label = Label(self.player4_frame, text='Ricardo', font="arial 24", bg="#046307")
    self.logo_label.grid(row=0, column=1)

    # Imagem das cartas dos oponentes viradas para baixo
    self.cartas_viradas = Label(self.player4_frame, bd = 0, image=self.back_card)
    self.cartas_viradas.grid(row=1, column=0)

    self.cartas_viradas1 = Label(self.player4_frame, bd = 0, image=self.back_card)
    self.cartas_viradas1.grid(row=1, column=1)

    self.cartas_viradas2 = Label(self.player4_frame, bd = 0, image=self.back_card)
    self.cartas_viradas2.grid(row=1, column=2)

    # Nome do jogador
    self.logo_label = Label(self.player3_frame, text='Pagotto', font="arial 24", bg="#046307")
    self.logo_label.grid(row=0, column=1)

    # Imagem das cartas dos oponentes viradas para baixo
    self.cartas_viradas = Label(self.player3_frame, bd = 0, image=self.back_card)
    self.cartas_viradas.grid(row=1, column=0)

    self.cartas_viradas1 = Label(self.player3_frame, bd = 0, image=self.back_card)
    self.cartas_viradas1.grid(row=1, column=1)

    self.cartas_viradas2 = Label(self.player3_frame, bd = 0, image=self.back_card)
    self.cartas_viradas2.grid(row=1, column=2)

    # Mesa frame
    self.logo_label = Label(self.mesa_frame, bd = 0, image=self.front_card)
    self.logo_label.grid(row=0, column=0)
    self.logo_label = Label(self.mesa_frame, bd = 0, image=self.card_deck)
    self.logo_label.grid(row=0, column=1)
    self.logo_label = Label(self.mesa_frame, bd = 0, image=self.front_card)
    self.logo_label.grid(row=0, column=2)
    self.start_match_button = Button(self.start_frame, bd = 3, text="Iniciar Partida", command=self.start_match, width=50, height=10)
    self.start_match_button.grid(row=1, column=0)

    #Tela inicial
    self.titulo_label = Label(self.start_frame, text='TRUCO', font="arial 24", bg="#046307")
    self.titulo_label.grid(row=0, column=0)

    # Placar frame
    self.titulo_label = Label(self.placar_frame, text='Score', font="arial 24", bg="#046307")
    self.titulo_label.grid(row=0, column=1)

    self.time_azul_label = Label(self.placar_frame, text='Time Azul - 0', font="arial 20", fg="blue", bg="#046307")
    self.time_azul_label.grid(row=1, column=1)
    self.time_vermelho_label = Label(self.placar_frame, text='Time Vermelho - 0', font="arial 20", fg="red", bg="#046307")
    self.time_vermelho_label.grid(row=2, column=1)

    truco = Button(self.main_window,text = "Truco", command=self.truco) 
    valeSeis = Button(self.main_window,text = "Vale seis", command=self.valeSeis)
    valeNove = Button(self.main_window,text = "Vale nove", command=self.valeNove)
    valeDoze = Button(self.main_window,text = "Vale doze", command=self.valeDoze)

    player_name = simpledialog.askstring(title="Player identification", prompt="What is your name?")
    self.dog_server_interface = DogActor()
    message = self.dog_server_interface.initialize(player_name, self)
    messagebox.showinfo(message=message)


    self.main_window.mainloop() # abrir a janela

  def truco(self):
    print("Truco")

  def valeSeis(self):
    print("Vale seis")

  def valeNove(self):
    print("Vale nove")

  def valeDoze(self):
    print("Vale doze")

  def aceitar(self):
    print("Aceito!")

  def correr(self):
    print("Corro!")

  def aumentar(self):
    print("Aumento os pontos!")

  def start_match(self):
    start_status = self.dog_server_interface.start_match(2)
    message = start_status.get_message()
    messagebox.showinfo(message=message)
    if(start_status.code == '2'):
      self.start_frame.destroy()
    
  def receive_start(self, start_status):
    message = start_status.get_message()
    messagebox.showinfo(message=message)
    if(start_status.code == '2'):
      self.start_frame.destroy()