#!/usr/bin/python
# -*- coding: UTF-8 -*-
from truco.game_logic.Problema.Carta import Carta
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


	# !! metodo adicionado depois, ATUALIZAR PROJETO -> diagrama de sequência do initialize por exemplo
	def instanciarCartas(self):
		baralho_aux = []
		valores = [4,5,6,7,'J','Q','K',1,2,3] #!! troquei 'A' pra 1. baralho espanhol representa por numero não por valete e os cacete. Mudar diagrama e pdf ou mudar aqui e nome dos arquivos de imagem de 1_(naipe).png pra A_(naipe).png
		naipes = ["paus","copa","espada","ouro"] #!! a maioria aqui ta escrito no singular, nos diagramas e no pdf acho que estão todos no plural, ou muda o nome de todos os arquivos pra plural ou muda os diagramas
		for valor in valores:
			for naipe in naipes:
				carta = Carta(valor,naipe)
				baralho_aux.append(carta)
		
		return baralho_aux
	



	def __init__(self):
		self._cartas = self.instanciarCartas()
		"""@AttributeType Problema.Carta"""

		#!! acho que esses atributos aqui são inuteis ou redundantes. Remover dos diagramas depois
		self._unnamed_Mesa_ = None
		"""@AttributeType Problema.Mesa
		# @AssociationType Problema.Mesa"""
		self._unnamed_Carta_ = []
		"""@AttributeType Problema.Carta*
		# @AssociationType Problema.Carta[]
		# @AssociationMultiplicity 40
		# @AssociationKind Aggregation"""

