import tutorial_conexao as cn
import requests
from bs4 import BeautifulSoup

def savePromo(tuple, connection):
	sql_query = "INSERT INTO promotion (`identifier`, `name`, `url`, `gatry_url`, `price`) VALUES (%s, %s, %s, %s, %s)"
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
		
connection = cn.connectDB()
qtde=0
while qtde<100:
	url = 'https://gatry.com/home/mais_promocoes?onlyPromocao=true&qtde=' + str(qtde)
	req = requests.get(url)
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
			try:
				fullprice = currency.text + price.text
			except:
				fullprice = 'cupom'
			id_url_gatry = item.find(name='a', attrs={'class':'mais hidden-xs'})
			id_gatry = id_url_gatry['data-promocao']
			url_gatry = id_url_gatry['href']
			tupla = (id_gatry, name_url.text, name_url['href'], url_gatry, fullprice)
			savePromo(tupla, connection)
	qtde+=9
cn.closeDB(connection)
print("conexao fechada")
		







