#!/usr/bin/python
# -*- coding: UTF-8 -*-
from truco.game_logic.Problema import Jogador

class Time(object):
	def registrarTimeCarta(self, aJogador):
		"""@ParamType aJogador Problema.Jogador
		@ReturnType Problema.Time"""
		pass

	def pegarPontuacao(self, time):
		"""@ParamType aTime Problema.Time
		@ReturnType int"""
		return time._pontuacao

	def verificarRodadasTime(self):
		"""@ReturnType int"""
		pass

	def registraMaoEncerrada(self, encerrada):
		"""@ParamType aEncerrada boolean"""
		self._unnamed_Mesa_.registraMaoEncerrada(encerrada)

	def ZerarPlacar(self):
		self._pontuacao = 0

	def setarPontuacao(self, pontos):
		"""@ParamType aPontos int"""
		self._pontuacao = pontos

	def __init__(self, id):
		self._identificacao = id
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

