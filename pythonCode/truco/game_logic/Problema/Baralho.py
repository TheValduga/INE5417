#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Problema import Carta
from Problema import Mesa
import random

class Baralho(object):
	def embaralharCartas(self):
		"""@ReturnType Problema.Baralho"""
		baralho_aux = self._cartas #!! no diagrama de algoritmo ta como self.Cartas ao invés de self._cartas
		
		baralho_resultado = []

		for i in range(0,len(self._cartas)):
			indice = random.randint(0,len(baralho_aux)-1)
			item = baralho_aux.pop(indice)
			baralho_resultado.append(item)
		
		self._cartas = baralho_resultado
		
		return baralho_resultado


	# !! metodo adicionado depois, ATUALIZAR PROJETO
	def instanciarCartas(self):# metodo incompleto
		pass


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

