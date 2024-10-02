def valida_int(pergunta, min, max):
    valor = int(input(pergunta))
    if valor < min or valor > max:
        valor = int(input(pergunta))
    return valor

#Segunda parte
def conferir_infor(SG_UE):
    try:
        arquivo = open("consulta_cand_2024_PB.csv", "r")
        codig = SG_UE
        for linha in arquivo:
            dados = linha.split(";")
            if dados[11].replace('"', '') == codig:
                return True
        return False
    finally:
        arquivo.close()

def listar_infor(SG_UE):
    arquivo = open("consulta_cand_2024_PB.csv", "r")
    codig = SG_UE
    for linha in arquivo:
        dados = linha.split(";")
        if dados[11].replace('"', '') == codig:
            print(f"Municipio escolhido:{dados[12]}")
            break
    arquivo.close() 


def conferir_inform(CD_CARGO):
    try:
        arquivo = open("consulta_cand_2024_PB.csv", "r")
        codig = CD_CARGO
        for linha in arquivo:
            dados = linha.split(";")
            if dados[13].replace('"', '') == codig:
                return True
        return False
    finally:
        arquivo.close()


def listar_inform(CD_CARGO, SG_UE):
    arquivo = open("consulta_cand_2024_PB.csv", "r")
    codig = CD_CARGO
    codig2=SG_UE
    for linha in arquivo:
        dados = linha.split(";")
        if dados[13].replace('"', '') == codig and dados[11].replace('"', '') == codig2:
            print(f"Nome do(a) candidato(a): {dados[17]}\nNome na urna: {dados[18]}\nNúmero: {dados[16]}\nPartido: {dados[26]}")
    arquivo.close()  

# Terceira parte
def conferir_informacao(CodC):
    try:
        arquivo = open("consulta_cand_2024_PB.csv", "r")
        codigo = CodC
        for linha in arquivo:
            dados = linha.split(";")
            if dados[15].replace('"', '') == codigo:
                return True
        return False
    finally:
        arquivo.close()
    
def listar_informacao(CodC):
    arquivo = open("consulta_cand_2024_PB.csv", "r")
    codigo = CodC
    for linha in arquivo:
        dados = linha.split(";")
        if dados[15].replace('"', '') == codigo:
            print(f"Nome do(a) candidato(a): {dados[17]}\nNome na urna: {dados[18]}\nNúmero: {dados[16]}\nPartido: {dados[26]}")
    arquivo.close()

#Biblioteca
import os
def abrir_pagina():
    os.system("start Estatisticas.html")

#Programa Principal
while True:
    print("-" * 25 + "MENU" + "-" * 25)
    print("| MENU: ")
    print("| Para Código do Município e Código do cargo, digite: 1")
    print("| Para Código do candidato, digite: 2")
    print("| Para Estatisticas eleições 2024, digite: 3")
    print("| Sair, digite: 4")
    print("-" * 54)

    # Função para forçar apenas os valores de acesso contidos no menu
    opcao = valida_int("Opção desejada: ", 1, 4)

    # Condição para passar:
        # Código do Município/Código do cargo e chamar as funções listar_irfor e listar_inform apenas se o retorno do "if" for TRUE
    if opcao == 1:
        SG_UE = input("Código do Muncípio: ")
        if conferir_infor(SG_UE):
            listar_infor(SG_UE)
        else:
            print("MUNICÍPIO NÃO ENCONTRADO!")
        CD_CARGO = input("Código do Cargo: ")
        if conferir_inform(CD_CARGO):
            listar_inform(CD_CARGO, SG_UE)

        else:
            print("cargo NÃO ENCONTRADO!")
        
    
    # Condição para passar:
        # Código do Candidato e chamar a função listar_informacao apenas se o retorno do "if" for TRUE
    elif opcao == 2:
        SQ_CANDIDATO = input("Código do Candidato: ")
        if conferir_informacao(SQ_CANDIDATO):
            listar_informacao(SQ_CANDIDATO)
        else:
            print("CANDIDATO NÃO ENCONTRADO!")

    #Estatisticas atuais
    elif opcao ==3:
         abrir_pagina()

    # Condição para encerrar o programa
    else:
        print("Encerrando programa...")
        break


#Bibliotecas
import pandas as pd
from datetime import datetime #importei conversao de dados para data

df = pd.read_csv('consulta_cand_2024_PB.csv', sep=';', encoding='latin1') #esse comando le o arquivo(encoding='latin1 identificao formato do arquivo)

