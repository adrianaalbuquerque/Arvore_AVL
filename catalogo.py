from registro import Registro

class Catalogo:
	def __init__(self):
		self._raiz = None
		self._raizNome = None
		self._raizAno = None

	def adicionarRegistro(self, nomeMusica, ano, album, id):
		novo_registro = Registro(nomeMusica, ano, album, id)
		novo_registro2 = Registro(nomeMusica, ano, album, id)
		novo_registro3 = Registro(nomeMusica, ano, album, id)
		self.adicionarRegistroPorId(novo_registro)
		self.adicionarRegistroPorNome(novo_registro2)
		self.adicionarRegistroPorAno(novo_registro3)

	def adicionarRegistroPorId(self, novo_registro):
		if not self._raiz:
			self._raiz = novo_registro
			return
		
		caminho_ate_insercao = []
		inicio = self._raiz

		while True:
			caminho_ate_insercao.append(inicio)
			if novo_registro._id >= inicio._id:
				if inicio._direita != None:
					inicio = inicio._direita
					continue
				else:
					inicio._direita = novo_registro
					break
			else: 
				if inicio._esquerda != None:
					inicio = inicio._esquerda
					continue
				else:
					inicio._esquerda = novo_registro
					break

		caminho_ate_insercao.append(novo_registro)
		#atualizando altura dos nós percorridos
		altura_max_percurso = len(caminho_ate_insercao)

		for no in caminho_ate_insercao:
			if no._altura < altura_max_percurso:
				no._altura = altura_max_percurso
			altura_max_percurso -= 1

		#atualizando balanco dos nós percorridos
		for no in caminho_ate_insercao:
			no._balanco = self.getBalanco(no)

		#procurando primeiro nó do percurso (de baixo pra cima) que ficou desbalanceado
		for i in reversed(range(len(caminho_ate_insercao))):
			if caminho_ate_insercao[i]._balanco > 1:
				# caso esquerda esquerda
				if novo_registro._id < caminho_ate_insercao[i]._esquerda._id:
					res = self.rotacionarADireitaId(caminho_ate_insercao[i])
					if i > 0:
						self.atribuirPaiId(caminho_ate_insercao[i-1], res)
				#caso esquerda direita
				else:
					res = self.rotacionarAEsquerdaId(caminho_ate_insercao[i]._esquerda)
					self.atribuirPaiId(caminho_ate_insercao[i], res)

					res = self.rotacionarADireitaId(caminho_ate_insercao[i])
					if i > 0:
						self.atribuirPaiId(caminho_ate_insercao[i-1], res)

				#atualizando altura dos nós acima
				for k in reversed(range(i)):
					caminho_ate_insercao[k]._altura = 1 + max(self.getAltura(caminho_ate_insercao[k]._esquerda), self.getAltura(caminho_ate_insercao[k]._direita))
				break
			if caminho_ate_insercao[i]._balanco < -1:				
				# caso direita direita
				if novo_registro._id >= caminho_ate_insercao[i]._direita._id:
					res = self.rotacionarAEsquerdaId(caminho_ate_insercao[i])
					if i > 0:
						self.atribuirPaiId(caminho_ate_insercao[i-1], res)
				#caso direita esquerda
				else:
					res = self.rotacionarADireitaId(caminho_ate_insercao[i]._direita)
					self.atribuirPaiId(caminho_ate_insercao[i], res)

					res = self.rotacionarAEsquerdaId(caminho_ate_insercao[i])
					if i > 0:
						self.atribuirPaiId(caminho_ate_insercao[i-1], res)

				#atualizando altura dos nós acima
				for k in reversed(range(i)):
					caminho_ate_insercao[k]._altura = 1 + max(self.getAltura(caminho_ate_insercao[k]._esquerda), self.getAltura(caminho_ate_insercao[k]._direita))
				break		

	def adicionarRegistroPorAno(self, novo_registro):
		if not self._raizAno:
			self._raizAno = novo_registro
			return
		
		caminho_ate_insercao = []
		inicio = self._raizAno

		while True:
			caminho_ate_insercao.append(inicio)
			if novo_registro._ano >= inicio._ano:
				if inicio._direita != None:
					inicio = inicio._direita
					continue
				else:
					inicio._direita = novo_registro
					break
			else: 
				if inicio._esquerda != None:
					inicio = inicio._esquerda
					continue
				else:
					inicio._esquerda = novo_registro
					break

		caminho_ate_insercao.append(novo_registro)
		#atualizando altura dos nós percorridos
		altura_max_percurso = len(caminho_ate_insercao)

		for no in caminho_ate_insercao:
			if no._altura < altura_max_percurso:
				no._altura = altura_max_percurso
			altura_max_percurso -= 1

		#atualizando balanco dos nós percorridos
		for no in caminho_ate_insercao:
			no._balanco = self.getBalanco(no)

		#procurando primeiro nó do percurso (de baixo pra cima) que ficou desbalanceado
		for i in reversed(range(len(caminho_ate_insercao))):
			if caminho_ate_insercao[i]._balanco > 1:
				# caso esquerda esquerda
				if novo_registro._ano < caminho_ate_insercao[i]._esquerda._ano:
					res = self.rotacionarADireitaAno(caminho_ate_insercao[i])
					if i > 0:
						self.atribuirPaiAno(caminho_ate_insercao[i-1], res)
				#caso esquerda direita
				else:
					res = self.rotacionarAEsquerdaAno(caminho_ate_insercao[i]._esquerda)
					self.atribuirPaiAno(caminho_ate_insercao[i], res)

					res = self.rotacionarADireitaAno(caminho_ate_insercao[i])
					if i > 0:
						self.atribuirPaiAno(caminho_ate_insercao[i-1], res)

				#atualizando altura dos nós acima
				for k in reversed(range(i)):
					caminho_ate_insercao[k]._altura = 1 + max(self.getAltura(caminho_ate_insercao[k]._esquerda), self.getAltura(caminho_ate_insercao[k]._direita))
				break
			if caminho_ate_insercao[i]._balanco < -1:				
				# caso direita direita
				if novo_registro._ano >= caminho_ate_insercao[i]._direita._ano:
					res = self.rotacionarAEsquerdaAno(caminho_ate_insercao[i])
					if i > 0:
						self.atribuirPaiAno(caminho_ate_insercao[i-1], res)
				#caso direita esquerda
				else:
					res = self.rotacionarADireitaAno(caminho_ate_insercao[i]._direita)
					self.atribuirPaiAno(caminho_ate_insercao[i], res)

					res = self.rotacionarAEsquerdaAno(caminho_ate_insercao[i])
					if i > 0:
						self.atribuirPaiAno(caminho_ate_insercao[i-1], res)

				#atualizando altura dos nós acima
				for k in reversed(range(i)):
					caminho_ate_insercao[k]._altura = 1 + max(self.getAltura(caminho_ate_insercao[k]._esquerda), self.getAltura(caminho_ate_insercao[k]._direita))
				break

	def adicionarRegistroPorNome(self, novo_registro):
		if not self._raizNome:
			self._raizNome = novo_registro
			return
		
		caminho_ate_insercao = []
		inicio = self._raizNome

		while True:
			caminho_ate_insercao.append(inicio)
			if novo_registro._nomeMusica >= inicio._nomeMusica:
				if inicio._direita != None:
					inicio = inicio._direita
					continue
				else:
					inicio._direita = novo_registro
					break
			else: 
				if inicio._esquerda != None:
					inicio = inicio._esquerda
					continue
				else:
					inicio._esquerda = novo_registro
					break

		caminho_ate_insercao.append(novo_registro)
		#atualizando altura dos nós percorridos
		altura_max_percurso = len(caminho_ate_insercao)

		for no in caminho_ate_insercao:
			if no._altura < altura_max_percurso:
				no._altura = altura_max_percurso
			altura_max_percurso -= 1

		#atualizando balanco dos nós percorridos
		for no in caminho_ate_insercao:
			no._balanco = self.getBalanco(no)

		#procurando primeiro nó do percurso (de baixo pra cima) que ficou desbalanceado
		for i in reversed(range(len(caminho_ate_insercao))):
			if caminho_ate_insercao[i]._balanco > 1:
				# caso esquerda esquerda
				if novo_registro._nomeMusica < caminho_ate_insercao[i]._esquerda._nomeMusica:
					res = self.rotacionarADireitaNome(caminho_ate_insercao[i])
					if i > 0:
						self.atribuirPaiNome(caminho_ate_insercao[i-1], res)
				#caso esquerda direita
				else:
					res = self.rotacionarAEsquerdaNome(caminho_ate_insercao[i]._esquerda)
					self.atribuirPaiNome(caminho_ate_insercao[i], res)

					res = self.rotacionarADireitaNome(caminho_ate_insercao[i])
					if i > 0:
						self.atribuirPaiNomeNome(caminho_ate_insercao[i-1], res)

				#atualizando altura dos nós acima
				for k in reversed(range(i)):
					caminho_ate_insercao[k]._altura = 1 + max(self.getAltura(caminho_ate_insercao[k]._esquerda), self.getAltura(caminho_ate_insercao[k]._direita))
				break
			if caminho_ate_insercao[i]._balanco < -1:				
				# caso direita direita
				if novo_registro._nomeMusica >= caminho_ate_insercao[i]._direita._nomeMusica:
					res = self.rotacionarAEsquerdaNome(caminho_ate_insercao[i])
					if i > 0:
						self.atribuirPaiNome(caminho_ate_insercao[i-1], res)
				#caso direita esquerda
				else:
					res = self.rotacionarADireitaNome(caminho_ate_insercao[i]._direita)
					self.atribuirPaiNome(caminho_ate_insercao[i], res)

					res = self.rotacionarAEsquerdaNome(caminho_ate_insercao[i])
					if i > 0:
						self.atribuirPaiNome(caminho_ate_insercao[i-1], res)

				#atualizando altura dos nós acima
				for k in reversed(range(i)):
					caminho_ate_insercao[k]._altura = 1 + max(self.getAltura(caminho_ate_insercao[k]._esquerda), self.getAltura(caminho_ate_insercao[k]._direita))
				break		

	def atribuirPaiId(self, pai, filho):
		if filho._id >= pai._id:
			pai._direita = filho
		else:
			pai._esquerda = filho

	def atribuirPaiNome(self, pai, filho):
		if filho._nomeMusica >= pai._nomeMusica:
			pai._direita = filho
		else:
			pai._esquerda = filho

	def atribuirPaiAno(self, pai, filho):
		if filho._ano >= pai._ano:
			pai._direita = filho
		else:
			pai._esquerda = filho

	def imprimirArvoreInOrder(self, raiz, campo):
		if raiz:
			self.imprimirArvoreInOrder(raiz._esquerda, campo)
			print(raiz.printToStr(campo))
			self.imprimirArvoreInOrder(raiz._direita, campo)

	def imprimirArvorePreOrder(self, raiz, campo):
		if raiz:
			print(raiz.printToStr(campo) + "->", end='')
			self.imprimirArvorePreOrder(raiz._esquerda, campo)			
			self.imprimirArvorePreOrder(raiz._direita, campo)

	def imprimirArvorePostOrder(self, raiz, campo):
		if raiz:
			self.imprimirArvorePostOrder(raiz._esquerda, campo)			
			self.imprimirArvorePostOrder(raiz._direita, campo)
			print(raiz.printToStr(campo) + "->", end='')

	def rotacionarAEsquerdaId(self, raiz):
		y = raiz._direita
		T2 = y._esquerda
		y._esquerda = raiz
		raiz._direita = T2

		#atualizando altura dos únicos nós que têm alturas afetadas e por conta disso, podemos confiar nas alturas de seus filhos porque as alturas deles não mudam na rotação
		#não precisamos atualizar o balanço nesse momento, já que na próxima inserção, os balanços dos nós afetados serão atualizados
		raiz._altura = 1 + max(self.getAltura(raiz._esquerda),
						   self.getAltura(raiz._direita))
		y._altura = 1 + max(self.getAltura(y._esquerda),
						   self.getAltura(y._direita))

		if raiz == self._raiz:
			self._raiz = y

		return y

	def rotacionarADireitaId(self, raiz):
		y = raiz._esquerda
		T3 = y._direita
		y._direita = raiz
		raiz._esquerda = T3

		#atualizando altura dos únicos nós que têm alturas afetadas e por conta disso, podemos confiar nas alturas de seus filhos porque as alturas deles não mudam na rotação
		#não precisamos atualizar o balanço nesse momento, já que na próxima inserção, os balanços dos nós afetados serão atualizados
		raiz._altura = 1 + max(self.getAltura(raiz._esquerda),
						   self.getAltura(raiz._direita))
		y._altura = 1 + max(self.getAltura(y._esquerda),
						   self.getAltura(y._direita))

		if raiz == self._raiz:
			self._raiz = y

		return y

	def rotacionarAEsquerdaNome(self, raiz):
		y = raiz._direita
		T2 = y._esquerda
		y._esquerda = raiz
		raiz._direita = T2

		#atualizando altura dos únicos nós que têm alturas afetadas e por conta disso, podemos confiar nas alturas de seus filhos porque as alturas deles não mudam na rotação
		#não precisamos atualizar o balanço nesse momento, já que na próxima inserção, os balanços dos nós afetados serão atualizados
		raiz._altura = 1 + max(self.getAltura(raiz._esquerda),
						   self.getAltura(raiz._direita))
		y._altura = 1 + max(self.getAltura(y._esquerda),
						   self.getAltura(y._direita))

		if raiz == self._raizNome:
			self._raizNome = y

		return y

	def rotacionarADireitaNome(self, raiz):
		y = raiz._esquerda
		T3 = y._direita
		y._direita = raiz
		raiz._esquerda = T3

		#atualizando altura dos únicos nós que têm alturas afetadas e por conta disso, podemos confiar nas alturas de seus filhos porque as alturas deles não mudam na rotação
		#não precisamos atualizar o balanço nesse momento, já que na próxima inserção, os balanços dos nós afetados serão atualizados
		raiz._altura = 1 + max(self.getAltura(raiz._esquerda),
						   self.getAltura(raiz._direita))
		y._altura = 1 + max(self.getAltura(y._esquerda),
						   self.getAltura(y._direita))

		if raiz == self._raizNome:
			self._raizNome = y

		return y

	def rotacionarAEsquerdaAno(self, raiz):
		y = raiz._direita
		T2 = y._esquerda
		y._esquerda = raiz
		raiz._direita = T2

		#atualizando altura dos únicos nós que têm alturas afetadas e por conta disso, podemos confiar nas alturas de seus filhos porque as alturas deles não mudam na rotação
		#não precisamos atualizar o balanço nesse momento, já que na próxima inserção, os balanços dos nós afetados serão atualizados
		raiz._altura = 1 + max(self.getAltura(raiz._esquerda),
						   self.getAltura(raiz._direita))
		y._altura = 1 + max(self.getAltura(y._esquerda),
						   self.getAltura(y._direita))

		if raiz == self._raizAno:
			self._raizAno = y

		return y

	def rotacionarADireitaAno(self, raiz):
		y = raiz._esquerda
		T3 = y._direita
		y._direita = raiz
		raiz._esquerda = T3

		#atualizando altura dos únicos nós que têm alturas afetadas e por conta disso, podemos confiar nas alturas de seus filhos porque as alturas deles não mudam na rotação
		#não precisamos atualizar o balanço nesse momento, já que na próxima inserção, os balanços dos nós afetados serão atualizados
		raiz._altura = 1 + max(self.getAltura(raiz._esquerda),
						   self.getAltura(raiz._direita))
		y._altura = 1 + max(self.getAltura(y._esquerda),
						   self.getAltura(y._direita))

		if raiz == self._raizAno:
			self._raizAno = y

		return y

	def buscarPorId(self, id):
		registros = []
		inicio = self._raiz
		while inicio:			
			if id >= inicio._id:
				if id == inicio._id:
					registros.append(inicio)
				inicio = inicio._direita
			else:
				inicio = inicio._esquerda
		return registros

	def buscarPorAno(self, ano):
		registros = []
		inicio = self._raizAno
		while inicio:			
			if ano >= inicio._ano:
				if ano == inicio._ano:
					registros.append(inicio)
				inicio = inicio._direita
			else:
				inicio = inicio._esquerda
		return registros

	# Get the height of the node
	def getAltura(self, raiz):
		if not raiz:
			return 0
		return raiz._altura

	def getBalanco(self, raiz):
		if not raiz:
			return 0
		return (raiz._esquerda._altura if raiz._esquerda != None else 0) - (raiz._direita._altura if raiz._direita != None else 0)

	def imprimirArvore2(self, raiz, campo = 'id'):
		if not raiz:
			return
		niveis = []
		nivel_atual = [raiz]
		proximo_nivel = []
		
		niveis.append(nivel_atual)		
					
		while True:
			temProximoNivel = False

			for no in nivel_atual:
				if not no:
					#apenas pra desenhar a árvore completa
					proximo_nivel.append(None)
					proximo_nivel.append(None)
					continue

				if no._esquerda or no._direita:
					temProximoNivel = True
									
				proximo_nivel.append(no._esquerda)
				proximo_nivel.append(no._direita)		
			
			if not temProximoNivel:
				break
			
			nivel_atual = proximo_nivel
			niveis.append(nivel_atual)
			proximo_nivel = []
		
		outer_espaco_char = ' '
		inner_espaco_char = '*'
		ikey_espaco_char = ' '
		tamanho_key = 3
		no_vazio_char = 'N'

		ultima_linha = inner_espaco_char.join([str(x.printToStr(campo) if x else 'N').center(tamanho_key, ikey_espaco_char) for x in niveis[len(niveis) - 1]])		
		espacos_entre_chaves = [i for i, c in enumerate(ultima_linha) if c == inner_espaco_char]
		espacos_entre_chaves_utlizados = espacos_entre_chaves[::2]

		#removendo os '*' que foram utilizados para encontrar os espaços em branco
		ultima_linha = ultima_linha.replace(inner_espaco_char, ' ')
		arvore_impressa3 = []
		arvore_impressa3.append(ultima_linha)

		for i in range(len(niveis) - 2, 0, -1):	
			distancia_entre_espacos = espacos_entre_chaves_utlizados[1] - espacos_entre_chaves_utlizados[0]			
			espaco_necessario = distancia_entre_espacos - int(tamanho_key - 1) - 1
			linha = ((ikey_espaco_char*espaco_necessario).join([str(x.printToStr(campo) if x else 'N').center(tamanho_key, ikey_espaco_char) for x in niveis[i]])).center(len(ultima_linha), outer_espaco_char)			
			arvore_impressa3.append(linha)

			espacos_entre_chaves_utlizados = [x + y for x, y in zip(espacos_entre_chaves_utlizados[::2], espacos_entre_chaves_utlizados[1::2])]
			espacos_entre_chaves_utlizados = [int(x/2) for x in espacos_entre_chaves_utlizados]			
		
		#adicionando raiz
		arvore_impressa3.append(str(niveis[0][0].printToStr(campo)).center(tamanho_key, ikey_espaco_char).center(len(ultima_linha), outer_espaco_char))
		print('\n'.join(arvore_impressa3[::-1]))