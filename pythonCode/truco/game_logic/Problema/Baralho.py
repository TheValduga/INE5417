#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Problema import Carta
from Problema import Mesa

class Baralho(object):
	def embaralharCartas(self):
		"""@ReturnType Problema.Baralho"""
		pass

	# !! metodo adicionado depois, ATUALIZAR PROJETO
	def instanciarCartas(self):
		# metodo incompleto
  		naipes = ['paus', 'copas', 'espadas', 'ouros']
		for i in range(1,11):
			for j in naipes:
				Carta(i,j)

	def __init__(self):
		self._cartas = self.instanciarCartas()
		"""@AttributeType Problema.Carta"""
		self._unnamed_Mesa_ = None
		"""@AttributeType Problema.Mesa
		# @AssociationType Problema.Mesa"""
		self._unnamed_Carta_ = []
		"""@AttributeType Problema.Carta*
		# @AssociationType Problema.Carta[]
		# @AssociationMultiplicity 40
		# @AssociationKind Aggregation"""

