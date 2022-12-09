
import mysql.connector

host = "167.99.252.245"
user = "BSI_E4"
passwd = "bsi@e42022"
database = "BSI_E4"
conexao = mysql.connector.connect(
    host=host, user=user, passwd=passwd, database=database)
cursor = conexao.cursor()

# Menu


def menuMercado():
    print("Selecione uma das opções")
    print("1-Criar de tabela ")
    print("2-Cadastrar produto ")
    print("3-Remover item do estoque ")
    print("4-Atualização de produtos ")
    print("5-sair ")
    opcao = input(">>> ")
    if (opcao == "1"):
        novaTabela()
    elif (opcao == "2"):
        addProduct()
    elif (opcao == "3"):
        productDelete()
    elif (opcao == "4"):
        updateItem()
    else:
        exit()


# tabela
def novaTabela():
    tabela = input("Digite o nome da nova tabela: ")
    cursor.execute(
        "CREATE TABLE " + tabela + " (FUNCAO VARCHAR(100), NOME VARCHAR(100), PRECO FLOAT, PRODUTOS INT);")
    conexao.commit()
    conexao.close()
    menuMercado()


# Cadastrar produto
def addProduct():
    tabela = input("Informe o nome da tabela que sera inserido: ")
    idd = input("Id do produto: ")
    nome = input("Nome do produto: ")
    preco = input("Preço do produto: ")
    print("Inserido na tabela " + tabela + " Id do produto:  " + idd +
          " nome do produto: " + nome + " Preco do produto: " + preco + ";")
    conexao.commit()
    conexao.close()
    menuMercado()


# Remoção de itens.
def productDelete():
    tabela = input("Informe o produto a ser deletado: ")
    idd = input("Função: ")
    print("removido da tabela " + tabela + " Id do produto:  " + idd + ";")
    conexao.commit()
    conexao.close()
    menuMercado()


# Atualização de item.
def updateItem():
    tabela = input("Informe a tabela para a atualização: ")
    idd = input("Id do produto: ")
    nome = input("Nome do produto: ")
    preco = input("Valor do produto: ")
    print("Atualizado na tabela " + tabela + " Id do produto:  " + idd +
          " nome do produto: " + nome + " Preco do produto: " + preco + ";")
    conexao.commit()
    conexao.close()
    menuMercado()


menuMercado()
