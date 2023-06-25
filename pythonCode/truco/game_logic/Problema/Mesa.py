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
		pass

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

<<<<<<< Updated upstream
	def encerramentoRodada(self):
		"""@ReturnType boolean"""
		pass

	def encerramentoMao(self): # !! metodo nao estad nos diagramas, arrumar diagrama de avaliar encerramento da mao
		pass
   
	def comparaMonte(self):
		"""@ReturnType int"""
		pass
=======
	def encerramentoRodada(self, jogador):
		#!! alterar parametro nos diagramas
		encerrar = False
		cartaForte = self.comparaMonte()
		self.definirTopo(cartaForte)
		self._PlayerInterface.atualizarTopo(cartaForte)
		ordem = self.pegarOrdem()
		ehUltimo = self._jogadores[jogador].ehUltimo(ordem)
		#if ehUltimo:
			#pontuaRodada = self.vencedorRodada(self._monte, cartaForte)
			#!! TODO: acrescentar vetor registroRodadas
			#qualrodada= self.verificaRodada()
			#self.registrarRodada(qualrodada, pontuaRodada)
			#encerrar = True
			#self.registrarStatusRodada(False)
		return encerrar

	def encerramentoMao(self):
		rodadas = self.verificarRegistroRodadas()
		match len(rodadas):
			case 1:
				#  Apenas uma rodada até o momento.
				self._times[1].registraMaoEncerrada(False)
				self._times[0].registraMaoEncerrada(False)
			case 2:
				#  Duas rodadas até o momento.
				empate = self.verificarEmpate()
				if empate:
					# !! TODO: implementar verificarEmpate
					# !! TODO: implementar verificarRodadasEmpatadas
					rodadasEmpatadas = self.verificarRodadasEmpatadas()
					if len(rodadasEmpatadas) > 2:
						self._times[1].registraMaoEncerrada(False)
						self._times[0].registraMaoEncerrada(False)
					elif len(rodadasEmpatadas) == 1:
						# !! TODO: implementar verificarVencedorRodada
						time = self.verificarVencedorRodada(rodadasEmpatadas[0])
						if time == self._times[0]:
							self.registraPontoMao(self._times[0], self._valorMao)
							self._times[0].registraMaoEncerrada(True)
						else:
							self.registraPontoMao(self._times[1], self._valorMao)
							self._times[1].registraMaoEncerrada(True)
					else:
						# rodadasempatadas == 2
						time = self.verificarVencedorRodada(rodadasEmpatadas[0])
						if time == self._times[0]:
							self.registraPontoMao(self._times[0], self._valorMao)
							self._times[0].registraMaoEncerrada(True)
						else:
							self.registraPontoMao(self._times[1], self._valorMao)
							self._times[1].registraMaoEncerrada(True)
				else:
					#!! TODO: verificar identificação do time local ou remoto
					rodadasTimeLocal = self._times[0].verificarRodadasTime()
					rodadasTimeRemoto = self._times[1].verificarRodadasTime()
					if rodadasTimeLocal == 2:
						self.registraPontoMao(self._times[0], self._valorMao)
						self._times[0].registraMaoEncerrada(True)
					elif rodadasTimeRemoto == 2:
						self.registraPontoMao(self._times[1], self._valorMao)
						self._times[1].registraMaoEncerrada(True)
					else:
						# rodadasTimeLocal == 1 and rodadasTimeRemoto == 1
						self._times[1].registraMaoEncerrada(False)
						self._times[0].registraMaoEncerrada(False)
			case 3:
				#  Três rodadas até o momento.
				empate = self.verificarEmpate()
				if empate:
					rodadasEmpatadas = self.verificarRodadasEmpatadas()
					if len(rodadasEmpatadas) >= 3:
						self.nenhumTimePontua()
					elif len(rodadasEmpatadas) == 2:
						time = self.verificarVencedorRodada(rodadasEmpatadas[0])
						if time == self._times[0]:
							self.registraPontoMao(self._times[0], self._valorMao)
							self._times[0].registraMaoEncerrada(True)
						else:
							self.registraPontoMao(self._times[1], self._valorMao)
							self._times[1].registraMaoEncerrada(True)
					else:
						# rodadasempatadas == 1
						time = self.verificarVencedorRodada(rodadasEmpatadas[0])
						if time == self._times[0]:
							self.registraPontoMao(self._times[0], self._valorMao)
							self._times[0].registraMaoEncerrada(True)
						else:
							self.registraPontoMao(self._times[1], self._valorMao)
							self._times[1].registraMaoEncerrada(True)
				else:
					rodadasTimeLocal = self._times[0].verificarRodadasTime()
					rodadasTimeRemoto = self._times[1].verificarRodadasTime()
					if rodadasTimeLocal == 2:
						self.registraPontoMao(self._times[0], self._valorMao)
						self._times[0].registraMaoEncerrada(True)
					if rodadasTimeRemoto == 2:
						self.registraPontoMao(self._times[1], self._valorMao)
						self._times[1].registraMaoEncerrada(True)


	def comparaMonte(self):
		"""@ReturnType carta"""
		naipes = ["paus","copa","espada","ouro"]
		seq = [4,5,6,7,'J','Q','K',1,2,3]
		cartaForte = Carta(4, 'ouro') #!! teste isso né?
		cartas_monte = [item for sublist in self._monte for item in sublist]
		for carta in cartas_monte:
			valorCarta = seq.index(carta._valor)
			valorCartaForte = seq.index(cartaForte._valor)
			naipeCarta = naipes.index(carta._naipe)
			naipeCartaForte = naipes.index(cartaForte._naipe)
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



