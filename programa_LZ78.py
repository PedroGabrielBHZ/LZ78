import argparse

from LZ78_pgas import *


parser = argparse.ArgumentParser(

	description = "Um programa para comprimir e descomprimir arquivos utilizando o metodo LZ78."

	)

parser.add_argument(

		"-x",

		"--descomprimir",

		type=str,

		dest="descomprimir",

		help="descomprime um arquivo .lz78 em um arquivo .txt"

	)

parser.add_argument(

		"-c",

		"--comprimir",

		type=str,

		dest="comprimir",

		help="comprime um arquivo .txt em um arquivo .lz78"

	)

parser.add_argument(

		"-o",

		"--arquivo_saida",

		type=str,

		dest="define_saida",
		
		help="define o caminho do arquivo de saida, argumento opcional"

	)

argumentos = parser.parse_args()

if argumentos.comprimir:

	if argumentos.define_saida:

		compressao_LZ78_ineficiente_mas_funcional(argumentos.comprimir, argumentos.define_saida)

	else:

		caminho_saida = '.'.join(argumentos.comprimir.split('.')[:-1] + ['z78'])

		compressao_LZ78_ineficiente_mas_funcional(argumentos.comprimir, caminho_saida)

elif argumentos.descomprimir:

	if argumentos.define_saida:

		descompressao_LZ78_quase_eficiente(argumentos.descomprimir, argumentos.define_saida)

	else:

		caminho_saida = '.'.join(argumentos.descomprimir.split('.')[:-1] + ['txt'])

		descompressao_LZ78_quase_eficiente(argumentos.descomprimir, caminho_saida)

else:

	print(" -- erro nos argumentos --")



