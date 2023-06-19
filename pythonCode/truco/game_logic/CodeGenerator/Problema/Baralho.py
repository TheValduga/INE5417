#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Problema import Carta
from Problema import Mesa

class Baralho(object):
	def embaralharCartas(self):
		"""@ReturnType Problema.Baralho"""
		pass

	def __init__(self):
		self._cartas = None
		"""@AttributeType Problema.Carta"""
		self._unnamed_Mesa_ = None
		"""@AttributeType Problema.Mesa
		# @AssociationType Problema.Mesa"""
		self._unnamed_Carta_ = []
		"""@AttributeType Problema.Carta*
		# @AssociationType Problema.Carta[]
		# @AssociationMultiplicity 40
		# @AssociationKind Aggregation"""

