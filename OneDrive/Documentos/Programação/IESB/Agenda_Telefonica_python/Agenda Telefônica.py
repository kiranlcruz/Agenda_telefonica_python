def salvar_contatos(lista): #Função para salvar contatos.
    arquivo = open("contatos.txt", "w")

    for contatos in lista:
        arquivo.write("{},{},{},{},{}\n".format(
            contatos["nome"], contatos["telefone"], contatos["email"], contatos["twitter"], contatos["instagram"]))
    arquivo.close()


def carregar_contatos(lista): #Função para carregar a lista de contatos.
    try:
        arquivo = open("contato.txt", "r")

        for linha in arquivo.readline():
            coluna = linha.strip().split(",")


            contatos = {
                "nome": coluna[0],
                "telefone": coluna[1],
                "email": coluna[2],
                "twitter": coluna[3],
                "instagram": coluna[4]
            }
            lista.append(contatos)

        arquivo.close()

        return lista
    except FileNotFoundError:
        pass


def existe_contatos(lista, nome): #Função para conferir a existência do contato.
    if len(lista) > 0:
        for contatos in lista:
            if contatos["nome"] == nome:
                return True
    return False


def adicionar(lista): #função para adicionar novos contatos.
    while True:
        nome = str(input("Informe o nome do contato: "))
        if not existe_contatos(lista, nome):
            break
        else:
            print("Nome já cadastrado! Favor, insira outro nome para cadastro.")

    contatos = {
        "nome": nome,
        "telefone": str(input("Digite o telefone: ")),
        "email": str(input("Digite seu e-mail: ")),
        "twitter": str(input("Informe o seu pefil do Twitter: ")),
        "instagram": str(input("Informe o seu perfil do Instagram: "))
    }
    lista.append(contatos)

    print("O contato {} foi cadastrado com sucesso!\n".format(contatos["nome"]))


def alterar(lista): #Função para alterar os contatos.
    print("\n= Alterar Contato =")
    if len(lista) > 0:
        nome = input("Informe o nome do contato a ser alterado: ")
        if existe_contatos(lista, nome):
            for contatos in lista:
                if contatos["nome"] == nome:
                    print("\n")
                    print("=========================")
                    print("Nome: {}".format(contatos["nome"]))
                    print("Telefone: {}".format(contatos["telefone"]))
                    print("Email: {}".format(contatos["email"]))
                    print("Twitter: {}".format(contatos["twitter"]))
                    print("Instagram: {}".format(contatos["instagram"]))
                    print("=========================")
                    print("\n")

                    contatos["nome"] = input("Digite o novo nome do contato: ")
                    contatos["telefone"] = input(
                        "Digite o novo telefone do contato: ")
                    contatos["email"] = input(
                        "Digite o novo e-mail do contato: ")
                    contatos["twitter"] = input(
                        "Digite o novo perfil do Twitter do contato: ")
                    contatos["instagram"] = input(
                        "Digite o novo perfil do instagram do contato: ")

                    print("Os dados do contato com o nome {}, foram alterados com sucesso!\n".format(
                        contatos["nome"]))
                    break

        else:
            print(
                "Não há contato cadastrado no sistema com o nome {}.\n".format(nome))
    else:
        print("Não há nenhum contato cadastrado no sistema.\n")


def remover(lista): #Função para remover contatos.
    print("\n= Remover Contato =")
    if len(lista) > 0:
        nome = input("Digite o nome do contato a ser excluído: ")
        if existe_contatos(lista, nome):
            for i, contatos in enumerate(lista):
                if contatos["nome"] == nome:
                    print("\n=========================")
                    print("Nome: {}".format(contatos["nome"]))
                    print("Telefone: {}".format(contatos["telefone"]))
                    print("E-mail: {}".format(contatos["email"]))
                    print("Twitter: {}".format(contatos["twitter"]))
                    print("Instagram: {}".format(contatos["instagram"]))
                    print("=========================\n")

                    del lista[i]

                    print("O contato foi apagado com sucesso!")
                    break

        else:
            print(
                "Não há contato cadastrado no sistema com esse nome {}.\n".format(nome))
    else:
        print("Não existe nenhum contato cadastrado no sistema.\n")


def pesquisar(lista): #função para buscar contato.
    print("\n= Buscar Contato =")
    if len(lista) > 0:
        nome = input("Informe o nome do contato desejado: ")
        if existe_contatos(lista, nome):
            for contatos in lista:
                if contatos["nome"] == nome:
                    print("\n")
                    print("=========================")
                    print("Nome: {}".format(contatos["nome"]))
                    print("Telefone: {}".format(contatos["telefone"]))
                    print("E-mail: {}".format(contatos["email"]))
                    print("Twitter: {}".format(contatos["twitter"]))
                    print("Instagram: {}".format(contatos["instagram"]))
                    print("=========================")
                    print("\n")
                    break
        else:
            print(
                "Não há contato cadastrado no sistema com esse nome {}.\n".format(nome))
    else:
        print("Não há nenhum contato cadastrado no sistema.\n")


def listar(lista): #Função para listar/gerar relatório dos contatos cadastrados.
    if len(lista) > 0:
        for i, contatos in enumerate(lista):
            print("\n")
            print("=========================")
            print("contato {}:".format(i + 1))
            print("\tNome: {}".format(contatos["nome"]))
            print("\tTelefone: {}".format(contatos["telefone"]))
            print("\tE-mail: {}".format(contatos["email"]))
            print("\tTwitter: {}".format(contatos["twitter"]))
            print("\tInstagram: {}".format(contatos["instagram"]))
            print("=========================")
            print("")

        print("Quantidade de contatos: {}\n".format(len(lista)))

    else:
        print("Não há nenhum contato cadastrado para listar.\n")


def principal(): #Função para incializar a lista de contatos. Menu Principal.

    lista = []
    carregar_contatos (lista)

    while True:
        print(" @  Bem-vindo a sua Agenda Telefônica  @ ")
        print(" 1 - Adicionar contato ")
        print(" 2 - Alterar contato ")
        print(" 3 - Remover contato  ")
        print(" 4 - Buscar por contato ")
        print(" 5 - Listar contatos ")
        print(" 6 - Sair ")

        while True:
            try:
                opc = int(input("Insira o número da ação desejada -> "))
                opc = int(opc)
                break
            except ValueError:
                print("Apenas números são válidos!\nFavor. digite um número!")

        if opc == 1:
            adicionar(lista)
            salvar_contatos(lista)
        elif opc == 2:
            alterar(lista)
            salvar_contatos(lista)
        elif opc == 3:
            remover(lista)
            salvar_contatos(lista)
        elif opc == 4:
            pesquisar(lista)
        elif opc == 5:
            listar(lista)
        elif opc == 6:
            print("\nSaindo da Agenda\nVolte sempre!\n")
            break
        else:
            print("\nOpção inválida. Por favor, tente novamente.\n")

principal()

print ("Teste")