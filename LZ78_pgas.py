from trie_com_dicionario import *

tamanho_em_bytes_do_indice = 3
tamanho_em_bytes_do_caractere = 2

def compressao_LZ78_ineficiente_mas_funcional(caminho_de_entrada, caminho_de_saida):

	dicionario = quasePatricia()

	arquivo_entrada = open(caminho_de_entrada, 'r')

	texto_original = arquivo_entrada.read()

	arquivo_entrada.close()

	indice_dicionario = 1

	palavra_vazia = ''

	palavra = palavra_vazia

	arquivo_saida = open(caminho_de_saida, 'wb')

	for caractere in texto_original:

		palavra_concatenada = palavra + caractere

		indice_palavra_concatenada = dicionario.retorna_indice_da_palavra(palavra_concatenada)

		if indice_palavra_concatenada == (-1):

			indice_da_palavra = dicionario.retorna_indice_da_palavra(palavra)

			arquivo_saida.write(indice_da_palavra.to_bytes(tamanho_em_bytes_do_indice, "big"))

			arquivo_saida.write(ord(caractere).to_bytes(tamanho_em_bytes_do_caractere, "big"))

			dicionario.insere_palavra_e_indice(palavra_concatenada, indice_dicionario)

			indice_dicionario += 1

			palavra = palavra_vazia

		else:

			palavra = palavra_concatenada

	arquivo_saida.close()

def descompressao_LZ78_quase_eficiente(caminho_de_entrada, caminho_de_saida):

	dicionario_simplificado = ['']

	string_de_descodificacao = ""

	arquivo_entrada =  open(caminho_de_entrada, 'rb')

	fim_da_descodificacao = False

	while not fim_da_descodificacao :

		indice_da_palavra = arquivo_entrada.read(tamanho_em_bytes_do_indice)

		if indice_da_palavra == b'':

			fim_da_descodificacao = True

		indice_da_palavra = int.from_bytes(indice_da_palavra, byteorder="big")

		caractere = arquivo_entrada.read(tamanho_em_bytes_do_caractere)

		if caractere != b'':

			caractere = chr(int.from_bytes(caractere, byteorder="big"))

		else:

			caractere = ''

		palavra = dicionario_simplificado[indice_da_palavra]

		string_de_descodificacao += (palavra + caractere)

		dicionario_simplificado += [(palavra + caractere)]
	        
	arquivo_entrada.close()

	arquivo_saida = open(caminho_de_saida, 'w')

	arquivo_saida.write(string_de_descodificacao)

	arquivo_saida.close()