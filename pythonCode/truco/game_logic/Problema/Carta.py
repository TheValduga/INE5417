#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Problema import Baralho
from Problema import Jogador

class Carta(object):
	def __init__(self, valor, naipe):
		self._valor = valor
		"""@AttributeType int"""
		self._naipe = naipe
		"""@AttributeType string"""
		self._unnamed_Baralho_ = None
		"""@AttributeType Problema.Baralho
		# @AssociationType Problema.Baralho"""
		self._unnamed_Jogador_ = None
		"""@AttributeType Problema.Jogador
		# @AssociationType Problema.Jogador"""
