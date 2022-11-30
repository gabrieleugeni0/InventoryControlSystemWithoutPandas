# Importando bibliotecas
import csv
from os import path


# Obter opcao para o menu primario
def opcao_primaria():
    print('-' * 60)
    print(f'{"CONTROLE DE ESTOQUES":^60}')
    print('-' * 60)
    print('''    [1] Abrir estoque
    [2] Novo estoque
    [0] Sair''')
    while True:
        try:
            opcao = int(input('OPCAO: '))
        except TypeError:
            print('ERRO! Digite uma opcao valida! ', end='')
        except ValueError:
            print('ERRO! Digite uma opcao valida! ', end='')
        else:
            if 0 <= opcao <= 2:
                return opcao
            else:
                print('ERRO! Digite uma opcao valida! ', end='')


# Obter opcao para o menu secundario
def opcao_secundaria():
    print('-' * 60)
    print(f'{"OPCOES":^60}')
    print('-' * 60)
    print('''    [1] Adicionar novo produto
    [2] Pesquisar produto
    [3] Mostrar todos os produtos cadastrados
    [4] Alterar produto
    [5] Deletar produto
    [6] Ordenar estoque
    [0] Sair''')
    while True:
        try:
            opcao = int(input('OPCAO: '))
        except TypeError:
            print('ERRO! Digite uma opcao valida! ', end='')
        except ValueError:
            print('ERRO! Digite uma opcao valida! ', end='')
        else:
            if 0 <= opcao <= 6:
                print('-' * 60)
                return opcao
            else:
                print('ERRO! Digite uma opcao valida! ', end='')


# Obter opcao para a alteracao
def opcao_alteracao():
    print('-' * 60)
    print(f'{"ALTERACAO":^60}')
    print('-' * 60)
    print('''    [1] Alterar ID
    [2] Alterar Nome
    [3] Alterar Descricao
    [4] Alterar Preco
    [5] Alterar Quantidade
    [0] Sair''')
    while True:
        try:
            opcao = int(input('OPCAO: '))
        except TypeError:
            print('ERRO! Digite uma opcao valida! ', end='')
        except ValueError:
            print('ERRO! Digite uma opcao valida! ', end='')
        else:
            if 0 <= opcao <= 5:
                print('-' * 60)
                return opcao
            else:
                print('ERRO! Digite uma opcao valida! ', end='')


# Obter opcao para a chave
def opcao_chave():
    print('-' * 60)
    print(f'{"TIPO DE CHAVE DE PESQUISA":^60}')
    print('-' * 60)
    print('''    [1] Pesquisar por ID
    [2] Pesquisar por Nome
    [0] Sair''')
    while True:
        try:
            opcao = int(input('OPCAO: '))
        except TypeError:
            print('ERRO! Digite uma opcao valida! ', end='')
        except ValueError:
            print('ERRO! Digite uma opcao valida! ', end='')
        else:
            if 0 <= opcao <= 2:
                print('-' * 60)
                return opcao
            else:
                print('ERRO! Digite uma opcao valida! ', end='')


# Obter opcao para a ordenacao
def opcao_ordenacao():
    print('-' * 60)
    print(f'{"Ordenar estoque a partir do:":^60}')
    print('-' * 60)
    print('''    [1] ID
    [2] Nome
    [0] Sair''')
    while True:
        try:
            opcao = int(input('OPCAO: '))
        except TypeError:
            print('ERRO! Digite uma opcao valida! ', end='')
        except ValueError:
            print('ERRO! Digite uma opcao valida! ', end='')
        else:
            if 0 <= opcao <= 2:
                print('-' * 60)
                return opcao
            else:
                print('ERRO! Digite uma opcao valida! ', end='')


