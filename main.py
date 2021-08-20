from catalogo import Catalogo

def main():

	catalogo = Catalogo()
	# catalogo.adicionarRegistro("a", 2003, "album", 33)
	# catalogo.adicionarRegistro("b", 2001, "album", 9)
	# catalogo.adicionarRegistro("g", 2020, "album", 53)
	# catalogo.adicionarRegistro("z", 2011, "album", 61)
	# catalogo.adicionarRegistro("d", 2013, "album", 8)
	# catalogo.adicionarRegistro("y", 2015, "album", 21)
	# catalogo.adicionarRegistro("t", 2000, "album", 11)
	# catalogo.adicionarRegistro("u", 2006, "album", 12)

	# catalogo.adicionarRegistro("c", 2018, "album", 1)
	# catalogo.adicionarRegistro("o", 2004, "album", 45)
	# catalogo.adicionarRegistro("i", 2001, "album", 99)
	# catalogo.adicionarRegistro("e", 2002, "album", 37)
	# catalogo.adicionarRegistro("b", 2012, "album", 60)
	# catalogo.adicionarRegistro("g", 2007, "album", 59)

	print('Bem-vindo(a) ao sistema de stream!')
	while True:
		print('Escolha uma das opções abaixo:')
		print('(1) Inserir música')
		print('(2) Buscar música pelo id')
		print('(3) Buscar músicas pelo ano')
		print('(4) Listar músicas em ordem alfabética')
		print('(5) Altura da árvore')
		print('(6) Exibir a árvore')
		print('(7) Sair do programa')
		opcaoEscolhida = int(input('Digita a opção escolhida: '))

		if opcaoEscolhida == 1:
			nomeMusica = input("Digite o nome da música: ")
			anoMusica = int(input("Digite o ano da música: "))
			idMusica = int(input("Digite o id da música: "))
			albumMusica = input("Digite o album da música: ")
			catalogo.adicionarRegistro(nomeMusica, anoMusica, albumMusica, idMusica)
			print('Música adicionada!')
			print(20 * '-')
			continue
		elif opcaoEscolhida == 2:
			idMusica = int(input("Digite o id da música: "))
			registros = catalogo.buscarPorId(idMusica)
			if len(registros) > 0:
				print("\nMúsica(s) encontrada(s): \n")
				print('\n\n'.join([str(x) for x in registros]))
				print('\n')
			else:
				print("Música não encontrada!")
			print(20 * '-')
			continue
		elif opcaoEscolhida == 3:
			anoMusica = int(input("Digite o ano da música: "))
			registros = catalogo.buscarPorAno(anoMusica)
			if len(registros) > 0:
				print("\nMúsica(s) encontrada(s): \n")
				print('\n\n'.join([str(x) for x in registros]))
				print('\n')
			else:
				print("Música não encontrada!")
			print(20 * '-')
			continue
		elif opcaoEscolhida == 4:
			print("\nMúsicas em ordem alfabética: \n")
			catalogo.imprimirArvoreInOrder(catalogo._raizNome, 'nome')
			print(20 * '-')
			continue
		elif opcaoEscolhida == 5:
			print("\nAltura da árvore: \n")
			print(catalogo.getAltura(catalogo._raiz))
			print(20 * '-')
			continue
		elif opcaoEscolhida == 6:
			print('')
			# catalogo.printHelper(catalogo._raiz, "", True, 'id')
			catalogo.imprimirArvore2(catalogo._raiz, 'id')
			print(20 * '-')
			continue
		elif opcaoEscolhida == 7:
			return
		else:
			print("Opção inválida!")
			continue

if __name__ == "__main__":
  main()
