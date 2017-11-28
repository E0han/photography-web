from django.http import HttpResponse
from django.shortcuts import render

def hello(response):
	return HttpResponse("Hello world ! ")

def SetIndexBackroundImg(request):
	Address={}
	Address['Index_bg_img_address']='/static/img/index.png'
	Address['js_address']='/static/js/main.js'
	return render(request, 'index.html', Address)
def test(request):
	Address={}
	Address['js_address']='/static/js/main.js'
	Address['main_logo_address']='/static/img/logo/logo2.png'
	return render(request, 'spec.html', Address)
