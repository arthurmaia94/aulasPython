# Importando a biblioteca PIL
from PIL import Image

# Importando a biblioteca OS
import os

# Constantes da biblioteca OS para dados de entrada e saida
INPUT_FOLDER="input"
OUTPUT_FOLDER="output"

# Inicio da função para retornar o diretório temporario da imagem
def in_path(filename):
	return os.path.join(INPUT_FOLDER, filename)

# Inicio da função para desenhar a imagem
def triangle(size):
	white = (255,255,255) # atribuição o RGB, equivalente a cor branca para variavel
	black = (0,0,0) # atribuição o RGB, equivalente a cor preta para variavel
	# Instância da classe Image (PIL) recebendo como parametro as variaveis para dimensoes e cor branca de fundo
	image = Image.new("RGB", (size, size), white)
	
	# Loop responsavel pelo desenho da area que devera ser impressa na cor preta
	for x in range(size):
		for y in range(size):
			if x < y:
				image.putpixel((x, y), black)
	return image

# função para desenha a bandeira japonesa
def bandeira_japao(height):
	width = 3*height//2
	WHITE = (255, 255, 255)
	RED = (173, 35, 35)
	r = 3*height//10
	c = (width//2, height//2)
	
	# Instância da classe Image (PIL) recebendo como parametro as variaveis para dimensoes e cor branca de fundo
	image = Image.new("RGB", (width, height), WHITE)
	
	# Loop para calcular os raios do circulo que deverá ser impresso
	for x in range(c[0]-r, c[0] + r):
		for y in range(c[1]-r, c[1] + r):
			if (x-c[0])**2 + (y-c[1])**2 <= r**2:
				image.putpixel((x, y), RED)
	return image

# Checagem de escopo
# Usando a varivel nativa __name__ para validar se retornar o módulo atual
if __name__ == "__main__":
	# Atribuimos a função para variavel passando o parametro de altura
	bandeira = bandeira_japao(700)
	# Metodo para exibir
	bandeira.show()
