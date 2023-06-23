#!/usr/bin/python
# -*- coding: UTF-8 -*-

from tkinter import PhotoImage
from PIL import ImageTk, Image #problema com biblioteca por causa do nojo do venv, cometa suícidio imediatamente
import os
class Carta():
	def __init__(self, valor, naipe):
		self._valor = valor
		"""@AttributeType int"""
		self._naipe = naipe
		"""@AttributeType string"""

		self._unnamed_Jogador_ = None
		"""@AttributeType Problema.Jogador
		# @AssociationType Problema.Jogador"""
		
		#
		self._unnamed_Baralho_ = None
		"""@AttributeType Problema.Baralho
		# @AssociationType Problema.Baralho"""

		#!! TUDO DAQUI PRA BAIXO TEM QUE BOTAR EU IMAGINO (pelo menos os com self eu acho)
		diretorio_atual = os.path.dirname(os.path.abspath(__file__))
		diretorio_pai = os.path.dirname(diretorio_atual)
		self.diretorio_imagens = os.path.join(diretorio_pai,"images")
		self.coords = [
			(0,0,124,193),
			(124,0,248,193),
			(248,0,372,193),
			(372,0,496,193),
			(496,0,620,193)
		]
	
	def get_foto_carta(self): #!! além de adicionar nos diagramas, ver se escrevi o nome dos arquivos perfeitamente
		if self._valor == 1:
			if self._naipe == 'paus':
				imagem = PhotoImage(self.diretorio_imagens,'1_paus.png')
		
		return imagem

		

