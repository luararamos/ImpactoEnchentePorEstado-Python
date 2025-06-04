# Lista com os nomes dos estados disponíveis para análise
listaCidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Porto Alegre", "Recife"]

# Lista com os valores máximos de chuva (em mm) que cada estado suporta antes de risco de enchente
chuvaSuportado = [70, 60, 55, 80 , 50]

# Função que exibe um mapa ASCII do estado de São Paulo
def mostrar_mapa_sao_paulo():
    mapa = r""" ... (mapa omitido para facilitar leitura) """
    print(mapa)

# Função que exibe o mapa do estado do Rio de Janeiro
def mostrar_mapa_rio_de_janeiro():
    mapa = """ ... """
    print(mapa)

# Função que exibe o mapa do estado da Bahia
def mostrar_mapa_bahia():
    mapa = """ ... """
    print(mapa)

# Função que exibe o mapa do estado do Paraná
def mostrar_mapa_parana():
    mapa = """ ... """
    print(mapa)

# Função que exibe o mapa do estado de Pernambuco
def mostrar_mapa_pernambuco():
    mapa = """ ... """
    print(mapa)

# Exibe o menu com as opções de estados para o usuário escolher
def mostrar_menu():
    print("\n==============================")
    print(" Selecione um estado para análise de chuvas:")
    print(" 1 - São Paulo")
    print(" 2 - Rio de Janeiro")
    print(" 3 - Bahia")
    print(" 4 - Paraná")
    print(" 5 - Pernambuco")
    print("==============================")

# Define os limites de chuva suportada por estado (repetido aqui por segurança)
chuvaSuportado = [70, 60, 55, 80, 50]

# Função genérica para validar qualquer número informado pelo usuário
def validar_numero(texto_input, tipo=float, minimo=0, maximo=None):
    validado = False
    while not validado:
        valor_str = input(texto_input)

        # Validação para números inteiros
        if tipo == int:
            if valor_str.isdigit():
                valor = int(valor_str)
            else:
                print("⚠️   Entrada inválida! Digite um número inteiro positivo válido.\n")
                continue

        # Validação para números decimais (floats)
        elif tipo == float:
            partes = valor_str.split('.')
            if len(partes) > 2:
                print("⚠️   Entrada inválida! Digite um número decimal positivo válido.\n")
                continue
            if all(p.isdigit() for p in partes):
                valor = float(valor_str)
            else:
                print("⚠️   Entrada inválida! Digite um número decimal positivo válido.\n")
                continue
        else:
            print("⚠️   Tipo inválido para validação.")
            return None

        # Verifica se está dentro dos limites mínimo e máximo
        if valor < minimo:
            print(f"⚠️   Valor inválido! Deve ser maior ou igual a {minimo}.\n")
            continue
        if maximo is not None and valor > maximo:
            print(f"⚠️   Valor inválido! Deve ser menor ou igual a {maximo}.\n")
            continue

        # Entrada válida, sai do loop
        validado = True

    return valor

# Função que verifica se há risco de enchente com base em 3 critérios
def verificar_enchente(estado_num, chuva, nivel_rio, dias_chuva):
    # Recupera o valor de chuva suportado conforme o estado escolhido
    limite_chuva = chuvaSuportado[estado_num - 1]

    # Define os critérios de risco com base nas entradas do usuário
    crit1 = chuva > limite_chuva
    crit2 = nivel_rio > 4
    crit3 = dias_chuva > 2

    # Soma quantos critérios foram atingidos
    total_criticos = sum([crit1, crit2, crit3])

    # Se 2 ou mais critérios forem verdadeiros, exibe alerta. Caso contrário, tudo está sob controle
    if total_criticos >= 2:
        return "⚠️  Alerta: Há risco de enchente na região!"
    else:
        return "✅ Situação sob controle. Nenhum risco de enchente detectado."

# Função principal do programa
def main():
    mostrar_menu()  # Mostra o menu de estados

    estado_valido = False
    # Solicita que o usuário escolha um estado válido
    while not estado_valido:
        estado_num = int(input("\nDigite o número do estado: "))
        if 1 <= estado_num <= 5:
            estado_valido = True
        else:
            print("⚠️   Opção inválida. Digite um valor de 1 a 5.\n")

    # Associa o número digitado ao estado e mostra o mapa correspondente
    if estado_num == 1:
        estado = "São Paulo"
        mostrar_mapa_sao_paulo()
    elif estado_num == 2:
        estado = "Rio de Janeiro"
        mostrar_mapa_rio_de_janeiro()
    elif estado_num == 3:
        estado = "Bahia"
        mostrar_mapa_bahia()
    elif estado_num == 4:
        estado = "Paraná"
        mostrar_mapa_parana()
    elif estado_num == 5:
        estado = "Pernambuco"
        mostrar_mapa_pernambuco()

    # Coleta os dados de entrada do usuário
    print("\n---------------------------------------")
    print(f"Estado selecionado: {estado}")
    chuva = validar_numero(f"Digite a quantidade de chuva registrada em {estado} (em mm): ", float, 0, 500)
    nivel_rio = validar_numero("Digite o nível do rio (em metros): ", float, 0, 20)
    dias_chuva = validar_numero("Digite a quantidade de dias de chuva contínua: ", int, 0, 30)
    print("---------------------------------------\n")

    # Chama a função que verifica se há risco e mostra o resultado final
    resultado = verificar_enchente(estado_num, chuva, nivel_rio, dias_chuva)

    print(resultado)
    print("\n=======================================")

# Inicia o programa chamando a função principal
main()
