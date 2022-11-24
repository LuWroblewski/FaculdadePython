
import pymongo
import csv
from csv import writer
from pymongo import MongoClient
import pandas as pd

# Conexão
try:
    myclient = pymongo.MongoClient(
        "mongodb+srv://teste:teste123@cluster0.1ylmc4y.mongodb.net/test")
    mydb = myclient["prova2"]

    print("\nConectado com sucesso\n")

except:
    print("\nPor favor tente mais tarde. Banco de dados fora do ar\n")


# funções robos:
def inserirRobos():

    print("Inserir dados do robo.\n\n")

    id = input("id:  ")
    mercadoria = input("mercadoria: ")
    prateleira = input("prateleira: ")

    avulso = {"id": id, "mercadoria": mercadoria, "prateleira": prateleira}
    x = mycol.insert_one(avulso)
    print(x)
    csvfile = open("robos.csv", "r")
    csv.DictReader(csvfile)

    enviaCSV = [id, mercadoria, prateleira]

    with open('robos.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(enviaCSV)
        f_object.close()


def lerRobo():
    for x in mycol.find():
        print(x)

    csvfile = open("robos.csv", "r")
    header = ["id",  "mercadoria", "prateleira"]
    reader = csv.DictReader(csvfile)
    print("\n")
    print(csvfile.read())


def updateRobo():

    print("Modificar dados do robo.\n\n")

    id = input("id:  ")
    mercadoria = input("mercadoria: ")
    prateleira = input("prateleira: ")

    myquery = {"id": id}
    newvalue = {
        "$set": {"id": id, "mercadoria": mercadoria, "prateleira": prateleira}}
    mycol.update_many(myquery, newvalue)

    df = pd.read_csv("robos.csv")
    df.loc[id, "id"] = id
    df.loc[id, "mercadoria"] = mercadoria
    df.loc[id, "prateleira"] = prateleira
    df.to_csv("robos.csv", index=False)

    print(df)


def deletarRobo():
    id = input("id:  ")
    myquery = { "id": id }
    mycol.delete_one(myquery)
    print(id)

    df = pd.read_csv("robos.csv")
    df_s = df[:int(id)]
    df_s.set_index('id', inplace=True)
    df_s = df_s.drop(int(id))
    print(df_s)

# funções admnistração:
def inserirADM():

    print("Inserir dados do colaborador.\n\n")

    matricula = input("matricula:  ")
    nome = input("nome:  ")
    CPF = input("CPF: ")
    cargo = input("cargo: ")
    filial = input("filial: ")

    avulso = {"matricula": matricula, "nome": nome,
              "CPF": CPF, "cargo": cargo, "filial": filial}
    x = mycol.insert_one(avulso)
    print(x)
    csvfile = open("adm.csv", "r")
    csv.DictReader(csvfile)

    enviaCSV = [matricula, nome, CPF, cargo, filial]

    with open('adm.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(enviaCSV)
        f_object.close()


def lerADM():
    for x in mycol.find():
        print(x)

    csvfile = open("adm.csv", "r")
    header = ["matricula",  "nome", "CPF", "cargo", "filial"]
    reader = csv.DictReader(csvfile)
    print("\n")
    print(csvfile.read())


def updateADM():

    print("Modificar dados do colaborador.\n\n")

    matricula = input("matricula:  ")
    nome = input("nome:  ")
    CPF = input("CPF: ")
    cargo = input("cargo: ")
    filial = input("filial: ")

    myquery = {"matricula": matricula}
    newvalue = {"$set": {"matricula": matricula, "nome": nome,
                         "CPF": CPF, "cargo": cargo, "filial": filial}}
    mycol.update_many(myquery, newvalue)

    df = pd.read_csv("adm.csv")
    df.loc[matricula, "matricula"] = matricula
    df.loc[matricula, "nome"] = nome
    df.loc[matricula, "CPF"] = CPF
    df.loc[matricula, "cargo"] = cargo
    df.loc[matricula, "filial"] = filial
    df.to_csv("adm.csv")

    print(df)


def deletarADM():
    matricula = input("matricula:  ")
    myquery = {"matricula": matricula}
    mycol.delete_one(myquery)
    print(matricula)
    df = pd.read_csv("adm.csv", index_col=False)

    df_s = df[:int(matricula)]
    print("df: \n", df_s)

    print("df index: ", df_s.index)
    df_s.set_index('matricula', inplace=True)
    df_s = df_s.drop(int(matricula))

    print(df_s)

# Menu


print("Digite 1 para: Robos;")
print("Digite 2 para: Administração;")
menu = input("\n Digite o banco de dados desejado >>> ")


if (menu == "1"):
    mycol = mydb["robos"]
    print("\nDigite 1 para: inserir;")
    print("Digite 2 para: ler;")
    print("Digite 3 para: atualizar;")
    print("Digite 4 para: deletar.\n")

    menuRobo = input("\n Digite a ação dentro do banco >>> ")
    if (menuRobo == "1"):
        inserirRobos()
    elif (menuRobo == "2"):
        lerRobo()
    elif (menuRobo == "3"):
        updateRobo()
    elif (menuRobo == "4"):
        deletarRobo()

if (menu == "2"):
    mycol = mydb["adm"]
    print("\nDigite 1 para: inserir;")
    print("Digite 2 para: ler;")
    print("Digite 3 para: atualizar;")
    print("Digite 4 para: deletar.\n")

    menuADM = input("\n Digite a ação dentro do banco >>> ")
    if (menuADM == "1"):
        inserirADM()
    elif (menuADM == "2"):
        lerADM()
    elif (menuADM == "3"):
        updateADM()
    elif (menuADM == "4"):
        deletarADM()
