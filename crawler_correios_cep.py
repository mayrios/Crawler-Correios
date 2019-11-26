import selenium.webdriver as webdriver
import pandas as pd
import csv

chrome = webdriver.Chrome()

#txt irá guardar a pesquisa nos correios
txt_file = open('enderecos_correios.txt', 'ab')
#arquivo = "Rua;Bairro;Localidade/UF;CEP \n"
#txt_file.write((arquivo.encode("utf8")))

#dataframe abre o arquivo de imóveis e cria a série de CEPs para pesquisa
df = pd.read_excel("Endereços aleatórios.xlsx")
ceps = df['CEP']

for cep in ceps:	
	
	chrome.get('http://www.buscacep.correios.com.br/sistemas/buscacep/')
	search_box = chrome.find_element_by_xpath('//*[@id="Geral"]/div/div/span[2]/label/input')
	search_box.send_keys(cep)
	search_box.submit()

	rua = chrome.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[1]').text
	bairro = chrome.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[2]').text
	localidade = chrome.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[3]').text
	codigo = chrome.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[4]').text
	dados = rua + ";" + bairro + ";" + localidade + ";" + codigo + "\n"
	txt_file.write((dados.encode("utf8")))    

txt_file.close()
chrome.close()
