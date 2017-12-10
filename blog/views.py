from django.shortcuts import render
from blog.models import Introductions, Gallery, Image


# Create your views here.
def hello(response):
	return HttpResponse("Hello world ! ")

def SetIndexBackroundImg(request):
	Address={}
	Address['Index_bg_img_address']='/static/img/index.png'
	Address['js_address']='/static/js/main.js'
	return render(request, 'index.html', Address)
def spec(request):
	show={}
	show['js_address']='/static/js/main.js'
	show['main_logo_address']='/static/img/logo/logo2.png'
	intro=Introductions.objects.filter(brief_intro='spec') 
	title=intro.values('title')[0]['title']
	content=intro.values('content')[0]['content']
	number_of_imgs=Image.objects.filter(gallery=1).count()#if it return int 2, actually the index is 0 and 1
	a=[]
	for i in range(number_of_imgs):
		a.append('/'+Image.objects.filter(gallery=1)[i].file.name)
	#file=a.values('file')[0]['file']
	show['title']=title
	show['content']=content
	show['file']=a
	#show['file']='/'+file
	return render(request, 'spec.html', show)
def contact(request):
	show={}
	show['main_logo_address']='/static/img/logo/logo2.png'
	return render(request, 'contact.html', show)