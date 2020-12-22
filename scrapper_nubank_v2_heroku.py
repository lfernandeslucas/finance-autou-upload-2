from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
#import pickle
from datetime import date, timedelta###### Essencial
import datetime
####
####
from shareplum import Site ###### Essencial
from shareplum import Office365 ###### Essencial

import os

#import sys
### Ignorar.
# f = open('parrot4.pkl','rb')
# myrowsbackup = pickle.load(f)
# z = open('parrot5.pkl','rb')
# mycells_backup = pickle.load(z)
#print(sys.version)

####Alterar:
################################### PARAMETRIZAÇÃO de data (DEFINIR O ANO DOS REGISTROS) e dicionário de meses!!!!!!!!!!!!!!!!!!!!!!!! <<<<<<<<<<<<<<<<<------ CONFERIR \/\/\/!!
year = 2020
dict_convert_month = {'JAN': 1, 'FEV':2, 'MAR': 3, 'ABR':4, 'MAI': 5, 'JUN':6, 'JUL': 7, 'AGO':8, 'SET': 9, 'OUT':10, 'NOV': 11, 'DEZ':12}
###############################################################################################################################################################################
################################### PARAMETRIZAÇÃO de Login do usuário !!!!!!!!!!!!!!!!!!!!!!!! <<<<<<<<<<<<<<<<<------ CONFERIR \/\/\/!!
cpf = '15744584773'
senha = 'Gmjc873umac1$'
###############################################################################################################################################################################
#### Fim do alterar.


print("TESTANDO git")

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)


driver.get("https://www.google.com")
#print(driver.page_source)

print("Fui no google e voltei brabão")

###################################################################### Início do Crawler no site do nubank!! Atenção ao QR Code.
####### Preparando o webdriver
#options = webdriver.ChromeOptions() 
#options.add_argument("user-data-dir=C:\\Users\\I\\AppData\\Local\\Google\\Chrome\\User Data") #Path to your chrome profile
#driver = webdriver.Chrome() #executable_path="C:\\WebDrivers\\chromedriver.exe")

####### Indo ao site do Nubank
#driver.get('https://app.nubank.com.br/#/login')




############### DESCOMENTAR TUDO (UMA VEZ SÓ NO CTRL / DAQUI PRA BAIXO!)

# #################### Vasculhando o Xpath e Fazendo Login
# xpath_cpf= '/html/body/navigation-base/div[1]/div/main/div[1]/div/div[1]/form/md-input-container[1]/input'
# xpath_senha = '/html/body/navigation-base/div[1]/div/main/div[1]/div/div[1]/form/md-input-container[2]/input'
# xpath_botao = '/html/body/navigation-base/div[1]/div/main/div[1]/div/div[1]/form/button'
# login_cpf = driver.find_element_by_xpath(xpath_cpf)
# login_cpf.send_keys(cpf)
# login_senha = driver.find_element_by_xpath(xpath_senha)
# login_senha.send_keys(senha)
# login_senha.send_keys(Keys.ENTER)

# #################### Sleep do QR Code. Ficar atento.
# time.sleep(15)

# #################### Coletando as informações da tabela.
# mytable = driver.find_element_by_css_selector('#feedTable')
# print(mytable)
# list_rows = []
# list_cells = []
# for row in mytable.find_elements_by_css_selector('tr'):
#     list_rows.append(row.text)
#     print(row.text)
#     for cell in row.find_elements_by_tag_name('td'):
#         print(cell.text)
#         list_cells.append(cell.text)
#         print("----")

# ####### Salvando os resultados em Pickle temporário
# # with open('parrot4.pkl','wb') as z:
# #         pickle.dump(list_rows,z)
# # with open('parrot5.pkl','wb') as x:
# #         pickle.dump(list_cells,x)

# ###################################################################### Fim do Crawler ao site do Nubank.









# ###################################################################### Indo no SHAREPOINT PEGAR A ULTIMA DATA REGISTRADA e preparar a base de IDS JÁ EXISTENTES:
# #####Conexão
# print("------------ Entrando no sharepoint para pegar ultima data registrada...")
# authcookie = Office365('https://autouonline0.sharepoint.com', username='lucas@autou.online', password='Gmjc873umac2$').GetCookies()
# site = Site('https://autouonline0.sharepoint.com/Sites/plataforma_de_gastos_ok', authcookie=authcookie)
# sp_list = site.List('registros_nubank')
# data = sp_list.GetListItems('All Items')
# last_data_base = (data[0]['data_nubank']).date()

