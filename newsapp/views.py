from django.shortcuts import render
import requests

def home(request):
	if request.method=="POST":
		src = request.POST.get('src')
		try:
			a1 = "https://newsapi.org/v2/top-headlines"
			a2 = "?sources=" + src
			a3 = "&apikey="+"dcf42dec7d614e778d3dcd8616ab8182"
			wa = a1 + a2 + a3
			res = requests.get(wa)
			data = res.json()
			info =  data['articles']
			return render(request,"home.html",{'info':info,'src':src})
		except Exception as e:
			return render(request,"home.html",{'info':'Check later'})
	else:
		return render(request,"home.html")