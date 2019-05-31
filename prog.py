import tutorial_conexao as cn
import requests
from bs4 import BeautifulSoup

def savePromo(tuple):
	sql_query = "INSERT INTO promotion (`identifier`, `name`, `url`, `gatry_url`, `price`) VALUES (%s, %s, %s, %s, %s)"
	connection = cn.connectDB()
	try: 
		cursor = connection.cursor(prepared=True)
		result = cursor.execute(sql_query, tuple)
		connection.commit()
		print("registro inserido")
	except:
		connection.rollback()
		print("erro ao inserir")
	finally:
		cursor.close()
		cn.closeDB(connection)
		print("conexao fechada")

req = requests.get('http://www.gatry.com')
conexao = cn.connectDB()
if req.status_code == 200:
	print('gatry opened')
	content = req.content
	soup = BeautifulSoup(content, 'html.parser')
	div = soup.find_all(name='div', attrs={'class':'informacoes'})
	print(len(div))

	for item in div:
		name_url = item.find(name='a')
		price = item.find(attrs={'itemprop':'price'})
		currency = item.find(attrs={'itemprop':'priceCurrency'})
		fullprice = currency.text + price.text
		id_url_gatry = item.find(name='a', attrs={'class':'mais hidden-xs'})
		id_gatry = id_url_gatry['data-promocao']
		url_gatry = id_url_gatry['href']
		tupla = (id_gatry, name_url.text, name_url['href'], url_gatry, fullprice)
		savePromo(tupla)