candidatos_por_cargo = {}#lista vazia
partidos_prefeito = set()#esse comando cria um conjunto vazio
faixa_etaria = {
    'ate_21': 0,
    'entre_22_40': 0,
    'entre_41_60': 0,
    'acima_60': 0
}
total_candidatos = 0 #contador zerado
generos = {}
graus_instrucao = {}
estados_civis = {}


for index, row in df.iterrows():#retorna o valor das linhas em cara interaçao 
    cargo = row['DS_CARGO']
    partido = row['NM_PARTIDO']
    data_nascimento = row['DT_NASCIMENTO']
    genero = row['DS_GENERO']
    grau_instrucao = row['DS_GRAU_INSTRUCAO']
    estado_civil = row['DS_ESTADO_CIVIL']

for cargo in df['DS_CARGO']:#para cada cargo dentro da linha e colune de DS_CARGO contabilize mais um
 if cargo in candidatos_por_cargo:
        candidatos_por_cargo[cargo] += 1
 else:
        candidatos_por_cargo[cargo] = 1

for i, row in df.iterrows():#gera um iterador que retorna pares de valores em cada iteração
    if row['DS_CARGO'] == "PREFEITO": 
        partidos_prefeito.add(row['NM_PARTIDO'])#se for partido a prefeito ele adiciona o nome do partido a lista de candidatos a prefeito


df['DT_NASCIMENTO'] = pd.to_datetime(df['DT_NASCIMENTO'], format='%d/%m/%Y', errors='coerce')#formatei para ficar no tipo de data

# calculei a idade com base na data atual
hoje = datetime.now()#data de hoje
df['idade'] = hoje.year - df['DT_NASCIMENTO'].dt.year#calculei a data conforme a data de hoje e o ano de nascimento


for idade in df['idade']: #para cada idade que esta em idade verifique se... 
 if idade <= 21:
        faixa_etaria['ate_21'] += 1
 elif 22 <= idade <= 40:
        faixa_etaria['entre_22_40'] += 1
 elif 41 <= idade <= 60:
        faixa_etaria['entre_41_60'] += 1
 else:
        faixa_etaria['acima_60'] += 1

for genero in df['DS_GENERO']:#para cada genero que esta dentro de DS_GENERO contabilize 1 a aquele determinado genero

 if genero in generos:
        generos[genero] += 1
 else:
        generos[genero] = 1

for grau_instrucao in df['DS_GRAU_INSTRUCAO']:#para cada  grau que esta dentro de GRAU_INTRUÇAO contabilize 1 a aquele determinado grau  
 if grau_instrucao in graus_instrucao:
        graus_instrucao[grau_instrucao] += 1
 else:
        graus_instrucao[grau_instrucao] = 1

for estado_civil in df['DS_ESTADO_CIVIL']:#para cada estado civil contabiliza 1 a cada estado(solteiro,viuvo,casado,divorciado e separado)
   
 if estado_civil in estados_civis:
        estados_civis[estado_civil] += 1
 else:
        estados_civis[estado_civil] = 1

   
 total_candidatos += 1 #em cada interecao vai contabilizar um candidato independente das outras informaçoes

html = open('Estatisticas.html','w')
html.write('<html>\n')
html.write('<body>\n')
html.write('<ul>\n')
html.write('<h2>Candidatos por cargo</h2>\n')
    
    
for cargo in candidatos_por_cargo:
        quantidade = candidatos_por_cargo[cargo]#contabiliza a quantidade de individuos que exitem dentro de candidatos_por_cargo
        html.write(f'<li>{cargo}: {quantidade}</li>\n')
    
html.write('<h2>Partidos a Prefeito</h2>\n')
    
    
for partido in partidos_prefeito:
        html.write(f'<li>{partido}</li>\n')
    
html.write('<h2>Idades</h2>\n')
    
    
for faixa in faixa_etaria:
        quantidade = faixa_etaria[faixa]
        html.write(f'<li>{faixa}: {quantidade}</li>\n')
    
html.write('<h2>Total de candidatos</h2>\n')
html.write(f'<li>{total_candidatos}</li>\n')
    
html.write('<h2>Gêneros</h2><ul>\n')
    
   
for genero in generos:
        quantidade = generos[genero]
        html.write(f'<li>{genero}: {quantidade}</li>\n')
    
html.write('<h2>Grau de Instrução</h2>\n')
    
    
for grau in graus_instrucao:
        quantidade = graus_instrucao[grau]
        html.write(f'<li>{grau}: {quantidade}</li>\n')
    
html.write('<h2>Estado Civil</h2>\n')
    
    
    
for estado in estados_civis:
        quantidade = estados_civis[estado]
        html.write(f'<li>{estado}: {quantidade}</li>\n')

html.write('</ul>\n')
html.write('</body>\n')
html.write('</html>\n')
html.close()