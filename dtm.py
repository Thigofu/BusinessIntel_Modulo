#Importando a biblioteca para criação de graficos visuais
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import time

#função que faz a conversão para porcentagem e exibe texto nos graficos
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct
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
grafnotsolbol = boleto
grafnotsolcarimbo = carimbo
grafnotsolrequ = requerimento
grafnotsolprob = problema
grafnotsoldoc = documentos
grafnotsoltranc = trancamento
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
grafnotsolcelbol = boleto
grafnotsolcelcarimbo = carimbo
grafnotsolcelrequ = requerimento
grafnotsolcelprob = problema
grafnotsolceldoc = documentos
grafnotsolceltranc = trancamento

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

pcresp1 = ((resp1 / Tamanholista)*100)
pcresp2 = ((resp2 / Tamanholista)*100)
pcresp3 = ((resp3 / Tamanholista)*100)
pcresp4 = ((resp4 / Tamanholista)*100)
pcresp5 = ((resp5 / Tamanholista)*100)
print("atendimentos que demoram menos de 10 minutos =",resp1," representam:",pcresp1,"%")
print("atendimentos que demoram de 10 a 30 minutos =",resp2," representam:",pcresp2,"%")
print("atendimentos que demoram de 30 a 45 minutos =",resp3," representam:",pcresp3,"%")
print("atendimentos que demoram 1 hora =",resp4," representam:",pcresp4,"%")
print("atendimentos que demoram mais de 1 hora =",resp5," representam:",pcresp5,"%\n")

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
pcrespcel1 = ((resp1 / Tamanholista)*100)
pcrespcel2 = ((resp2 / Tamanholista)*100)
pcrespcel3 = ((resp3 / Tamanholista)*100)
pcrespcel4 = ((resp4 / Tamanholista)*100)
pcrespcel5 = ((resp5 / Tamanholista)*100)



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
grafservbol = boleto
grafservcar = carimbo
grafservreq = requerimento
grafservprob = problema
grafservdoc = documentos
grafservtranc = trancamento
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


#=============================================================================================================================================
#                                                            SETOR DOS GRAFICOS                                                                         
#=============================================================================================================================================

#=====================================Grafico de Pizza das soluções=======================================================
nomes = 'Sim', 'Não'
tamanho = [porcentosim , porcentonao ]
fig1, grafsol = plt.subplots()
grafsol.set_title("Contagem de solução presencial")
grafsol.pie(tamanho, autopct='%1.1f%%',shadow=False, startangle=90)
grafsol.axis('equal')  # Equal deixa o grafico sem ficar distorcido.
grafsol.legend(nomes)
#=====================================Grafico de Pizza das soluções=======================================================


#=====================================Grafico de Pizza das soluções Telefonicas=======================================================
nomes = 'Sim', 'Não'
tamanho = [porcentocelsim , porcentocelnao ]
fig2, grafsolcel = plt.subplots()
grafsolcel.set_title("Contagem de solução Telefonica")
grafsolcel.pie(tamanho, autopct='%1.1f%%',shadow=False, startangle=90)
grafsolcel.axis('equal')  # Equal deixa o grafico sem ficar distorcido.
grafsolcel.legend(nomes)
#=====================================Grafico de Pizza das soluções Telefonicas=======================================================

#=====================================Grafico de Pizza do tempo demora solucoes=======================================================
nomes = '< 10 minutos', '10 - 30 minutos', '30 - 45 minutos', '1 hora', '> 1 hora'
tamanho = [pcresp1, pcresp2, pcresp3, pcresp4, pcresp5  ]
fig3, grafdemora = plt.subplots()
grafdemora.set_title("Tempo de demora para ser atendido presencialmente")
grafdemora.pie(tamanho, autopct='%1.1f%%',shadow=False, startangle=90)
grafdemora.axis('equal')  # Equal deixa o grafico sem ficar distorcido.
grafdemora.legend(nomes)
#=====================================Grafico de Pizza do tempo demora solucoes=======================================================

#=====================================Grafico de Pizza do tempo demora solucoes=======================================================
nomes = '< 10 minutos', '10 - 30 minutos', '30 - 45 minutos', '1 hora', '> 1 hora'
tamanho = [pcrespcel1, pcrespcel2, pcrespcel3, pcrespcel4, pcrespcel5  ]
fig4, grafdemoracel = plt.subplots()
grafdemoracel.set_title("Tempo de demora para ser atendido no telefone")
grafdemoracel.pie(tamanho, autopct='%1.1f%%',shadow=False, startangle=90)
grafdemoracel.axis('equal')  # Equal deixa o grafico sem ficar distorcido.
grafdemoracel.legend(nomes)

