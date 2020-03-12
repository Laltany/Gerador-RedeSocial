from os import listdir
import sys
import os
from graphviz import Digraph



diretorio = str(sys.argv[1])
dir= './'+ diretorio + "/"
lista_arqs = [arq for arq in listdir(dir)]


class vertice:
	def __init__(self, matricula, nome, curso, email, telefone, estado, relacionamentoN1 ,relacionamentoN2):
		self.matricula = matricula
		self.nome = nome 
		self.curso=curso
		self.email=email
		self.telefone = telefone
		self.estado= estado
		self.relacionamentoN1 = relacionamentoN1
		self.relacionamentoN2 = relacionamentoN2
		#self.predecessor = []

	def getmatricula(self):
		return self.matricula


class Aresta():
	def __init__(self,origem,destino):
		self.origem = origem
		self.destino = destino

	def getOrigem(self):
		return self.origem
		
	def getDestino(self):
		return self.destino

class Grafo:
	def __init__(self):
		self.lista_Vertices = []
		self.lista_Arestas = []
		self.lista_Arestas2 = []
		self.lista_Arestas_AuxTotal=[]

	def novo_Vertice(self, identificador, nome):       
		diretorio = dir + nome + ".txt"
		arquivo =  open(diretorio, 'r')
		linhas = arquivo.readlines()
		listaRelacionamentoN1 = list(map(int, linhas[6].split(",")))
		#print(listaRelacionamentoN1)
		listaRelacionamentoN2 = list(map(int, linhas[7].split(",")))
		#print(listaRelacionamentoN2)
		#print(identificador,linhas[1], linhas[2],linhas[3],linhas[4], linhas[5], listaRelacionamentoN1, listaRelacionamentoN2)			
		novo = vertice(identificador, linhas[1], linhas[2],linhas[3],linhas[4], linhas[5], listaRelacionamentoN1, listaRelacionamentoN2)  #Cria novo nodo
		self.lista_Vertices.append(novo)
		print(self.lista_Vertices)


	'''def remove_repetidos(lista):
	    l = []
	    for i in lista:
	        if i not in l:
	            l.append(i)
	    l.sort()
	    return l'''

	def nova_Aresta(self):  # Método recebe dois identificadores		
		for origem in self.lista_Vertices:
			origem_aux = self.busca_Vertice(origem.matricula)
			for destino in origem.relacionamentoN1:
				destino_aux =  self.busca_Vertice(destino)
				print("Origem", origem_aux.matricula)
				if (origem_aux is not None) and (destino_aux is not None):					
					self.lista_Arestas.append(Aresta(origem_aux.matricula, destino_aux.matricula))
					self.lista_Arestas_AuxTotal.append((origem_aux.matricula,destino_aux.matricula))
				else:
					print("O vertice %i não existe"%destino)
			for destino in origem.relacionamentoN2:
				destino_aux =  self.busca_Vertice(destino)
				print("Origem2", origem_aux.matricula)
				if (origem_aux is not None) and (destino_aux is not None):					
					self.lista_Arestas2.append(Aresta(origem_aux.matricula, destino_aux.matricula))
					self.lista_Arestas_AuxTotal.append((origem_aux.matricula,destino_aux.matricula))
				else:
					print("O vertice %i não existe"%destino)
		self.lista_Arestas_AuxTotal.sort()
		#x=[]
		#x = remove_repetidos(self.lista_Arestas_AuxTotal)

	def printArestas(self):
		self.lista_ArestasAux=[]
		for aresta in self.lista_Arestas:
			self.lista_ArestasAux.append((aresta.origem,aresta.destino))			      
		print(self.lista_ArestasAux)
		self.lista_ArestasAux2=[]
		for aresta in self.lista_Arestas2:
			self.lista_ArestasAux2.append((aresta.origem,aresta.destino))			       
		print(self.lista_ArestasAux2)


	def N1(self):
		print("relacionamentoN1:\n")
		for aresta in self.lista_Arestas:
			print(aresta.origem,"--->", aresta.destino)

	def N2(self):
		print("relacionamentoN2:\n")
		for aresta in self.lista_Arestas2:
			print(aresta.origem,"--->", aresta.destino)

	def Total(self):

		for aresta in self.lista_Arestas:
			print(aresta.origem,"--->", aresta.destino)
		for aresta in self.lista_Arestas2:
			print(aresta.origem,"--->", aresta.destino)

	def GraphvizN1(self):
		dot = Digraph(comment='Grafo referente ao N1')
		for vertice in self.lista_Vertices:
			x= str(vertice.matricula)
			print(x, vertice.nome)
			dot.node(x, vertice.nome)
		for aresta in self.lista_Arestas:
			x, y = str(aresta.origem), str(aresta.destino)
			x = x.strip('\n')
			y = y.strip('\n')
			dot.edge(x,y)
		dot.render('GrafoN1.dot', view=True) 

	def GraphvizN2(self):
		dot = Digraph(comment='Grafo referente ao N2')
		for vertice in self.lista_Vertices:
			x= str(vertice.matricula)
			print(x, vertice.nome)
			dot.node(x, vertice.nome)
		for aresta in self.lista_Arestas2:
			x, y = str(aresta.origem), str(aresta.destino)
			x = x.strip('\n')
			y = y.strip('\n')
			dot.edge(x,y)
		dot.render('GrafoN2.dot', view=True)    

	def GraphvizTotal(self):
		dot = Digraph(comment='Grafo com as relações N1 e N2')		
		for vertice in self.lista_Vertices:
			x= str(vertice.matricula)
			print(x, vertice.nome)
			dot.node(x, vertice.nome)
		for aresta in self.lista_Arestas_AuxTotal:
			x, y = str(aresta[0]), str(aresta[1])
			x = x.strip('\n')
			y = y.strip('\n')
			dot.edge(x,y)
		dot.render('GrafoTotal.dot', view=True)


	def busca_Vertice(self, identificador):  # Método recebe um int
		for i in self.lista_Vertices:
			if identificador == i.getmatricula():
				return i
		else:
			return None