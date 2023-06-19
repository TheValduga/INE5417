#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Problema import Mesa
from TKinter import Frame
from TKinter import PhotoImage
from TKinter import Label
from TKinter import Button
from TKinter import Tk
from Problema import Carta
import MatchStartedMessage
import MoveMessage
import PyNetgamesServerListener

class PlayerInterface(PyNetgamesServerListener):
	def PlayerInterface(self):
		pass

	def __init__(self):
		self._main_window = None
		"""@AttributeType Problema.Mesa"""
		self._player1_frame = None
		"""@AttributeType TKinter.Frame"""
		self._player2_frame = None
		"""@AttributeType TKinter.Frame"""
		self._player3_frame = None
		"""@AttributeType TKinter.Frame"""
		self._player4_frame = None
		"""@AttributeType TKinter.Frame"""
		self._mesa_frame = None
		"""@AttributeType TKinter.Frame"""
		self._placar_frame = None
		"""@AttributeType TKinter.Frame"""
		self._back_card = None
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

	def fill_main_window(self):
		pass

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
		pass

	def add_listener(self):
		pass

	def send_connect(self):
		pass

	def Notificar(self, aMensagem):
		"""@ParamType aMensagem string"""
		pass

	def send_match(self, aAmount_of_players):
		"""@ParamType aAmount_of_players int"""
		pass

	def set_match_id(self, aMatch_id):
		"""@ParamType aMatch_id string"""
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

	def receive_connection_succes(self):
		""""""@ReturnType void"""
		@ReturnType void"""
		pass

	def receive_match(self, aMatch):
		""""""@ParamType aMatch MatchStartedMessage
		@ReturnType void"""
		@ParamType aMatch MatchStartedMessage
		@ReturnType void"""
		pass

	def receive_move(self, aReceive_move):
		""""""@ParamType aReceive_move MoveMessage
		@ReturnType void"""
		@ParamType aReceive_move MoveMessage
		@ReturnType void"""
		pass

	def receive_error(self, aError):
		""""""@ParamType aError Exception
		@ReturnType void"""
		@ParamType aError Exception
		@ReturnType void"""
		pass

	def receive_disconnect(self):
		""""""@ReturnType void"""
		@ReturnType void"""
		pass