# Menu primario
def controle_estoque():
    try:
        while True:
            opcao1 = opcao_primaria()
            if opcao1 == 0:  # opcao de encerrar o sistema
                print()
                print('*' * 60)
                print(f'{" SISTEMA ENCERRADO ":^60}')
                print('*' * 60)
                exit()
            elif opcao1 == 1:  # opcao de abrir estoque existente
                while True:
                    nome_existente = str(input('Nome do estoque a abrir: ')).strip()
                    nomecomextensao = f'{nome_existente}.csv'
                    if path.isfile(nomecomextensao):  # validar se o arquivo existe
                        menu_secundario(nome_existente)
                        break
                    else:
                        print(f'ERRO! {nomecomextensao} nao existe!')
                        while True:
                            try:
                                opcao = int(input(' [0] Voltar ao menu anterior\n'
                                                  ' [1] Fazer nova pesquisa por arquivo de estoque\n'
                                                  ' OPCAO: '))
                            except TypeError:
                                print('ERRO! Digite uma opcao valida!')
                            except ValueError:
                                print('ERRO! Digite uma opcao valida!')
                            else:
                                if opcao == 0:
                                    controle_estoque()
                                elif opcao == 1:
                                    break
                                else:
                                    print('ERRO! Digite uma opcao valida!')
            elif opcao1 == 2:  # opcao de criar novo estoque
                nome_novo = str(input('Nome do estoque: '))
                novo_estoque(nome_novo)  # cria um novo estoque
                menu_secundario(nome_novo)
    except KeyboardInterrupt:
        print()
        print('*' * 60)
        print(f'{" SISTEMA ENCERRADO ":^60}')
        print('*' * 60)
        exit()


# Menu secundario
def menu_secundario(nome):
    while True:
        opcao2 = opcao_secundaria()  # entra no menu secundario
        if opcao2 == 0:
            break
        elif opcao2 == 1:
            adicionar_produto(nome)
        elif opcao2 == 2:
            menu_pesquisa(nome)
        elif opcao2 == 3:
            exibir_estoque(nome)
        elif opcao2 == 4:
            chave = str(input('Chave de pesquisa: [ID/Nome] ')).strip()
            alterar_estoque(nome, chave)
        elif opcao2 == 5:
            chave = str(input('Chave de pesquisa: [ID/Nome] ')).strip()
            deleta_produto(nome, chave)
        elif opcao2 == 6:
            menu_ordenacao(nome)


# Menu de pesquisa
def menu_pesquisa(nome):
    while True:
        chave = opcao_chave()
        if chave == 0:
            break
        elif chave == 1:
            id_pesquisa = str(input('ID: '))
            pesquisar_id(nome, id_pesquisa)
        elif chave == 2:
            nome_pesquisa = str(input('Nome: '))
            pesquisar_nome(nome, nome_pesquisa)


# Menu de alteracao
def menu_alteracao(produto):
    while True:
        opcao = opcao_alteracao()
        if opcao == 0:
            break
        elif opcao == 1:
            novo_id = obter_id()
            produto[0] = novo_id
        elif opcao == 2:
            novo_nome = obter_nome()
            produto[1] = novo_nome
        elif opcao == 3:
            nova_descricao = obter_descricao()
            produto[2] = nova_descricao
        elif opcao == 4:
            novo_preco = obter_preco()
            produto[3] = novo_preco
            produto[5] = produto[4] * novo_preco
        elif opcao == 5:
            nova_quantidade = obter_quantidade()
            produto[4] = nova_quantidade
            produto[5] = produto[4] * nova_quantidade


# Menu de ordenacao
def menu_ordenacao(nome):
    while True:
        chave = opcao_ordenacao()
        if chave == 0:
            break
        elif chave == 1:
            ordenar_estoque(nome, chave)
            break
        elif chave == 2:
            ordenar_estoque(nome, chave)
            break


# Funcao para criar um novo estoque em um novo arquivo .csv
def novo_estoque(nome):
    nome_arquivo = f'{nome}.csv'
    while path.isfile(nome_arquivo):
        novo_nome = str(input('ERRO! Arquivo ja existente! Digite outro nome para o arquivo: '))
        nome_arquivo = f'{novo_nome}.csv'
    with open(nome_arquivo, 'w', newline='') as estoque:
        escritor = csv.writer(estoque)
        escritor.writerow(['ID', 'Nome', 'Descricao', 'Preco unitario', 'Quantidade', 'Valor em estoque'])
    print(f'Estoque {nome_arquivo} criado com sucesso!')


