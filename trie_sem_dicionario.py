class nodoQuasePatriciano:

	"""
	O nodo padrão.
	"""

	def __init__(self, char, dictionary_index):
		
		self.char_armazenado = char

		self.dictionary_index = dictionary_index

		self.representa_fim_da_palavra = False

		self.filhotes = []


class quasePatricia:

	def __init__(self):

		"""
		A quasePatricia possui o nodo raíz.
		A string vazia é armazenada nele.
		"""

		self.root = nodoQuasePatriciano('', 0)

	def insere_palavra(self, word, index):

		"""
		Insere uma palavra junta de
		um índice na quasePatrícia.
		O nodo que representa a última
		letra da palavra recebe o índice.
		"""

		nodo_atual = self.root

		for char in word:

			for filhote in nodo_atual.filhotes:

				filhote_encontrado_com_char = False

				if filhote.char_armazenado == char:

					nodo_atual = filhote

					filhote_encontrado_com_char = True

				if not filhote_encontrado_com_char:

					new_node = nodoQuasePatriciano(char, index)

					nodo_atual.filhotes.append(new_node)

					nodo_atual = new_node

					break

		nodo_atual.representa_fim_da_palavra = True

	def get_word_index(self, palavra):

		"""
		Dada uma palavra, retorna o índice
		do nodo que representa o último caractere
		da palavra no galho correspondente.
		Se não há essa palavra na quasePatricia,
		a função retorna -1.
		"""

		nodo_atual = self.root

		if palavra == '':

			return 0

		palavra_encontrada = False

		palavra_em_construcao = ""

		for char in palavra:

			char_encontrado_nos_filhotes = False

			for filhote in nodo_atual.filhotes:				

				if char == filhote.char_armazenado:

					nodo_atual = filhote

					char_encontrado_nos_filhotes = True

					palavra_em_construcao += char

				if not char_encontrado_nos_filhotes:

					return -1

		if (nodo_atual.representa_fim_da_palavra == True) and (palavra_em_construcao == palavra):

			palavra_encontrada = True

			return nodo_atual.dictionary_index

		if not palavra_encontrada:

			return -1