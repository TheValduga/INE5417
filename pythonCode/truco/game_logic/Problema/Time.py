#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Problema import Jogador
from Problema import Mesa

class Time(object):
	def registrarTimeCarta(self, aJogador):
		"""@ParamType aJogador Problema.Jogador
		@ReturnType Problema.Time"""
		pass

	def pegarPontuacao(self, aTime):
		"""@ParamType aTime Problema.Time
		@ReturnType int"""
		pass

	def verificarRodadasTime(self):
		"""@ReturnType int"""
		pass

	def registraMaoEncerrada(self, aEncerrada):
		"""@ParamType aEncerrada boolean"""
		pass

	def ZerarPlacar(self):
		pass

	def setarPontuacao(self, aPontos):
		"""@ParamType aPontos int"""
		pass

	def __init__(self):
		self._identificacao = None
		"""@AttributeType int"""
		self._pontuacao = None
		"""@AttributeType int"""
		self._jogadores = None
		"""@AttributeType Problema.Jogador"""
		self._unnamed_Mesa_ = None
		"""@AttributeType Problema.Mesa
		# @AssociationType Problema.Mesa"""
		self._unnamed_Jogador_ = None
		"""@AttributeType Problema.Jogador
		# @AssociationType Problema.Jogador
		# @AssociationKind Aggregation"""
