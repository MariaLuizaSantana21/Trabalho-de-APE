def valida_int(pergunta, min, max):
    valor = int(input(pergunta))
    if valor < min or valor > max:
        valor = int(input(pergunta))
    return valor

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

#Programa Principal
while True:
    print("-" * 55)
    print("| MENU: ")
    print("| Para Código do Município e Código do cargo, digite: 1")
    print("| Para Código do candidato, digite: 2")
    print("| Sair, digite: 3")
    print("-" * 55)

    # Função para forçar apenas os valores de acesso contidos no menu
    opcao = valida_int("Opção desejada: ", 1, 3)

    # Condição para passar:
        # Código do Município/Código do cargo e chamar a função listar_candidatos
    if opcao == 1:
        SG_UE = input("Código do Muncípio: ")
        CD_CARGO = input("Código do Cargo: ")
    
    # Condição para passar:
        # Código do Candidato e chamar a função listar_informacao se o retorno do "if" for TRUE
    elif opcao == 2:
        SQ_CANDIDATO = input("Código do Candidato: ")
        if conferir_informacao(SQ_CANDIDATO):
            listar_informacao(SQ_CANDIDATO)
        else:
            print("CANDIDATO NÃO ENCONTRADO!")
    
    # Condição para encerrar o programa
    else:
        print("Encerrando programa...")
        break