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

		
		diretorio_atual = os.path.dirname(os.path.abspath(__file__))
		diretorio_pai = os.path.dirname(diretorio_atual)
		self.diretorio_imagens = os.path.join(diretorio_pai,"images")
	
	def get_foto_carta(self): 
		nome_imagem = str(self._valor) + '_' + str(self._naipe) + ".png"
		file=os.path.join(self.diretorio_imagens, nome_imagem)
		imagem = ImageTk.PhotoImage(Image.open(file).resize((61,95)))
		self._imagem = imagem 
		

		

