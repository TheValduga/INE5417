#!/usr/bin/python
# -*- coding: UTF-8 -*-
from truco.game_logic.Problema.Carta import Carta
import random

class Baralho(object):
	def embaralharCartas(self):
		"""@ReturnType Problema.Baralho"""
		baralho_aux = self._cartas 
		
		baralho_resultado = []

		for i in range(0,len(self._cartas)):
			indice = random.randint(0,len(baralho_aux)-1)
			item = baralho_aux.pop(indice)
			baralho_resultado.append(item)
		
		self._cartas = baralho_resultado

	
	def instanciarCartas(self):
		baralho_aux = []
		valores = [4,5,6,7,'J','Q','K',1,2,3] 
		naipes = ["paus","copa","espada","ouro"] 
		for valor in valores:
			for naipe in naipes:
				carta = Carta(valor,naipe)
				baralho_aux.append(carta)
		
		return baralho_aux
	
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