# list_ids_no_sharepoint = []

# for i,item in enumerate(data):
#     sharepoint_ids = data[i]['id_gerado_nubank']
#     print(sharepoint_ids)
#     list_ids_no_sharepoint.append(sharepoint_ids)
# print("última data no sharepoint: ")
# print(last_data_base)

# ###################################################################### Fim da consulta inicial ao Sharepoint. 












# ###################################################################### Início do Loop que irá preparar a lista de registros a serem subidos:
# list_registros_nubank = []
# for item in list_cells:
#     seq = item.splitlines(0)
#     print(seq)
#     try:
#         if len(seq) == 4:
#             categ, desc, valor, data = seq
#         else:
#             categ, desc, valor, valor_usd, data = seq

#         valor = valor.replace("R$ ","")
#         print(categ)
#         print(desc)

#         if (categ == 'Fatura fechada' or categ == 'Pagamento recebido'):
#             print("fatura fechada ou pagamento recebido. ignorar!")

#         else:
#             print(valor)
#             print(data)
#             id_gerado_nubank = (categ + desc + valor + data).replace(' ','')
#             ################################## Convertendo a data do nubank em formato data:
#             data_month_written = data[-3:]
#             print(data_month_written)
#             data_day = data[:2].strip()
#             data_month = dict_convert_month[data_month_written]
#             print("Data Registro: " + data_day + "/" + str(data_month) + "/" + str(year))
#             string_data_full = data_day + "/" + str(data_month) + "/" + str(year)
#             data_registro_full_date = datetime.datetime.strptime(string_data_full, '%d/%m/%Y').date()

#             #####################################CHECK DO ID DO NUBANK)
#             print("----- check do id nubank ------")
#             print(id_gerado_nubank)
#             print(id_gerado_nubank in list_ids_no_sharepoint)

#             ################################## Apendando registro na lista que irá subir no sharepoint
#             if id_gerado_nubank in list_ids_no_sharepoint:
#                 print("registro já existente na base. ignorando...")
#             else:
#                 print("novo registro. adicionando à lista de registros!")
#                 #list_registros_nubank.append({'categ_nubank': categ, 'desc_nubank':desc, 'valor_nubank':valor, 'data_nubank':data, 'data_coleta': datetime.datetime.now(), 'id_gerado_nubank':id_gerado_nubank})
#                 list_registros_nubank.append({'categ_nubank': categ, 'desc_nubank':desc, 'valor_nubank':valor, 'data_nubank':data_registro_full_date, 'data_coleta': datetime.datetime.now(), 'id_gerado_nubank':id_gerado_nubank})

    
#     except:
#         "nope"
    
#     print("_________________________________________")
#     print("                                         ")

# print("!!! Dicionário de Registros Nubank está pronto !!! Quantidade de novos registros: " + str(len(list_registros_nubank)))
# print(list_registros_nubank)
# ###################################################################### Fim do Loop.










# ###################################################################### Subindo no SHAREPOINT:
# #####Conexão
# print("------------ Subindo no sharepoint...")
# authcookie = Office365('https://autouonline0.sharepoint.com', username='lucas@autou.online', password='Gmjc873umac2$').GetCookies()
# site = Site('https://autouonline0.sharepoint.com/Sites/plataforma_de_gastos_ok', authcookie=authcookie)
# sp_list = site.List('registros_nubank')
# data = sp_list.GetListItems('All Items')

# ######Editando a Lista:
# try:
#     new_list = site.List('registros_nubank')
#     new_list.UpdateListItems(data=list_registros_nubank, kind='New')
#     print("Upload no Sharepoint Concluido!")
#     print(str(len(list_registros_nubank)) + "Novos registros foram adicionados ao SharePoint." )
# except:
#     print("Nenhum novo registro.")
#     print(len(list_registros_nubank))

# ############################################################## Fim da subida no Sharepoint.

