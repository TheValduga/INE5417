#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Problema import Carta
from Problema import Time
from Problema import Mesa
from Problema import Baralho

class Jogador(object):
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

	def definirManilha(self, aBaralho):
		"""@ParamType aBaralho Problema.Baralho
		@ReturnType Problema.Carta"""
		pass

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

	def RegistrarNome(self, aNome):
		"""@ParamType aNome string"""
		pass

	def DefinirDealer(self):
		pass

	def PegarTime(self):
		"""@ReturnType int"""
		pass

	def __init__(self):
		self._nome = None
		"""@AttributeType string"""
		self._seuTurno = None
		"""@AttributeType boolean"""
		self._mao = None
		"""@AttributeType Problema.Carta*"""
		self._dealer = None
		"""@AttributeType boolean"""
		self._time = None
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

