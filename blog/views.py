from django.shortcuts import render
from blog.models import Introductions

# Create your views here.
def hello(response):
	return HttpResponse("Hello world ! ")

def SetIndexBackroundImg(request):
	Address={}
	Address['Index_bg_img_address']='/static/img/index.png'
	Address['js_address']='/static/js/main.js'
	return render(request, 'index.html', Address)
def test(request):
	show={}
	show['js_address']='/static/js/main.js'
	show['main_logo_address']='/static/img/logo/logo2.png'
	a=Introductions.objects.filter(brief_intro='spec')
	title=a.values('title')[0]['title']
	content=a.values('content')[0]['content']
	file=a.values('file')[0]['file']
	show['title']=title
	show['content']=content
	show['file']='/'+file
	return render(request, 'spec.html', show)