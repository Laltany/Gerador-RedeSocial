from grafo import *

def main():
	print("Rodando!")
	#opcao = 0
	grafo = Grafo()
	opcao=0
	while opcao != 8:
		print("***********************************")
		print("Entre com a opcao:")
		print(" --- 1: Criar Grafo")
		print(" --- 2: Mostrar N1")
		print(" --- 3: Mostrar N2")
		print(" --- 4: Mostrar todas as relações")
		print(" --- 5: GraphvizN1")
		print(" --- 6: GraphvizN2")
		print(" --- 7: Graphviz Todas as relações")
		opcao = int(input("->"))
		if opcao == 1:
			for i in range(len(lista_arqs)):
				numero = lista_arqs[i].split(".")				
				nome = numero[0]				
				identifica = int(numero[0])	
				print(identifica)			
				grafo.novo_Vertice(identifica, nome)			
			grafo.nova_Aresta()
		if opcao == 2:			
			grafo.N1()
		if opcao == 3:
			grafo.N2()
		if opcao == 4:
			grafo.Total()
		if opcao== 5:
			grafo.GraphvizN1()
		if opcao == 6:
			grafo.GraphvizN2()
		if opcao == 7:
			grafo.GraphvizTotal()
if __name__ == "__main__":
	main()