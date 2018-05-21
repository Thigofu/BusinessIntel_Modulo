#Importando o arquivo .CSV para analise em modo de leitura #
myFile = open('caa.csv', 'r')
#dividindo as linhas horizontalmente
Linhas = myFile.read().splitlines()
#Determina o tamanho da lista
Tamanholista = len(Linhas)
print("A lista contem:",Tamanholista - 1,"Linhas" )
#===============================================================
#PRIMEIRO ITEM DE UMA LISTA
Alinha = Linhas[1]
ListaLinha = Alinha.split(',')
#print(ListaLinha)
nota = ListaLinha[1] # O segundo item da lista sempre vai ser as notas
#print(nota)
#print(type(nota))
#PRIMEIRO ITEM DE UMA LISTA
soma = 0

#=============== Contador de média da nota  ======================
soma = 0
for i in range(1, (Tamanholista), 1):
    Alinha = Linhas[i]
    #print(Alinha)
    ListaLinha = Alinha.split(',')
    #print(ListaLinha)
    nota = ListaLinha[1] # O segundo item da lista sempre vai ser as notas
    #print(nota)
    #print(type(nota))
    notafloat = float(nota)
    soma = soma + notafloat
media = soma / Tamanholista
print("media da nota presencial:",media)
#=============== Contador de média da nota  ======================

#=============== Contador de média da nota telefonica  ======================
soma = 0
for i in range(1, (Tamanholista), 1):
    Alinha = Linhas[i]
    #print(Alinha)
    ListaLinha = Alinha.split(',')
    #print(ListaLinha)
    notacel = ListaLinha[8] # O segundo item da lista sempre vai ser as notas
    #print(nota)
    #print(type(nota))
    notacelfloat = float(notacel)
    soma = soma + notacelfloat

media = soma / Tamanholista
print("media da nota telefonica: ",media)
#=============== Contador de média da nota telefonica  ======================

#=============== Contador de solucao presencial =============================
contadorsim = 0
contadornao = 0
for i in range(1, (Tamanholista), 1):
    Alinha = Linhas[i]
    #print(Alinha)
    ListaLinha = Alinha.split(',')

    if (ListaLinha[2] == "Sim"):
        contadorsim += 1
    else:
        contadornao +=1

porcentosim = (contadorsim / Tamanholista) * 100
porcentonao = (contadornao / Tamanholista) * 100
print("Total de atendimentos presenciais solucionados =", contadorsim,"Que equivalem a",round(porcentosim),"%")
print("Total de atendimentos presenciais não solucionados =", contadornao,"Que equivalem a",round(porcentonao),"%")

#=============== Contador de solucao presencial =============================

#=============== Contador de solucao telefonica =============================
contadorcelsim = 0
contadorcelnao = 0
for i in range(1, (Tamanholista), 1):
    Alinha = Linhas[i]
    #print(Alinha)
    ListaLinha = Alinha.split(',')

    if (ListaLinha[10] == "Sim"):
        contadorcelsim += 1
    else:
        contadorcelnao +=1

porcentocelsim = (contadorcelsim / Tamanholista) * 100
porcentocelnao = (contadorcelnao / Tamanholista) * 100
print("Total de atendimentos telefonicos solucionados =", contadorcelsim,"Que equivalem a",round(porcentocelsim),"%")
print("Total de atendimentos telefonicos não solucionados =", contadorcelnao,"Que equivalem a",round(porcentocelnao),"%")

#=============== Contador de solucao telefonica =============================