from django.shortcuts import render
from blog.models import Introductions, Gallery, Image
from django import forms
from django.http import HttpResponse
#coding=utf-8

# Create your views here.
def hello(response):
	return HttpResponse("Hello world ! ")
def get_count():#record the number of user clicking the page and save to the file
	countfile  = open('count.dat','a+')
	counttext = countfile.read()
	try:
		count=int(counttext)+1
	except:
		count=1
	countfile.seek(0)
	countfile.truncate()
	countfile.write(str(count))
	countfile.flush()
	countfile.close()
	return count


def SetIndexBackroundImg(request):
	Address={}
	Address['ico']='/static/img/logo/logo.ico'
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
	zh_content=intro.values('zh_content')[0]['zh_content']
	author=intro.values('author')[0]['author']
	location=intro.values('location')[0]['location']
	author_mail=intro.values('author_email')[0]['author_email']
	#capture=Image.objects.get()
	b=Gallery.objects.get(title='spec')#外键的反向朔源
	this_gallery=b.image_set.all()
	number_of_imgs=this_gallery.count()#brief_intro, content, id, pub_date, title. if it return int 2, actually the index is 0 and 1
	a=[]#save the file name
	for i in range(number_of_imgs):
		a.append(['/'+this_gallery[i].file.name,this_gallery[i].capture])
	show['title']=title
	show['content']=content
	show['zh_content']=zh_content
	show['author']=author
	show['location']=location
	show['file']=a
	show['author_mail']=author_mail
	show['ico']='/static/img/logo/logo.ico'
	#show['file']='/'+file
	return render(request, 'spec.html', show)
def contact(request):
	show={}
	show['ico']='/static/img/logo/logo.ico'
	show['js_address']='/static/js/main.js'
	show['main_logo_address']='/static/img/logo/logo2.png'
	show['igico']='/static/img/logo/ig.png'
	show['emailico']='/static/img/logo/email.png'
	return render(request, 'contact.html',show)


		