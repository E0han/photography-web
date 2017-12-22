from django.shortcuts import render
from blog.models import Introductions, Gallery, Image
from django import forms
from django.http import HttpResponse
#coding=utf-8

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
	b=Gallery.objects.get(title='spec')#外键的反向朔源
	this_gallery=b.image_set.all()
	number_of_imgs=this_gallery.count()#brief_intro, content, id, pub_date, title. if it return int 2, actually the index is 0 and 1
	a=[]
	for i in range(number_of_imgs):
		a.append('/'+this_gallery[i].file.name)
	show['title']=title
	show['content']=content
	show['file']=a
	#show['file']='/'+file
	return render(request, 'spec.html', show)
def contact(request):
	show={}
	show['js_address']='/static/js/main.js'
	show['main_logo_address']='/static/img/logo/logo2.png'
	return render(request, 'contact.html',show)


		