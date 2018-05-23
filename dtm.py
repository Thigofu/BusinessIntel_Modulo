#Importando o arquivo .CSV para analise em modo de leitura #
clientes = open('clientes.csv', 'r')
funcionarios = open('func.csv', 'r')

#dividindo as linhas horizontalmente
Linhas = clientes.read().splitlines()
Linhasfunc = funcionarios.read().splitlines()

#Determina o tamanho da lista
Tamanholista = len(Linhas)
Tamanholistafunc = len(Linhasfunc)
print("A lista clientes contem:",Tamanholista - 1,"Linhas\n" )
print("A lista funcionarios contem:",Tamanholistafunc - 1,"Linhas\n" )

#=============================================================================================================================================================
#PRIMEIRO ITEM DA LISTA CLIENTES
Alinha = Linhas[1]
ListaLinha = Alinha.split(',')
#print(ListaLinha)
nota = ListaLinha[1] # O segundo item da lista sempre vai ser as notas
#print(nota)
#print(type(nota))
#PRIMEIRO ITEM DE UMA LISTA


'''
OUTPUT:
['2018/05/20 11:37:26 AM GMT-3', '5', 'Sim', '19:00', '10 - 30 minutos', 'Onibus', 'Ubatuba', 'Sim', '1', 'mais de 1 hora', 'Sim', 'Requerimentos']
'''
#=============================================================================================================================================================

#PRIMEIRO ITEM DA LISTA FUNCIONARIOS
Alinhafunc = Linhasfunc[1]
ListaLinhafunc = Alinhafunc.split(',')
print(ListaLinhafunc[1]) #printa o primeiro item da lista(no caso os dias de lotação do CAA)

#OUTPUT
# ['Segunda;Sexta']
#PRIMEIRO ITEM DA LISTA FUNCIONARIOS

#=============================================================================================================================================================



#=============================================== Contador de média da nota  ======================
print("=============================Medias dos atendimentos==============================")
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
print("media da nota telefonica: ",media,"\n\n")
#========================================== Contador de média da nota telefonica  ======================

#========================================== Contador de solucao presencial =============================
print("#========================================== Contador de solucao =============================")
contadorsim = 0
contadornao = 0
boleto = 0 
carimbo = 0
requerimento = 0 
problema = 0
documentos = 0
trancamento = 0


for i in range(1, (Tamanholista), 1):
    Alinha = Linhas[i]
    #print(Alinha)
    ListaLinha = Alinha.split(',')
    servicos = ListaLinha[11].split(';')

    if (ListaLinha[2] == "Sim"):
        contadorsim += 1
    if (ListaLinha[2] == "Nao"):
        contadornao +=1
        for j in range (0 ,len(servicos), 1):
            if (servicos[j] == "Boletos"):
                boleto += 1
            if (servicos[j] == "Requerimentos"):
                requerimento += 1
            if (servicos[j] == "Carimbo/Passe escolar"):
                carimbo += 1
            if (servicos[j] == "Problemas com matricula"):
                problema += 1
            if (servicos[j] == "Entrega/retirada de documentos"):
                documentos += 1
            if (servicos[j] == "Cancelamento/Trancamento de matricula"):
                trancamento += 1


porcentosim = (contadorsim / Tamanholista) * 100
porcentonao = (contadornao / Tamanholista) * 100
print("Total de atendimentos presenciais solucionados =", contadorsim,"Que equivalem a",round(porcentosim),"%")
print("Total de atendimentos presenciais não solucionados =", contadornao,"Que equivalem a",round(porcentonao),"%\n")
print("Dos",contadornao,"casos não solucionados:")
print(boleto,"Eram Boletos")
print(carimbo,"Eram Carimbos/Passe escolar")
print(requerimento,"Eram Requerimentos")
print(problema,"Eram Problemas com matricula")
print(documentos,"Eram Entrega/Retirada documentos")
print(trancamento,"Eram trancamento/Cancelamento de matricula\n\n")

#=========================================== Contador de solucao presencial =============================

#========================================== Contador de solucao telefonica =============================
contadorcelsim = 0
contadorcelnao = 0
boleto = 0 
carimbo = 0
requerimento = 0 
problema = 0
documentos = 0
trancamento = 0

for i in range(1, (Tamanholista), 1):
    Alinha = Linhas[i]
    #print(Alinha)
    ListaLinha = Alinha.split(',')
    servicos = ListaLinha[11].split(';')

    if (ListaLinha[10] == "Sim"):
        contadorcelsim += 1
    if (ListaLinha[10] == "Nao"):
        contadorcelnao +=1
        for j in range (0 ,len(servicos), 1):
            if (servicos[j] == "Boletos"):
                boleto += 1
            if (servicos[j] == "Requerimentos"):
                requerimento += 1
            if (servicos[j] == "Carimbo/Passe escolar"):
                carimbo += 1
            if (servicos[j] == "Problemas com matricula"):
                problema += 1
            if (servicos[j] == "Entrega/retirada de documentos"):
                documentos += 1
            if (servicos[j] == "Cancelamento/Trancamento de matricula"):
                trancamento += 1

