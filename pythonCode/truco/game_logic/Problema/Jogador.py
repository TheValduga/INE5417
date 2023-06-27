#!/usr/bin/python
# -*- coding: UTF-8 -*-
from truco.game_logic.Problema.Carta import Carta
from truco.game_logic.Problema.Time import Time
from truco.game_logic.Problema.Baralho import Baralho
import random

class Jogador():

	def verificarTurno(self):
		"""@ReturnType boolean"""
		return self._seuTurno

	def clicarBotao(self):
		pass

	def definirOrdem(self):
		"""@ReturnType Problema.Jogador[]"""
		pass

	def distribuirCartas(self, aBaralho):
		"""@ParamType aBaralho Problema.Baralho
		@ReturnType Problema.Carta*"""
		pass

	def definirManilha(self, baralho):
		"""@ParamType aBaralho Problema.Baralho
		@ReturnType Problema.Carta"""

		sequencia = [4,5,6,7,'J','Q','K',1,2,3]

		vira = baralho._cartas[13]._valor # !! mudar diagrama de algoritmo

		manilha = sequencia[(sequencia.index(vira)+1) % 10]


		carta_retorno = Carta(manilha,'ouro')

		return carta_retorno

	def selecionarCarta(self, cartaIndex: int): # !! alterar nome e tipo de do argumento para int
		"""@ParamType aCarta Problema.Carta"""
		turno = self.verificarTurno()
		encerraMao = False
		encerraRodada = False
		encerraPartida = False
		
		if turno:
			truco = self._mesa.VerificarTrucoAndamento()
			if not truco:
				time = self._position % 2
				carta = self._mesa.ColocarNaMesa(time, cartaIndex, self) # !! adicionar argumento cartaIndex no
				encerraRodada = self._mesa.encerramentoRodada(self._position)
				if not encerraRodada:
					proximo = self._mesa.PassarTurno(self)
					novoEstado = {'rodadaEncerrada': encerraRodada, 'maoEncerrada': False,'jogoEncerrado': False, 'carta': carta, 'tipo' : 'carta', 'proximo' : proximo, 'monte':self._mesa._monte}
				else:
					encerraMao = self._mesa.encerramentoMao()
					if encerraMao[0]: #!! encerraMao é um array agora
						#encerraPartida = self._mesa.encerramentoPartida()
						
						pass
					
					proximo = self._mesa.PassarTurno(self)
					#self._mesa._monte.append(carta)
					self._mesa.registrarStatusRodada(False)
					self._mesa._PlayerInterface.Notificar("Nova Rodada Iniciada")
					registro_envio = self._mesa._registroRodada
					monte_envio = []
					self._mesa._monte = []
					self._mesa._topo = Carta(4,'ouro')
					self._mesa._PlayerInterface._topo = Carta(4,'ouro')
					if encerraMao[0]:
						self._mesa._registroRodada = []
						self._mesa._PlayerInterface._topo = Carta(4,"ouro")
					print("ESTOU ENVIANDO:")
					print(monte_envio)
					novoEstado = {'rodadaEncerrada': encerraRodada, 'maoEncerrada': encerraMao[0],'vencedor_mao':encerraMao[1], 'jogoEncerrado': encerraPartida, 'carta': carta, 'tipo' : 'carta', 'proximo' : proximo, 'monte':monte_envio, 'vencedor_rodada': registro_envio[-1],}
					self._mesa._PlayerInterface._topo = Carta(4,"ouro")
					self._mesa._PlayerInterface.AtualizarInterface()
					
				self._mesa._PlayerInterface.AtualizarInterface()
				self._mesa._PlayerInterface.enviarAtualizacaoPartida(novoEstado)
			else:
				self._mesa._PlayerInterface.Notificar('Truco em andamento')
		else:
			self._mesa._PlayerInterface.Notificar('Não é seu turno')

	def verificarTrucoAndamento(self):
		"""@ReturnType boolean"""
		pass

	def removerCartaMao(self, aCarta):
		"""@ParamType aCarta Problema.Carta"""
		pass

	def passarTurno(self):
		self._seuTurno = False
		return ((self._position + 1) % 4)

	def ehUltimo(self):
		"""@ReturnType boolean"""
		"""@ParamType ordem Problema.Jogador[]"""
		return self._position == 3


	def respondeTruco(self):
		"""@ReturnType boolean"""
		pass

	def RegistrarNome(self, nome):
		"""@ParamType aNome string"""
		self._nome = nome
		pass

	def DefinirDealer(self):
		self._dealer = True
		return True

	def PegarTime(self):
		"""@ReturnType int"""
		return self._time

	def __init__(self, mesa): #!! não sei exatamente como se modelou o init, dar uma olhada no exemplo do Ricardo
		self._nome = ''
		"""@AttributeType string"""
		self._seuTurno = False
		"""@AttributeType boolean"""
		self._mao = []
		"""@AttributeType Problema.Carta*"""
		self._dealer = False
		"""@AttributeType boolean"""
		self._time = None

		self._position = '' #!! atributo nao ta na modelagem

		"""@AttributeType int"""
		self._unnamed_Carta_ = []
		"""@AttributeType Problema.Carta*
		# @AssociationType Problema.Carta[]
		# @AssociationMultiplicity 3
		# @AssociationKind Aggregation"""
		self._unnamed_Time_ = []
		"""@AttributeType Problema.Time*
		# @AssociationType Problema.Time[]
		# @AssociationMultiplicity 2"""
		self._mesa = mesa
		"""@AttributeType Problema.Mesa
		# @AssociationType Problema.Mesa"""