# Funcao para ADICIONAR um produto em um estoque
def adicionar_produto(nome_estoque):
    nome_arquivo = f'{nome_estoque}.csv'
    id = obter_id()
    nome = obter_nome()
    descricao = obter_descricao()
    preco = obter_preco()
    quantidade = obter_quantidade()
    valor = preco * quantidade
    with open(nome_arquivo, 'r+', newline='') as estoque:
        leitor = csv.reader(estoque)
        escritor = csv.writer(estoque)
        verificador_id = 0
        verificador_nome = 0
        for linha in leitor:
            if linha[0] == id:
                verificador_id += 1
            if linha[1] == nome:
                verificador_nome += 1
        if verificador_id == 0 and verificador_nome == 0:
            escritor.writerow([id, nome, descricao, preco, quantidade, valor])
        else:
            if verificador_id != 0:
                print(f'Erro! Ja existe um produto com ID: {id} no estoque!')
            if verificador_nome != 0:
                print(f'Erro! Ja existe um produto com Nome: {nome} no estoque!')


# Funcao para obter e validar o ID
def obter_id():
    while True:
        id = str(input('ID: ')).strip().lower()
        if len(id) > 0:
            return id
        else:
            print('Erro! O ID deve ter pelo menos 1 caracter!')


# Funcao para obter e validar o Nome
def obter_nome():
    while True:
        nome = str(input('Nome: ')).strip().lower()
        if len(nome) > 1:
            return nome
        else:
            print('Erro! O NOME deve ter pelo menos 2 caracteres!')


# Funcao para obter e validar a Descricao
def obter_descricao():
    while True:
        descricao = str(input('Descricao: ')).strip().lower()
        if len(descricao) > 1:
            return descricao
        else:
            print('Erro! A descricao deve ter pelo menos 2 caracteres!')


# Funcao para obter e validar o preco
def obter_preco():
    while True:
        try:
            preco = float(input('Custo unitario: R$'))
        except TypeError:
            print('Erro! O preco deve ser um valor real!')
        except ValueError:
            print('Erro! O preco deve ser um valor real!')
        else:
            if preco >= 0:
                return preco
            else:
                print('Erro! O preco deve ser um valor real maior ou igual a ZERO!')


# Funcao para obter e validar a quantidade
def obter_quantidade():
    while True:
        try:
            quantidade = float(input('Quantidade: '))
        except TypeError:
            print('Erro! A quantidade deve ser um valor real!')
        except ValueError:
            print('Erro! A quantidade deve ser um valor real!')
        else:
            if quantidade >= 0:
                return quantidade
            else:
                print('Erro! A quantidade deve ser um valor real maior ou igual a ZERO!')


# Funcao para PESQUISAR um produto em um estoque por seu ID
def pesquisar_id(nome_estoque, id):
    nome_arquivo = f'{nome_estoque}.csv'
    with open(nome_arquivo, 'r', newline='') as estoque:
        leitor = csv.reader(estoque)
        exibir = [['ID', 'Nome', 'Descricao', 'Preco unitario', 'Quantidade', 'Valor em estoque']]
        for linha in leitor:
            if linha[0] == id:
                exibir.append(linha)
        if exibir == '':
            print(f'{"|" * 10}{" ID nao encontrado "}{"|" * 10}')
        else:
            for linha in exibir:
                print()
                for posicao, coluna in enumerate(linha):
                    if posicao != 5:
                        print(f'{coluna:^20}|', end='')
                    else:
                        print(f'{coluna:^20}', end='')
            print('\n\n')


# Funcao para PESQUISAR um produto em um estoque por seu NOME
def pesquisar_nome(nome_estoque, nome):
    nome_arquivo = f'{nome_estoque}.csv'
    with open(nome_arquivo, 'r', newline='') as estoque:
        leitor = csv.reader(estoque)
        exibir = [['ID', 'Nome', 'Descricao', 'Preco unitario', 'Quantidade', 'Valor em estoque']]
        for linha in leitor:
            if linha[1] == nome:
                exibir.append(linha)
        if exibir == '':
            print(f'{"|" * 10}{" Nome nao encontrado "}{"|" * 10}')
        else:
            for linha in exibir:
                print()
                for posicao, coluna in enumerate(linha):
                    if posicao != 5:
                        print(f'{coluna:^20}|', end='')
                    else:
                        print(f'{coluna:^20}', end='')
            print('\n\n')


