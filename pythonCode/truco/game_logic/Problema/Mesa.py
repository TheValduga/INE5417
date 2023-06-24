#!/usr/bin/python
# -*- coding: UTF-8 -*-
from truco.game_logic.Problema.Jogador import Jogador
from truco.game_logic.Problema.Baralho import Baralho
from truco.game_logic.Problema.Carta import Carta
from truco.game_logic.Problema.Time import Time
from truco.game_logic.TKinter import PlayerInterface
import random

class Mesa():

	def registrarTruco(self):
		"""@ReturnType boolean"""
		self._truco = not self._truco
		return self._truco

	def registrarMao(self):
		"""@ReturnType boolean"""
		self._maoAndamento = not(self._maoAndamento)
		return self._maoAndamento

	def registrarStatusRodada(self, status):
		"""@ParamType aStatus boolean"""
		self._rodadaAndamento = status
		return self._rodadaAndamento
		

	def registraPontoMao(self, aTime, aPontuacao):
		"""@ParamType aTime Problema.Time
		@ParamType aPontuacao int"""
		pass

	def definirOrdem(self):
		"""@ReturnType Problema.Jogador[]"""
		if self._ordemRodada == []:
			nova_ordem = self._jogadores #!! no Mesa definirOrdem tem que mudar isso aqui. lá ta self.ordem = self.jogadores | tem que ser nova_ordem = self._jogadores agora
		else:
			nova_ordem = [self._ordemRodada[1]] #!! tem que colocar os [ ] ao redor do self.ordem[1] no diagrama de algoritmo Mesa definirOrdem
			nova_ordem.append(self._ordemRodada[2]) #!! NOMES DIFERENTES NOS DIAGRAMAS TEM QUE MUDAR
			nova_ordem.append(self._ordemRodada[3])
			nova_ordem.append(self._ordemRodada[0])
		
		self._ordemRodada = nova_ordem #!! mudar nos diagramas (nomes)
		return self._ordemRodada

	def encerramentoPartida(self):
		"""@ReturnType boolean"""
		pass

	def definirPartidaAndamento(self, aBoolean):
		pass

	def registrarVencedor(self, aTime):
		"""@ParamType aTime Problema.Time"""
		pass

	def verificarRegistroRodadas(self):
		"""@ReturnType int*"""
		pass

	def verificarVencedorRodada(self, aRodada):
		"""@ParamType aRodada int
		@ReturnType Problema.Time"""
		pass

	def verificarEmpate(self):
		"""@ReturnType boolean"""
		pass

	def verificarRodadasEmpatadas(self):
		"""@ReturnType int*"""
		pass

	def nenhumTimePontua(self):
		pass

	def encerramentoRodada(self):
		encerrar = False
		cartaForte = self.comparaMonte()
		self.definirTopo(cartaForte)
		PlayerInterface.atualizarTopo(cartaForte)
		ordem = self.pegarOrdem()
		ehUltimo = self._jogadores.ehUltimo(ordem)
		if ehUltimo:
			pontuaRodada = self.vencedorRodada(self._monte, cartaForte)
			#!! TODO: acrescentar vetor registroRodadas
			qualrodada= self.verificaRodada()
			self.registrarRodada(qualrodada, pontuaRodada)
			encerrar = True
			self.registrarStatusRodada(False)
		return encerrar

	def encerramentoMao(self):
		pass
   
	def comparaMonte(self):
		"""@ReturnType int"""
		naipes = ['O', 'E', 'P', 'C']
		seq = ['4', '5', '6', '7', 'Q', 'J', 'K', 'A', '2', '3']
		cartaForte = Carta(4, 'O')
		for carta in self._monte:
			valorCarta = seq.index(carta.getValor())
			valorCartaForte = seq.index(cartaForte.getValor())
			naipeCarta = naipes.index(carta.getNaipe())
			naipeCartaForte = naipes.index(cartaForte.getNaipe())
			if valorCarta < valorCartaForte:
				return cartaForte
			elif valorCarta == valorCartaForte:
				if naipeCarta > naipeCartaForte:
					cartaForte = carta
					return cartaForte
				else:
					return cartaForte
			else:
				# valorCarta > valorCartaForte
				cartaForte = carta
				return cartaForte




	def definirTopo(self, aCartaForte):
		"""@ParamType aCartaForte int
		@ReturnType int"""
		pass

	def pegarOrdem(self):
		return self._ordemRodada

	def vencedorRodada(self, *aMonte, aCartaForte):
		"""@ParamType aMonte Problema.Carta*
		@ParamType aCartaForte int
		@ReturnType int"""
		pass

	def verificaRodada(self, *aRegistroRodadas):
		for rodada in aRegistroRodadas:
			if rodada == 0:
				# EMPATE
				return 0
			elif rodada == 1:
				# Time 1 venceu
				return 1
			elif rodada == 2:
				# Time 2 venceu
				return 2
			elif rodada == 3:
				# Rodada nao finalizada
				return 3

	def registrarRodada(self, aQualRodada, aVencedorRodada):
		self._registroRodada = aQualRodada
		self._registroRodada.append(aVencedorRodada)

	def trucoRespondido(self):
		"""@ReturnType boolean"""
		pass

	def registrarRespostaTruco(self, aValor):
		"""@ParamType aValor string"""
		pass

	def timeTrucou(self):
		"""@ReturnType Problema.Time"""
		pass

	def adicionarPontuacaoTime(self, aTime, aPontos):
		"""@ParamType aTime Problema.Time
		@ParamType aPontos int"""
		pass

	def aumentarValorMao(self):
		pass

	def clicarBotao(self, aJogador):
		"""@ParamType aJogador Problema.Jogador"""
		pass

	def IniciarPartida(self, jogador_local): #!!
		#self._jogadores = jogadores
		print("INICIANDO PARTIDA")
		self.DefinirTimes()
		print(jogador_local._position)
		self.EscolherDealer(jogador_local) #!! adicionar aos diagramas
		self._times[0].ZerarPlacar()
		self._times[1].ZerarPlacar()
		#self._baralho = Baralho() #!! isso não tem nos diagramas de Receive Match. Tem que ter

	def DefinirTimes(self): #!! no diagrama times é Time. Tem que ser um array de Time
		j = self._jogadores
		
		self._times[0]._jogadores = [j[0],j[2]]
		j[0]._time = 0
		j[2]._time = 0
		
		self._times[1]._jogadores = [j[1],j[3]]
		j[1]._time = 1
		j[3]._time = 1
		

	def EscolherDealer(self, jogador_local): #!! tive que mudar o algoritmo. Jogador DefinirDealer nos diagramas tem que virar Mesa EscolherDealer e fazer as alterações necessárias
			print(jogador_local._position)
			if jogador_local._position == 0:
				dealer = jogador_local.DefinirDealer() #!! não sei se nos diagramas isso ta aqui. alguem ve
				print("Eu sou o jogador 0 e decidi que o seguinte jogador é o dealer: " + jogador_local._nome) 

		


	def pegarPlacar(self):
		"""@ReturnType int*"""
		pass


	def novaMao(self):
		Mao_registro =self.registrarMao()
		Rodada = self.registrarStatusRodada(True)
		self._ordemRodada = self.definirOrdem() #!! olha, aqui ta meio redundante já que definirOrdem já faz a atribuição. De qualquer forma tem que mudar o diagrama de sequencia Nova Mão
		self._baralho.embaralharCartas() #!! Tem um nota bizarra no diagrama de sequencia sobre "só entrará se for dealer" isso aqui tudo quem vai fazer é só o dealer. Por isso no final ele chama "enviarAtualização"
		self.distribuirCartas()
		self._manilha = self._jogadores[0].definirManilha(self._baralho) #!! diagrama de sequência não ta passando baralho como parametro. tem que passar
		print(self._manilha._valor)



	def distribuirCartas(self): #!! acho que metodo não existe na classe. o gerador automatico pelo menos não fez. O return é desnecessário e bunda

		i = 0 
		for jogador in self._jogadores:
			print("CARTAS PARA JOGADOR")
			carta1 = self._baralho._cartas[i]
			i = i+1
			carta2 = self._baralho._cartas[i]
			i = i+1
			carta3 = self._baralho._cartas[i]
			i = i+1
			jogador._mao = [carta1, carta2, carta3]
		
		print(i)

	def novaRodada(self):
		pass

	def ColocarNaMesa(self, aTime, cardIndex, jogador): #!! deve retornar um array com valor naipe da carta
		carta = jogador._mao[cardIndex]
		jogador._mao[cardIndex] = None
		self._monte[aTime].append(carta)
		carta = [carta._valor,carta._naipe]
		return carta

	def PassarTurno(self, jogador):
		jogador._seuTurno = False
		for j in range(4):
			if self._ordemRodada[j]._nome == jogador._nome:
				if j != 3:
					return self._ordemRodada[j]._nome
				


	def ClicarBotaoTruco(self, jogador):
		turno = jogador.verificarTurno()
		if turno:
			truco = self.VerificarTrucoAndamento()
			if not truco:
				self.registrarTruco()
				self._PlayerInterface_.Notificar('Você pediu truco, aguardando resposta adversária')
				novoEstado = {'tipo' : 'truco', 'time' : jogador._time, 'respondido' : False}
				self._PlayerInterface_.enviarAtualizaçãoPartida(novoEstado)
			else:
				self._PlayerInterface_.Notificar("Jogada de truco em andamento")
		else:
			self._PlayerInterface_.Notificar("Não é seu turno")

	def VerificarTrucoAndamento(self):
		"""@ReturnType boolean"""
		return self._truco

	def receberJogada(self, aJogada):
		"""@ParamType aJogada Dict{string, any}"""
		if self._table._Inicializada == False: #!! tem que fazer esse rolo do cacete pra rececber o nome dos jogadores antes de começar o jogo
			self.inicializar_mesa(aJogada) #!! Adicionar ao diagrama
		elif 'tipo' in aJogada.payload:
			if aJogada.payload['tipo'] == 'NovaMao' and aJogada.payload['turno_mao'] == self.localPlayer._position:
						print("pegando minha mão hehe")
						temp_mao = aJogada.payload['nova_mao'][(self.match_position)]
						self.localPlayer._mao = []
									
						carta1 = Carta(temp_mao[0][0],temp_mao[0][1])
						carta2 = Carta(temp_mao[1][0],temp_mao[1][1])
						carta3 = Carta(temp_mao[2][0],temp_mao[2][1])

						self.localPlayer._mao.append(carta1)
						self.localPlayer._mao.append(carta2)
						self.localPlayer._mao.append(carta3)

						temp_manilha = aJogada.payload['manilha']
						manilha = Carta(temp_manilha,'ouro')
						self._table._manilha = manilha

						self.AtualizarInterface()

						if self.localPlayer._position == 3:
							pass
						else:
							turno = (self.localPlayer._position + 1)
							self.send_move({'tipo': 'NovaMao', 'nova_mao': aJogada.payload['nova_mao'], 'turno_mao':turno, 'manilha': self._table._manilha._valor})

	def __init__(self, deck, time1, time2, interface):
		self._jogadores = []

		self._Inicializada = False
		"""@AttributeType Problema.Jogador"""
		self._baralho = deck
		"""@AttributeType Problema.Baralho"""
		self._manilha = Carta('','')
		"""@AttributeType Problema.Carta"""
		self._valorMao = 1
		"""@AttributeType int"""
		self._partidaAndamento = False
		"""@AttributeType boolean"""
		self._times = [time1,time2]
		"""@AttributeType Problema.Time"""
		self._rodadaAndamento = None
		"""@AttributeType boolean"""
		self._maoAndamento = None
		"""@AttributeType boolean"""
		self._truco = False
		"""@AttributeType boolean"""
		self._monte = [[],[]]
		"""@AttributeType Problema.Carta*"""
		self._registroRodada = 3
		"""@AttributeType int*"""
		self._ordemRodada = []
		"""@AttributeType Problema.Jogador*"""
		self._placar = None
		"""@AttributeType int*"""
		self._vencedor = None
		"""@AttributeType Problema.Time"""
		self._PlayerInterface = interface
		"""@AttributeType TKinter.PlayerInterface
		# @AssociationType TKinter.PlayerInterface"""
		self._unnamed_Jogador_3 = None
		"""@AttributeType Problema.Jogador
		# @AssociationType Problema.Jogador
		# @AssociationKind Aggregation"""
		self._unnamed_Baralho_ = None
		"""@AttributeType Problema.Baralho
		# @AssociationType Problema.Baralho
		# @AssociationKind Aggregation"""
		self._unnamed_Time_ = []
		"""@AttributeType Problema.Time*
		# @AssociationType Problema.Time[]
		# @AssociationMultiplicity 2
		# @AssociationKind Aggregation"""

