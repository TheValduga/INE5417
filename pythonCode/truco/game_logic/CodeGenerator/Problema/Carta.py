#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Problema import Baralho
from Problema import Jogador

class Carta(object):
	def __init__(self):
		self._valor = None
		"""@AttributeType int"""
		self._naipe = None
		"""@AttributeType string"""
		self._unnamed_Baralho_ = None
		"""@AttributeType Problema.Baralho
		# @AssociationType Problema.Baralho"""
		self._unnamed_Jogador_ = None
		"""@AttributeType Problema.Jogador
		# @AssociationType Problema.Jogador"""