# Funcao para EXIBIR todos os produtos cadastrados
def exibir_estoque(nome_estoque):
    nome_arquivo = f'{nome_estoque}.csv'
    with open(nome_arquivo, 'r', newline='') as estoque:
        leitor = csv.reader(estoque)
        for linha in leitor:
            print()
            for posicao, coluna in enumerate(linha):
                if posicao != 5:
                    print(f'{coluna:^20}|', end='')
                else:
                    print(f'{coluna:^20}', end='')
        print('\n\n')


# Funcao para MODIFICAR um produto cadastrado
def alterar_estoque(nome_estoque, chave_pesquisa):
    nome_arquivo = f'{nome_estoque}.csv'
    with open(nome_arquivo, 'r', newline='') as estoque:
        leitor = csv.reader(estoque)
        verificador = 0
        temporario = list(leitor)
        for produto in temporario:
            if produto[0] == chave_pesquisa:
                verificador += 1
                menu_alteracao(produto)
            elif produto[1] == chave_pesquisa:
                verificador += 1
                menu_alteracao(produto)
    if verificador == 0:
        print(f'{"|" * 10}{" Chave de pesquisa nao encontrada "}{"|" * 10}')
    else:
        with open(nome_arquivo, 'w', newline='') as estoque2:
            escritor = csv.writer(estoque2)
            escritor.writerows(temporario)
            temporario.clear()
            del verificador
            print('Alteracoes realizadas com sucesso!')


# Funcao para DELETAR um produto cadastrado
def deleta_produto(nome_estoque, chave_pesquisa):
    nome_arquivo = f'{nome_estoque}.csv'
    with open(nome_arquivo, 'r', newline='') as estoque:
        leitor = csv.reader(estoque)
        verificador = 0
        temporario = list(leitor)
        for posicao, produto in enumerate(temporario):
            if produto[0] == chave_pesquisa:
                verificador += 1
                temporario.pop(posicao)
            elif produto[1] == chave_pesquisa:
                verificador += 1
                temporario.pop(posicao)
    if verificador == 0:
        print(f'{"|" * 10}{" Chave de pesquisa nao encontrada "}{"|" * 10}')
    else:
        while True:
            confirmacao = str(input(f'Tem certeza de que deseja deletar '
                                    f'o produto [{chave_pesquisa}]? [S/N] ')).strip().upper()[0]
            if confirmacao not in 'SN':
                print('Erro! Digite uma opcao valida! [S/N]')
            else:
                break
        if confirmacao == 'S':
            with open(nome_arquivo, 'w', newline='') as estoque2:
                escritor = csv.writer(estoque2)
                escritor.writerows(temporario)
                temporario.clear()
                del verificador
                print(f'O produto [{chave_pesquisa}] foi deletado com sucesso!')
        else:
            print('Retornando ao menu anterior...')


# Funcao para ORDENAR o estoque pelo id
def ordenar_estoque(nome_estoque, opcao):
    nome_arquivo = f'{nome_estoque}.csv'
    with open(nome_arquivo, 'r', newline='') as estoque:
        leitor = csv.reader(estoque)
        next(leitor)
        temporario = list(leitor)
        if opcao == 1:
            temporario.sort(key=lambda x: x[0])
        elif opcao == 2:
            temporario.sort(key=lambda x: x[1])
    with open(nome_arquivo, 'w', newline='') as estoque2:
        escritor = csv.writer(estoque2)
        escritor.writerow(['ID', 'Nome', 'Descricao', 'Preco unitario', 'Quantidade', 'Valor em estoque'])
        escritor.writerows(temporario)
        temporario.clear()
        if opcao == 1:
            print('Ordenacao por ID realizada com sucesso!')
        elif opcao == 2:
            print('Ordenacao por NOME realizada com sucesso!')
