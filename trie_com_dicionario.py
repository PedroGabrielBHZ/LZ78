class nodoQuasePatriciano:

	"""
	O nodo padrão.
	"""

	def __init__(self, caractere, indice_dicionario):
		
		self.caractere_armazenado = caractere

		self.indice_dicionario = indice_dicionario

		self.representa_fim_da_palavra = False

		self.filhotes = {}

class quasePatricia:

	def __init__(self):

		"""
		A quasePatricia possui o nodo raíz.
		A string vazia é armazenada nele.
		"""

		self.raiz = nodoQuasePatriciano('', 0)

	def insere_palavra_e_indice(self, palavra, index):

		"""
		Insere uma palavra junta de
		um índice na quasePatrícia.
		O nodo que representa a última
		letra da palavra recebe o índice.
		"""

		nodo_atual = self.raiz

		for caractere in palavra:

			if caractere in nodo_atual.filhotes:

				nodo_atual = nodo_atual.filhotes[caractere]

			else:

				novo_nodo = nodoQuasePatriciano(caractere, index)

				nodo_atual.filhotes[caractere] = novo_nodo

				nodo_atual = novo_nodo

		nodo_atual.representa_fim_da_palavra = True

	def retorna_indice_da_palavra(self, palavra):

		"""
		Dada uma palavra, retorna o índice
		do nodo que representa o último caractere
		da palavra no galho correspondente.
		Se não há essa palavra na quasePatricia,
		a função retorna -1.
		"""

		nodo_atual = self.raiz

		if palavra == '':

			return 0

		palavra_encontrada = False

		palavra_em_construcao = ""

		for caractere in palavra:

			if caractere in nodo_atual.filhotes:

				nodo_atual = nodo_atual.filhotes[caractere]

				palavra_em_construcao += caractere

		if (nodo_atual.representa_fim_da_palavra == True) and (palavra_em_construcao == palavra):

			palavra_encontrada = True

			return nodo_atual.indice_dicionario

		if not palavra_encontrada:

			return -1