#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import simpledialog
import os
from py_netgames_client.tkinter_client.PyNetgamesServerProxy import PyNetgamesServerProxy
from py_netgames_client.tkinter_client.PyNetgamesServerListener import PyNetgamesServerListener

class PlayerInterface(PyNetgamesServerListener):

	def __init__(self):
		self.main_window = Tk()
		self.main_window.title("Truco")
		self.main_window.geometry("1366x768")

		self.fill_main_window()
		
		#!! esse porre precisa botar nos diagramas? 
		#!! variavel temporaria auxiliar porra, pelo amor de deus né
		diretorio_atual = os.path.dirname(os.path.abspath(__file__))
		diretorio_pai = os.path.dirname(diretorio_atual)
		diretorio_imagens = os.path.join(diretorio_pai,"images")
		print(self.SolicitarNomeJogador())


		self._back_card = PhotoImage(file=os.path.join(diretorio_imagens,"back_card2.png"))
		
		"""@AttributeType TKinter.PhotoImage"""
		self._front_card = None
		"""@AttributeType TKinter.PhotoImage"""
		self._card_deck = None
		"""@AttributeType TKinter.PhotoImage"""
		self._logo_label = None
		"""@AttributeType TKinter.Label"""
		self._botao_aceitar = None
		"""@AttributeType TKinter.Button"""
		self._botao_aumentar = None
		"""@AttributeType TKinter.Button"""
		self._botao_correr = None
		"""@AttributeType TKinter.Button"""
		self._botao_truco = None
		"""@AttributeType TKinter.Button"""
		self._unnamed_PhotoImage_ = None
		"""@AttributeType TKinter.PhotoImage
		# @AssociationType TKinter.PhotoImage
		# @AssociationKind Aggregation"""
		self._unnamed_Label_ = None
		"""@AttributeType TKinter.Label
		# @AssociationType TKinter.Label
		# @AssociationKind Aggregation"""
		self._unnamed_Frame_ = None
		"""@AttributeType TKinter.Frame
		# @AssociationType TKinter.Frame
		# @AssociationKind Aggregation"""
		self._unnamed_Tk_ = None
		"""@AttributeType TKinter.Tk
		# @AssociationType TKinter.Tk
		# @AssociationKind Aggregation"""
		self._unnamed_Mesa_ = None
		"""@AttributeType Problema.Mesa
		# @AssociationType Problema.Mesa
		# @AssociationKind Aggregation"""
		self._unnamed_Button_ = None
		"""@AttributeType TKinter.Button
		# @AssociationType TKinter.Button
		# @AssociationKind Aggregation"""
		self._unnamed_Tk_2 = None
		"""@AttributeType TKinter.Tk
		# @AssociationType TKinter.Tk
		# @AssociationKind Aggregation"""
		self._unnamed_Frame_2 = []
		"""@AttributeType TKinter.Frame*
		# @AssociationType TKinter.Frame[]
		# @AssociationMultiplicity 6
		# @AssociationKind Aggregation"""
		self._unnamed_Label_2 = None
		"""@AttributeType TKinter.Label
		# @AssociationType TKinter.Label
		# @AssociationKind Aggregation"""
		self._unnamed_PhotoImage_2 = []
		"""@AttributeType TKinter.PhotoImage*
		# @AssociationType TKinter.PhotoImage[]
		# @AssociationMultiplicity 3
		# @AssociationKind Aggregation"""
		self._unnamed_Button_2 = []
		"""@AttributeType TKinter.Button*
		# @AssociationType TKinter.Button[]
		# @AssociationMultiplicity 4
		# @AssociationKind Aggregation"""

		self.main_window.mainloop()

	def fill_main_window(self):
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

	def mostra_mensagem(self, aMensagem):
		"""@ParamType aMensagem string
		@ReturnType void"""
		pass

	def clicarBotao(self, aJogador):
		pass

	def exibirNotificacaoInicioMao(self):
		pass

	def enviarPedidoTruco(self):
		pass

	def notificarNaoEhTurno(self):
		pass

	def notificarTrucoAndamento(self):
		pass

	def exibirNovoEstado(self):
		pass

	def atualizaTopo(self, aMonte_cartaForte_):
		"""@ParamType aMonte_cartaForte_ Problema.Carta"""
		pass

	def exibirCarta(self, aCarta):
		"""@ParamType aCarta Problema.Carta"""
		pass

	def exibirMesa(self, aMesa):
		"""@ParamType aMesa Problema.Mesa"""
		pass

	def receberJogada(self, aJogada):
		"""@ParamType aJogada Dict{ string, any }"""
		pass

	def exibirAguardandoResposta(self):
		pass

	def exibirRespostaTruco(self, aResposta):
		pass

	def clicarCarta(self):
		"""@ReturnType Problema.Carta"""
		pass

	def SolicitarNomeJogador(self):
		"""@ReturnType string"""
		input_usuario = simpledialog.askstring("Solicitacao de Nome", "Digite seu nome: ")
		if input_usuario == "":
			return "Sem nome"
		else:
			return input_usuario

	def Notificar(self, aMensagem):
		"""@ParamType aMensagem string"""
		pass

	def set_match_id(self, match_id): # !! ATUALIZAR : botar match_id como atributo da classe playerinterface
		"""@ParamType aMatch_id string"""
		self._match_id = match_id
		pass

	def AtualizarInterface(self):
		pass

	def clicarBotao(self):
		pass

	def responderTruco(self, aResposta):
		"""@ParamType aResposta string"""
		pass

	def reset(self):
		pass

	def enviarAtualizacaoPartida(self, aNovoEstado):
		pass

	def ClicarBotaoTruco(self):
		pass

	def botaoResposta(self):
		pass

	def add_listener(self):		# Pyng use case "add listener"
		self.server_proxy = PyNetgamesServerProxy()
		self.server_proxy.add_listener(self)

	def send_connect(self):	# Pyng use case "send connect"
		self.server_proxy.send_connect("wss://py-netgames-server.fly.dev")

	def send_match(self, amount_of_players):	# Pyng use case "send match"
		self.server_proxy.send_match(amount_of_players) #4 = quantidade de jogadores.

	def receive_connection_success(self):	# Pyng use case "receive connection"
		print('*************** CONECTADO *******************')
		print("VAI SE FUDER VAI SE FUDER VAI SE FUDER")
		self.send_match()

	def receive_disconnect(self):	# Pyng use case "receive disconnect"
		pass
			
	def receive_error(self, error):	# Pyng use case "receive error"
		pass

	def receive_match(self, match):	# Pyng use case "receive match"
		print('*************** PARTIDA INICIADA *******************')
		print('*************** ORDEM: ', match.position)
		print('*************** match_id: ', match.match_id)
		self.set_match_id(match.match_id)

	def receive_move(self, move):	# Pyng use case "receive move"
		pass

