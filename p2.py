import requests

try:
	a1 = "https://newsapi.org/v2/top-headlines"
	a2 = "?sources=" + "the-hindu"
	a3 = "&apikey="+"dcf42dec7d614e778d3dcd8616ab8182"
	wa = a1 + a2 + a3
		
	res = requests.get(wa)
	print(res)
	
	data = res.json()
	print(data)
	
	info =  data['articles']
	
	for i in info:
		print("*" * 50)
		print(i['title'])
		print(i['url'])
except Exception as e:
	print("Issue -->",e)