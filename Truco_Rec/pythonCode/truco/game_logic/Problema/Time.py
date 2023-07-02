#!/usr/bin/python
# -*- coding: UTF-8 -*-
from truco.game_logic.Problema import Jogador

class Time(object):
	def pegarPontuacao(self): 
		"""@ParamType aTime Problema.Time
		@ReturnType int"""
		return self._pontuacao

	def ZerarPlacar(self):
		self._pontuacao = 0

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

