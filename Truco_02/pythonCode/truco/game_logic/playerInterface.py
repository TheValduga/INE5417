from tkinter import *
import os
from py_netgames_client.tkinter_client.PyNetgamesServerProxy import PyNetgamesServerProxy
from py_netgames_client.tkinter_client.PyNetgamesServerListener import PyNetgamesServerListener

class PlayerInterface(PyNetgamesServerListener):
  def __init__(self):
    self.main_window = Tk()
    self.main_window.title("Truco")
    self.main_window.geometry("1366x768")
    # self.main_window.attributes("-fullscreen", True)
    # self.main_window.resizable(False, False)
    self.main_window["bg"]="#046307"

    # # Frame da mesa do jogo
    # self.board_frame = Frame(self.main_window, padx=100, pady=25, bg="red")
    # self.board_frame.grid(row=0 , column=0)

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

    # Imagem verso da carta
    self.back_card = PhotoImage(file=os.path.join(os.path.dirname(__file__),"images/back_card2.png")) 
    self.front_card = PhotoImage(file=os.path.join(os.path.dirname(__file__),"images/a-espada.png")) 
    self.card_deck = PhotoImage(file=os.path.join(os.path.dirname(__file__), "images/card_deck.png")) 

    # Nome do jogador
    self.logo_label = Label(self.player1_frame, text='Gustavo', font="arial 24", bg="#046307")
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
    self.logo_label = Label(self.player2_frame, text='Lucas', font="arial 24", bg="#046307")
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
    self.logo_label = Label(self.player3_frame, text='Maria', font="arial 24", bg="#046307")
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
    # canvas = Canvas(self.mesa_frame, bg="#046307", width=200, height=100)
    # canvas.pack()
    # canvas.create_image(100,50,image=self.card_deck)
    self.logo_label.grid(row=0, column=1)
    self.logo_label = Label(self.mesa_frame, bd = 0, image=self.front_card)
    self.logo_label.grid(row=0, column=2)

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
    
    # truco.pack(side = BOTTOM)
    # valeSeis.pack(side = BOTTOM)
    # valeNove.pack(side = BOTTOM)
    # valeDoze.pack(side = BOTTOM)

    # self.fill_main_window()

  #----------------------- Pynetgames ----------------------------------->
    self.add_listener()
    self.send_connect()
  #<----------------------- Pynetgames ----------------------------------

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

#----------------------- Pynetgames ----------------------------------

  def add_listener(self):		# Pyng use case "add listener"
    self.server_proxy = PyNetgamesServerProxy()
    self.server_proxy.add_listener(self)

  def send_connect(self):	# Pyng use case "send connect"
    self.server_proxy.send_connect("wss://py-netgames-server.fly.dev")

  def send_match(self):	# Pyng use case "send match"
    self.server_proxy.send_match(4) #4 = quantidade de jogadores.

  def receive_connection_success(self):	# Pyng use case "receive connection"
    print('*************** CONECTADO *******************')
    self.send_match()

  def receive_disconnect(self):	# Pyng use case "receive disconnect"
    pass
		
  def receive_error(self, error):	# Pyng use case "receive error"
    pass

  def receive_match(self, match):	# Pyng use case "receive match"
    print('*************** PARTIDA INICIADA *******************')
    print('*************** ORDEM: ', match.position)
    print('*************** match_id: ', match.match_id)

  def receive_move(self, move):	# Pyng use case "receive move"
    pass