porcentocelsim = (contadorcelsim / Tamanholista) * 100
porcentocelnao = (contadorcelnao / Tamanholista) * 100
print("Total de atendimentos telefonicos solucionados =", contadorcelsim,"Que equivalem a",round(porcentocelsim),"%")
print("Total de atendimentos telefonicos não solucionados =", contadorcelnao,"Que equivalem a",round(porcentocelnao),"%\n\n")
print("Dos",contadorcelnao,"casos não solucionados:")
print(boleto,"Eram Boletos")
print(carimbo,"Eram Carimbos/Passe escolar")
print(requerimento,"Eram Requerimentos")
print(problema,"Eram Problemas com matricula")
print(documentos,"Eram Entrega/Retirada documentos")
print(trancamento,"Eram trancamento/Cancelamento de matricula\n\n")

#=========================================== Contador de solucao telefonica =============================

#======================================= Contador de localidade dos clientes ========================
print("#======================================= Contador de localidade dos clientes ========================")
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
        ubatuba += 1 # ubatuba = ubatuba + 1
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
print("Moradores de Ilhabela =",ilhabela," representam:",((ilhabela / Tamanholista)*100),"%\n\n")

#======================================== Contador de localidade dos clientes ========================

#======================================== Contador dos horarios de pico ===============================
print("#======================================== Contador dos horarios e dias de pico ===============================\n")
hora1 = 0
hora2 = 0
hora3 = 0
hora4 = 0
hora5 = 0
hora6 = 0
segunda = 0
terca = 0
quarta = 0
quinta = 0
sexta = 0
sem1 = 0
sem2 = 0
sem3 = 0
sem4 = 0

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

for i in range(1, (Tamanholistafunc), 1):
    Alinhafunc = Linhasfunc[i]
    #print(Alinhafunc)
    ListaLinhafunc = Alinhafunc.split(',')
    dias = ListaLinhafunc[1].split(';')
    semana = ListaLinhafunc[2].split(';')

    for j in range (0,(len(dias)), 1):
        if (dias[j] == "Segunda"):
            segunda += 1
        if (dias[j] == "Terça"):
            terca += 1
        if (dias[j] == "Quarta"):
            quarta += 1
        if (dias[j] == "Quinta"):
            quinta += 1
        if (dias[j] == "Sexta"):
            sexta += 1
    
    for k in range (0, (len(semana)),1):
        if (semana[k] == "Primeira semana"):
            sem1 += 1
        if (semana[k] == "Segunda semana"):
            sem2 += 1
        if (semana[k] == "Terceira semana"):
            sem3 += 1
        if (semana[k] == "Quarta semana"):
            sem4 += 1




    
print("Pessoas que frequentam no horario das 15:00 -->",hora1," representam:",((hora1 / Tamanholista)*100),"%")
print("Pessoas que frequentam no horario das 16:00 -->",hora2," representam:",((hora2 / Tamanholista)*100),"%")
print("Pessoas que frequentam no horario das 17:00 -->",hora3," representam:",((hora3 / Tamanholista)*100),"%")
print("Pessoas que frequentam no horario das 18:00 -->",hora4," representam:",((hora4 / Tamanholista)*100),"%")
print("Pessoas que frequentam no horario das 19:00 -->",hora5," representam:",((hora5 / Tamanholista)*100),"%")
print("Pessoas que frequentam no horario das 20:00 -->",hora6," representam:",((hora6 / Tamanholista)*100),"%\n\n")
print("contagem dos dias de lotação:")
print("Segunda feira =",segunda)
print("Terça feira =",terca)
print("Quarta feira =", quarta)
print("Quinta feira =", quinta)
print("Sexta feira =",sexta,"\n\n")
print("Contagem das semanas de pico:")
print("Primeira semana =",sem1)
print("Segunda semana =",sem2)
print("Terceira semana =",sem3)
print("Quarta semana =",sem4)

#======================================== Contador dos horarios de pico ==============================

#======================================== Contador de transporte dos clientes ====================================
print("#======================================== Contador de meios de transporte ====================================\n")
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
print("Clientes vindo de Outros =",outros," representam:",((outros / Tamanholista)*100),"% \n\n")
#======================================== Contador de transporte dos clientes ====================================

#======================================== Contador de tempo de demora atendimento presencial ====================================
print("#======================================== Contador de tempo de demora dos atendimentos ====================================\n")
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
print("atendimentos que demoram mais de 1 hora =",resp5," representam:",((resp5 / Tamanholista)*100),"%\n")

#======================================== Contador de tempo de demora atendimento presencial ====================================


#======================================== Contador de tempo de demora atendimento telefonico ====================================
resp1 = 0 
resp2= 0
resp3 = 0 
resp4 = 0
resp5 = 0

for i in range(1, (Tamanholista), 1):
    Alinha = Linhas[i]
    #print(Alinha)
    ListaLinha = Alinha.split(',')

    if (ListaLinha[9] == "menos de 10 minutos"):
        resp1 += 1
    elif(ListaLinha[9] == "10 - 30 minutos"):
        resp2 +=1
    elif(ListaLinha[9] == "30 - 45 minutos"):
        resp3 +=1
    elif(ListaLinha[9] == "mais de 1 hora"):
        resp4 += 1
    else:
        resp5 +=1

