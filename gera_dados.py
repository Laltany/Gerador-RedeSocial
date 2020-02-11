import sys
import os
from random import randint

diretorio = str(sys.argv[1])
quantidade = int(sys.argv[2])
inicio = int(sys.argv[3])
maxN1 = int(sys.argv[4])
maxN2 = int(sys.argv[5])
maximo= inicio + quantidade

provedor = ['@gmail.com', '@hotmail.com']

dir= './'+ diretorio
os.makedirs(dir)

nomes = open ('./info/nomes.txt', 'r')
nomes = nomes.readlines()
cursos = open ('./info/cursos.txt', 'r')
cursos = cursos.readlines()
estado = open ('./info/estados.txt', 'r')
estado = estado.readlines()
telefone = "\n"
j=0
inicio4= inicio
for i in range(quantidade):
	inicio2 = str(inicio4)
	matricula = inicio2 + "\n"
	nomearquivo = inicio2 + '.txt'
	dirarquivo= dir + "/" + nomearquivo 
	arquivo = open (dirarquivo, 'w')
	qtdNomes = int(len(nomes))	#Quantidade de nomes na lista
	random = randint(1, qtdNomes )
	qtdCursos = int(len(cursos)) #Quantidade de Cursos
	randomCurso = randint(0, 5 ) #curso aleatório
	randomEmail = randint(0, 1)
	randomestado= randint(0,26)	
	nome = nomes[random - 1].split("\n")
	tuplaemail = (nome[0], provedor[randomEmail])
	while j < 11:
		if j == 2:
			telefone+= " "
		numero = randint(0,9)
		numero = str(numero)
		telefone += numero
		j+=1
	email = "%s%s" %(tuplaemail[0], tuplaemail[1])
	listaN=[]
	inicio3=inicio
	for y in range(quantidade):
		listaN.append(inicio3)
		inicio3+=1



	ValidosN1= randint(3, maxN1)
	restoN1 = maxN1 - ValidosN1
	ValidosN2= randint(1, maxN2)
	restoN2 = maxN2 - ValidosN2
	qtdlista= int(len(listaN)) - 1


	arquivo.write(matricula)
	arquivo.write(nomes[random])
	arquivo.write(cursos[randomCurso])
	arquivo.write(email)
	arquivo.write(telefone)
	arquivo.write('\n')
	arquivo.write(estado[randomestado])
	for i in range(ValidosN1):
		posi = randint(0, qtdlista)
		valor= str(listaN[posi])
		if i == 0:
			arquivo.write(str(listaN[posi]))
		else:
			arquivo.write(', ')
			arquivo.write(str(listaN[posi]))
	for i in range(restoN1):
		aleatorio= maximo + randint(1, 10)
		aleatorio = str(aleatorio)
		arquivo.write(', ')
		arquivo.write(aleatorio)
	arquivo.write('\n')
	for i in range(ValidosN2):
		posi = randint(0, qtdlista)
		valor= str(listaN[posi])
		if i == 0:
			arquivo.write(str(listaN[posi]))
		else:
			arquivo.write(', ')
			arquivo.write(str(listaN[posi]))
	for i in range(restoN2):
		aleatorio= maximo + randint(1, 10)
		aleatorio = str(aleatorio)
		arquivo.write(', ')
		arquivo.write(aleatorio)
	arquivo.close()	
	inicio4 +=1
print("Todos os dados foram gerados com sucesso!")

	