#===================================== Grafico Pizza do meio de transporte======================================
nomes = 'Onibus', 'Carro', 'Van', 'Bicicleta', 'Outros'
tamanho = [onibus,carro,van ,bicicleta ,outros]
fig5, transporte = plt.subplots()
transporte.set_title("Meios de Transporte dos clientes")
transporte.pie(tamanho, autopct=make_autopct(tamanho),shadow=False, startangle=90)
transporte.axis('equal')  # Equal deixa o grafico sem ficar distorcido.
transporte.legend(nomes)
#===================================== Grafico Pizza do meio de transporte======================================

#===================================== Grafico Pizza das mudanças solicitadas======================================
nomes = 'Equipe', 'Equipamentos', 'Procedimentos', 'Coordenação'
tamanho = [equipe,equipamentos,procedimentos ,coordenacao]
fig6, sugestao = plt.subplots()
sugestao.set_title("Mudanças Solicitadas pelos funcionarios")
sugestao.pie(tamanho,autopct=make_autopct(tamanho),shadow=False, startangle=90)
sugestao.axis('equal')  # Equal deixa o grafico sem ficar distorcido.
sugestao.legend(nomes)
#===================================== Grafico Pizza das mudanças solicitadas======================================

#===================================== Grafico Pizza dos dias da semana======================================
nomes = 'Segunda', 'Terça', 'Quarta', 'Quinta','Sexta'
tamanho = [segunda,terca,quarta ,quinta,sexta]
fig7, diagraf = plt.subplots()
diagraf.set_title("Relação de dia da semana que o pessoal mais frequenta o CAA\n*Segundo os funcionarios")
diagraf.pie(tamanho,autopct=make_autopct(tamanho),shadow=False, startangle=90)
diagraf.axis('equal')  # Equal deixa o grafico sem ficar distorcido.
diagraf.legend(nomes)
#===================================== Grafico Pizza dos dias da semana======================================

#===================================== Grafico Pizza das semanas do mês======================================
nomes = '1° semana', '2° semana', '3° semana', '4° semana',
tamanho = [sem1,sem2,sem3 ,sem4]
fig8, semanames = plt.subplots()
semanames.set_title("Relação das semanas onde o CAA tem maior movimento\n*Segundo os funcionarios")
semanames.pie(tamanho,autopct=make_autopct(tamanho),shadow=False, startangle=90)
semanames.axis('equal')  # Equal deixa o grafico sem ficar distorcido.
semanames.legend(nomes)
#===================================== Grafico Pizza das semanas do mês======================================

#===================================== Grafico Pizza das horarios de frequencia======================================
nomes = '15:00h', '16:00h', '17:00h', '18:00h','19:00h','20:00h'
tamanho = [hora1,hora2,hora3 ,hora4,hora5,hora6]
fig9, semanames = plt.subplots()
semanames.set_title("Horario que os clientes costumam frequentar o CAA")
semanames.pie(tamanho,autopct=make_autopct(tamanho),shadow=False, startangle=90)
semanames.axis('equal')  # Equal deixa o grafico sem ficar distorcido.
semanames.legend(nomes)
#===================================== Grafico Pizza das horarios de frequencia======================================

#===================================== Grafico Pizza de satisfação dos funcionarios======================================
nomes = 'Sim', 'Não'
tamanho = [contadorlikefunc, contadordislikefunc]
fig10, gostatrabalho = plt.subplots()
gostatrabalho.set_title("Relação dos funcionarios que gostam de trabalhar no CAA")
gostatrabalho.pie(tamanho,autopct=make_autopct(tamanho),shadow=False, startangle=90)
gostatrabalho.axis('equal')  # Equal deixa o grafico sem ficar distorcido.
gostatrabalho.legend(nomes)
#===================================== Grafico Pizza de satisfação dos funcionarios======================================

