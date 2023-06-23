#!/usr/bin/python
# -*- coding: UTF-8 -*-
from truco.game_logic.Problema import Carta
from truco.game_logic.Problema import Time
from truco.game_logic.Problema import Baralho
import random

class Jogador():

	def verificarTurno(self):
		"""@ReturnType boolean"""
		pass

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

		sequencia = [4,5,6,7,'J','Q','K','A',2,3]

		vira = baralho[0].valor

		manilha = (sequencia.index(vira)+1) % 10

		carta_retorno = Carta(manilha,'X')

		return carta_retorno

	def selecionarCarta(self, aCarta):
		"""@ParamType aCarta Problema.Carta"""
		pass

	def verificarTrucoAndamento(self):
		"""@ReturnType boolean"""
		pass

	def removerCartaMao(self, aCarta):
		"""@ParamType aCarta Problema.Carta"""
		pass

	def passarTurno(self):
		pass

	def ehUltimo(self, *aOrdem):
		"""@ParamType aOrdem Problema.Jogador*
		@ReturnType boolean"""
		pass

	def respondeTruco(self):
		"""@ReturnType boolean"""
		pass

	def RegistrarNome(self, nome):
		"""@ParamType aNome string"""
		self._nome = nome
		pass

	def DefinirDealer(self): #!! mudar diagrama de algoritmo
		self._dealer = True
		return True

	def PegarTime(self):
		"""@ReturnType int"""
		pass

	def __init__(self,nome,position): #!! não sei exatamente como se modelo o init, dar uma olhada no exemplo do Ricardo
		self._nome = nome
		"""@AttributeType string"""
		self._seuTurno = None
		"""@AttributeType boolean"""
		self._mao = []
		"""@AttributeType Problema.Carta*"""
		self._dealer = False
		"""@AttributeType boolean"""
		self._time = None

		self._position = position

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
		self._unnamed_Mesa_2 = None
		"""@AttributeType Problema.Mesa
		# @AssociationType Problema.Mesa"""

