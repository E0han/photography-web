from django.db import models
from django.conf import settings
from django.core.files import File

class Introductions(models.Model):
	brief_intro=models.CharField(u'简写', max_length=128)
	title = models.CharField(u'标题', max_length=256)
	author = models.CharField(u'作者', max_length=256)
	author_email=models.CharField(u'作者邮箱', max_length=256)
	location = models.CharField(u'举办地点',  max_length=258)
	content = models.TextField(u'内容')
	zh_content= models.TextField(u'内容')
	pub_date = models.DateTimeField('date published',auto_now_add=True,editable = True)#publish date
	def __str__(self):# 在Python3中用 __str__ 代替 __unicode__
		return self.brief_intro

class Gallery(models.Model):
	title = models.CharField('Title', max_length=20)
	class Meta:
		verbose_name_plural = 'Galleries'

	def __str__(self):
		return self.title 

class Image(models.Model):
	file = models.FileField('File', upload_to='static/img/')
	gallery = models.ForeignKey(Gallery)
	def __str__(self):
		return self.filename
	@property
	def filename(self):
		return self.file.name.rsplit('/', 1)[-1]