#===================================== Grafico Pizza de satisfação dos funcionarios======================================
nomes = 'Sim', 'Não'
tamanho = [contadorsatifacao, contadorinsatisfacao]
fig11, gostacaa = plt.subplots()
gostacaa.set_title("Relação da satisfação dos funcionarios com a situação do CAA")
gostacaa.pie(tamanho,autopct=make_autopct(tamanho),shadow=False, startangle=90)
gostacaa.axis('equal')  # Equal deixa o grafico sem ficar distorcido.
gostacaa.legend(nomes)
#===================================== Grafico Pizza de satisfação dos funcionarios======================================

#===================================== Grafico Pizza dos problemas não resolvidos presencialmente======================================
nomes = 'Boletos', 'Carimbo/Passe escolar','Requerimentos','Problema com matricula','Documentos','Cancelamento/Trancamento de matricula'
tamanho = [grafnotsolbol, grafnotsolcarimbo,grafnotsolrequ,grafnotsolprob,grafnotsoldoc,grafnotsoltranc]
fig12, notsolve = plt.subplots()
notsolve.set_title("Relação dos serviços que não foram solucionados presencialmente")
notsolve.pie(tamanho,labels =nomes,autopct=make_autopct(tamanho),shadow=False, startangle=90)
notsolve.axis('equal')  # Equal deixa o grafico sem ficar distorcido.


#===================================== Grafico Pizza dos problemas não resolvidos no telefone======================================
nomes = 'Boletos', 'Carimbo/Passe escolar','Requerimentos','Problema com matricula','Documentos','Cancelamento/Trancamento de matricula'
tamanho = [grafnotsolcelbol, grafnotsolcelcarimbo,grafnotsolcelrequ,grafnotsolcelprob,grafnotsolceldoc,grafnotsolceltranc]
fig13, notsolvecel = plt.subplots()
notsolvecel.set_title("Relação dos serviços que não foram solucionados presencialmente")
notsolvecel.pie(tamanho,labels = nomes,autopct=make_autopct(tamanho),shadow=False, startangle=90)
notsolvecel.axis('equal')  # Equal deixa o grafico sem ficar distorcido.

#===================================== Grafico Pizza dos problemas não resolvidos no telefone======================================
nomes = 'Boletos', 'Carimbo/Passe escolar','Requerimentos','Problema com matricula','Documentos','Cancelamento/Trancamento de matricula'
tamanho = [grafservbol, grafservcar,grafservreq,grafservdoc,grafservprob,grafservtranc]
fig14, grafserv = plt.subplots()
grafserv.set_title("Relação dos serviços solicitados pelos clientes")
grafserv.pie(tamanho,labels = nomes,autopct=make_autopct(tamanho),shadow=False, startangle=90)
grafserv.axis('equal')  # Equal deixa o grafico sem ficar distorcido.


#==========================================Salvando os graficos em um PDF==============================================
pp = PdfPages('relatorio.pdf') #cria um PDF com o nome "relatório.pdf
pp.savefig(fig14)#Relação dos serviços solicitados ao CAA (total)
pp.savefig(fig1) #Contagem de solução 
pp.savefig(fig12) #Relação problemas não resolvidos presencialmente
pp.savefig(fig3) #Tempo de demora para ser atendido presencialmente

pp.savefig(fig2) #Contagem de solução Telefonica
pp.savefig(fig13) #Relação problemas não resolvidos no telefone
pp.savefig(fig4) #Tempo de demora para ser atendido no telefone

pp.savefig(fig9) #Horario que os clientes costumam frequentar o CA
pp.savefig(fig7) #Relação de dia da semana que o pessoal mais frequenta o CAA
pp.savefig(fig8) #Relação das semanas onde o CAA tem maior movimento
pp.savefig(fig5) #Meios de Transporte dos clientes

pp.savefig(fig10)#Relação dos funcionarios que gostam de trabalhar no CAA
pp.savefig(fig11)#Relação da satisfação dos funcionarios com a situação do CAA
pp.savefig(fig6) #Mudanças Solicitadas pelos funcionarios

'''
Codigo criado com intuição de fazer o datamining
PDF acabou sendo criado por pagina separada,infelizmente o Join das paginas não teve tempo o suficiente para ser estudado
O codigo esta disponivel no Github através do seguinte nome e link
-------------------------------------------------------------------------------------------------------
Thigofu/BusinessIntel_Modulo 
https://github.com/Thigofu/BusinessIntel_Modulo
'''
pp.close() #encerra o processo salvando o PDF com o conteudo inserido
#==========================================Salvando os graficos em um PDF==============================================
