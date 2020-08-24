import pandas as pd
import xlrd

data = pd.read_excel(r"C:\Users\aliss\PycharmProjects\formatador-topdata\funcionarios-malu.xlsx")
arquivo = open("importacao-topdata.txt", "w")

def name_limited(nome):
    new_name = ''
    cont = 0
    while(cont < 12):
        if(nome[cont] == ' '):
            cont = 12
        else:
            new_name += nome[cont]
        cont += 1
    return new_name

cont = 2
while (cont < 677):
    full_name = data.loc[cont][3]
    name = name_limited(data.loc[cont][3])
    pis = data.loc[cont][4]
    arquivo.write(str(full_name) + ";" + str(name) + ";" + str(pis) + "3;3;3;N;;" + "\n")
    cont = cont + 1


