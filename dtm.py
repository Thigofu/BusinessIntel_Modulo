#Importando o arquivo .CSV para analise em modo de leitura #
clientes = open('caa.csv', 'r')
#dividindo as linhas horizontalmente
Linhas = clientes.read().splitlines()
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

'''
OUTPUT:
['2018/05/20 11:37:26 AM GMT-3', '5', 'Sim', '19:00', '10 - 30 minutos', 'Onibus', 'Ubatuba', 'Sim', '1', 'mais de 1 hora', 'Sim', 'Requerimentos;;;;;']
'''

#=============================================== Contador de média da nota  ======================
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
#=============================================== Contador de média da nota  ======================

#======================================== Contador de média da nota telefonica  ======================
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
#========================================== Contador de média da nota telefonica  ======================

#========================================== Contador de solucao presencial =============================
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

#=========================================== Contador de solucao presencial =============================

#========================================== Contador de solucao telefonica =============================
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

#=========================================== Contador de solucao telefonica =============================

#======================================= Contador de localidade dos clientes ========================
ubatuba = 0 
caragua = 0
saoseba = 0 
paraibuna = 0
ilhabela = 0

for i in range(1, (Tamanholista), 1):
    Alinha = Linhas[i]
    #print(Alinha)
    ListaLinha = Alinha.split(',')

    if (ListaLinha[6] == "Ubatuba"):
        ubatuba += 1
    elif(ListaLinha[6] == "Caraguatatuba"):
        caragua +=1
    elif(ListaLinha[6] == "SÃ£o sebastiao"):
        saoseba +=1
    elif(ListaLinha[6] == "Paraibuna"):
        paraibuna += 1
    else:
        ilhabela +=1

print("Moradores de Ubatuba =",ubatuba," representam:",((ubatuba / Tamanholista)*100),"%")
print("Moradores de Caraguatatuba =",caragua," representam:",((caragua / Tamanholista)*100),"%")
print("Moradores de São sebastiao =",saoseba," representam:",((saoseba / Tamanholista)*100),"%")
print("Moradores de Paraibuna =",paraibuna," representam:",((paraibuna / Tamanholista)*100),"%")
print("Moradores de Ilhabela =",ilhabela," representam:",((ilhabela / Tamanholista)*100),"%")

#======================================== Contador de localidade dos clientes ========================

#======================================== Contador dos horarios de pico ===============================

hora1 = 0
hora2 = 0
hora3 = 0
hora4 = 0
hora5 = 0
hora6 = 0

for i in range(1, (Tamanholista), 1):
    Alinha = Linhas[i]
    #print(Alinha)
    ListaLinha = Alinha.split(',')

    if (ListaLinha[3] == "15:00"):
        hora1 += 1
    elif(ListaLinha[3] == "16:00"):
        hora2 +=1
    elif(ListaLinha[3] == "17:00"):
        hora3 +=1
    elif(ListaLinha[3] == "18:00"):
        hora4 +=1
    elif(ListaLinha[3] == "19:00"):
        hora5 += 1
    elif(ListaLinha[3] == "20:00"):
        hora6 +=1
    
print("Pessoas que frequentam no horario das 15:00:",hora1)
print("Pessoas que frequentam no horario das 16:00:",hora2)
print("Pessoas que frequentam no horario das 17:00:",hora3)
print("Pessoas que frequentam no horario das 18:00:",hora4)
print("Pessoas que frequentam no horario das 19:00:",hora5)
print("Pessoas que frequentam no horario das 20:00:",hora6)

#======================================== Contador dos horarios de pico ==============================

#======================================== Contador de transporte dos clientes ====================================
onibus = 0 
van = 0
carro = 0 
bicicleta = 0
outros = 0

for i in range(1, (Tamanholista), 1):
    Alinha = Linhas[i]
    #print(Alinha)
    ListaLinha = Alinha.split(',')

    if (ListaLinha[5] == "Onibus"):
        onibus += 1
    elif(ListaLinha[5] == "Carro"):
        carro +=1
    elif(ListaLinha[5] == "Bicicleta"):
        bicicleta +=1
    elif(ListaLinha[5] == "Van"):
        van += 1
    else:
        outros +=1

print("Clientes vindo de onibus =",onibus," representam:",((onibus / Tamanholista)*100),"%")
print("Clientes vindo de Carro =",carro," representam:",((carro / Tamanholista)*100),"%")
print("Clientes vindo de Bicicleta =",bicicleta," representam:",((bicicleta / Tamanholista)*100),"%")
print("Clientes vindo de Van =",van," representam:",((van / Tamanholista)*100),"%")
print("Clientes vindo de Outros =",outros," representam:",((outros / Tamanholista)*100),"%")
#======================================== Contador de transporte dos clientes ====================================

#======================================== Contador de tempo de demora atendimento presencial ====================================
resp1 = 0 
resp2= 0
resp3 = 0 
resp4 = 0
resp5 = 0

for i in range(1, (Tamanholista), 1):
    Alinha = Linhas[i]
    #print(Alinha)
    ListaLinha = Alinha.split(',')

    if (ListaLinha[4] == "menos de 10 minutos"):
        resp1 += 1
    elif(ListaLinha[4] == "10 - 30 minutos"):
        resp2 +=1
    elif(ListaLinha[4] == "30 - 45 minutos"):
        resp3 +=1
    elif(ListaLinha[4] == "mais de 1 hora"):
        resp4 += 1
    else:
        resp5 +=1

print("atendimentos que demoram menos de 10 minutos =",resp1," representam:",((resp1 / Tamanholista)*100),"%")
print("atendimentos que demoram de 10 a 30 minutos =",resp2," representam:",((resp2 / Tamanholista)*100),"%")
print("atendimentos que demoram de 30 a 45 minutos =",resp3," representam:",((resp3 / Tamanholista)*100),"%")
print("atendimentos que demoram 1 hora =",resp4," representam:",((resp4 / Tamanholista)*100),"%")
print("atendimentos que demoram mais de 1 hora =",resp5," representam:",((resp5 / Tamanholista)*100),"%")