print("atendimentos telefonicos que demoram menos de 10 minutos =",resp1," representam:",((resp1 / Tamanholista)*100),"%")
print("atendimentos telefonicos que demoram de 10 a 30 minutos =",resp2," representam:",((resp2 / Tamanholista)*100),"%")
print("atendimentos telefonicos que demoram de 30 a 45 minutos =",resp3," representam:",((resp3 / Tamanholista)*100),"%")
print("atendimentos telefonicos que demoram 1 hora =",resp4," representam:",((resp4 / Tamanholista)*100),"%")
print("atendimentos telefonicos que demoram mais de 1 hora =",resp5," representam:",((resp5 / Tamanholista)*100),"%\n")
#======================================== Contador de tempo de demora atendimento telefonico ====================================

#======================================== Contador de serviços solicitados ======================================================
print("#======================================== Contador de serviços solicitados ======================================================\n")
boleto = 0 
carimbo = 0
requerimento = 0 
problema = 0
documentos = 0
trancamento = 0

for i in range(1, (Tamanholista), 1):
    Alinha = Linhas[i]
    #print(Alinha)
    ListaLinha = Alinha.split(',')
    servicos = ListaLinha[11].split(';')

    for j in range (0 ,len(servicos), 1):
        if (servicos[j] == "Boletos"):
            boleto += 1
        if (servicos[j] == "Requerimentos"):
            requerimento += 1
        if (servicos[j] == "Carimbo/Passe escolar"):
            carimbo += 1
        if (servicos[j] == "Problemas com matricula"):
            problema += 1
        if (servicos[j] == "Entrega/retirada de documentos"):
            documentos += 1
        if (servicos[j] == "Cancelamento/Trancamento de matricula"):
            trancamento += 1

print("Boletos =",boleto)
print("Carimbos/Passe Escolar =",carimbo)
print("Requerimentos =",requerimento)
print("Problemas com matricula =",problema)
print("Entrega/Retirada Documentos =",documentos)
print("Cancelamento/Trancamento Matricula =",trancamento)

#======================================== Contador de satisfacao dos funcionarios ======================================================
print("#======================================== Contador de satisfacao dos funcionarios ======================================================")

contadorlikefunc = 0
contadordislikefunc = 0
contadorsatifacao = 0
contadorinsatisfacao = 0

for i in range (1, Tamanholistafunc, 1):
    Alinhafunc = Linhasfunc[i]
    #print(Alinhafunc)
    ListaLinhafunc = Alinhafunc.split(',')
    #print(ListaLinhafunc)

    if (ListaLinhafunc[3] == "Sim"):
        contadorlikefunc += 1
    if (ListaLinhafunc[3] == "NÃ£o"):
        contadordislikefunc +=1
    if (ListaLinhafunc[4] == "Sim"):
        contadorsatifacao += 1
    if (ListaLinhafunc[4] == "NÃ£o"):
        contadorinsatisfacao += 1

print("Funcionarios que gostam de trabalhar no CAA =",contadorlikefunc,"representam:",((contadorlikefunc / (Tamanholistafunc -1))*100))
print("Funcionarios que não gostam de trabalhar no CAA =",contadordislikefunc,"representam:",((contadordislikefunc / (Tamanholistafunc -1))*100),"%\n\n")

print("Funcionarios que gostam da situação do CAA =",contadorsatifacao,"representam:",((contadorsatifacao / (Tamanholistafunc -1))*100))
print("Funcionarios que não gostam da situação do CAA =",contadorinsatisfacao,"representam:",((contadorinsatisfacao / (Tamanholistafunc -1))*100))

#======================================== Contador de satisfacao dos funcionarios ======================================================

#======================================== Contador de mudanças sugeridas ======================================================
print("#======================================== Contador de mudanças sugeridas pelos funcionarios =====================================\n\n")
equipe = 0
equipamentos = 0
procedimentos = 0
coordenacao = 0


for i in range (1, Tamanholistafunc, 1):
    Alinhafunc = Linhasfunc[i]
    #print(Alinhafunc)
    ListaLinhafunc = Alinhafunc.split(',')
    #print(ListaLinhafunc)
    mudancas = ListaLinhafunc[6].split(';')
    
    
    for j in range (0 ,len(mudancas), 1):
        if (mudancas[j] == "Equipe"):
            equipe += 1
        if (mudancas[j] == "Equipamentos"):
            equipamentos += 1
        if (mudancas[j] == "Procedimentos"):
            procedimentos += 1
        if (mudancas[j] == "CoordenaÃ§Ã£o"):
            coordenacao += 1

#print(equipe,equipamentos,procedimentos,coordenacao)
print("Contagem de mudanças sugeridas:")
print("Equipe:",equipe)
print("Equipamentos:", equipamentos)
print("Procedimentos:", procedimentos)
print("Coordenação:",coordenacao)