>>>>>>> Stashed changes

	def definirTopo(self, aCartaForte):
		"""@ParamType aCartaForte int
		@ReturnType int"""
		pass

	def pegarOrdem(self):
		"""@ReturnType Problema.Jogador[]"""
		pass

	def vencedorRodada(self, aMonte, aCartaForte):
		"""@ParamType aMonte Problema.Carta*
		@ParamType aCartaForte int
		@ReturnType int"""
		pass

	def verificaRodada(self, *aRegistroRodadas):
		"""@ParamType aRegistroRodadas int*
		@ReturnType int"""
		pass

	def registrarRodada(self, aQualRodada, aVencedorRodada):
		"""@ParamType aQualRodada int
		@ParamType aVencedorRodada int"""
		pass

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
<<<<<<< Updated upstream

	def ColocarNaMesa(self, aTime):
		"""@ParamType aTime int"""
		pass
=======
	def ColocarNaMesa(self, aTime, cardIndex, jogador): #!! deve retornar um array com valor naipe da carta
		carta = jogador._mao[cardIndex]
		jogador._mao[cardIndex] = None
		carta = [carta._valor,carta._naipe]
		self._monte[aTime].append(carta)
		self._PlayerInterface.localPlayer._mao[cardIndex] = None
		return carta

	def PassarTurno(self, jogador):
		jogador._seuTurno = False
		proximo = (jogador._position + 1) % 4
		for player in self._jogadores:
			if player._position == proximo:
				return player._nome
>>>>>>> Stashed changes

	def PassarTurno(self):
		pass

<<<<<<< Updated upstream
	def ClicarBotaoTruco(self):
		pass
=======
	def ClicarBotaoTruco(self, jogador):
		turno = jogador.verificarTurno()
		if turno:
			truco = self.VerificarTrucoAndamento()
			if not truco:
				self.registrarTruco()
				self._PlayerInterface.Notificar('Você pediu truco, aguardando resposta adversária')
				novoEstado = {'tipo' : 'truco', 'time' : jogador._time, 'respondido' : False}
				self._PlayerInterface.enviarAtualizaçãoPartida(novoEstado)
			else:
				self._PlayerInterface.Notificar("Jogada de truco em andamento")
		else:
			self._PlayerInterface.Notificar("Não é seu turno")
>>>>>>> Stashed changes

	def VerificarTrucoAndamento(self):
		"""@ReturnType boolean"""
		pass

	def receberJogada(self, aJogada):
		"""@ParamType aJogada Dict{string, any}"""
<<<<<<< Updated upstream
		pass
=======
		if 'tipo' in aJogada.payload:
			if aJogada.payload['tipo'] == 'NovaMao' and aJogada.payload['turno_mao'] == self._PlayerInterface.localPlayer._position:
				print("pegando minha mão hehe")
				temp_mao = aJogada.payload['nova_mao'][(self._PlayerInterface.match_position)]
				self._PlayerInterface.localPlayer._mao = []
							
				carta1 = Carta(temp_mao[0][0],temp_mao[0][1])
				carta2 = Carta(temp_mao[1][0],temp_mao[1][1])
				carta3 = Carta(temp_mao[2][0],temp_mao[2][1])

				self._PlayerInterface.localPlayer._mao.append(carta1)
				self._PlayerInterface.localPlayer._mao.append(carta2)
				self._PlayerInterface.localPlayer._mao.append(carta3)

				temp_manilha = aJogada.payload['manilha']
				manilha = Carta(temp_manilha,'ouro')
				self._manilha = manilha

				self._PlayerInterface.AtualizarInterface()

				if self._PlayerInterface.localPlayer._position == 3:
					pass
				else:
					turno = (self._PlayerInterface.localPlayer._position + 1)
					self._PlayerInterface.send_move({'tipo': 'NovaMao', 'nova_mao': aJogada.payload['nova_mao'], 'turno_mao':turno, 'manilha': self._manilha._valor})
     
			elif aJogada.payload['tipo'] == 'rodada':
				pass
		
			elif aJogada.payload['tipo'] == 'carta':
				if aJogada.payload['rodadaEncerrada']:
					if vence == 0:
						printar = 'azul'
					else:
						printar = 'vermelho'
					if aJogada.payload['maoEncerrada']:
						self.registrarMao()
						vence = None # só pra nao acusar erro
						self.adicionarPontuacaoTime(vence, self._valorMao) # tem q receber o paratro do time q vence a rodada por pyng 
						if aJogada.payload['jogoEncerrado']:
							self.registrarVencedor(vence) #  TODO time vencedor deve chegar por pyng
							
							self._PlayerInterface.Notificar(f'Time {printar} vence o jogo')
						else:
						
							self._PlayerInterface.Notificar(f'Time {printar} vence a rodada')
					else:
						self.registrarStatusRodada(False)
						self._PlayerInterface.Notificar(f'Time {printar} vence a rodada')
						qualRodada = None # apenas pra nao acusar erro
						self.registrarRodada(qualRodada,vence) # TODO parametros tem que chegar por pyng
				else:
					self._PlayerInterface.Notificar(f'Turno de {aJogada.payload["proximo"]}')
					self._monte.append(aJogada.payload['carta'])
					print(self._monte)
					if self._PlayerInterface.localPlayer._nome == aJogada.payload['proximo']:
						
						self._PlayerInterface.AtualizarInterface()
						
						self._PlayerInterface.localPlayer._seuTurno = True
						print("MEU TURNO AEEE")
			
			elif aJogada.payload['tipo'] == 'truco':
				pass
>>>>>>> Stashed changes

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
		self._truco = None
		"""@AttributeType boolean"""
		self._monte = None
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

