from django.db import models
from django.conf import settings
from django.core.files import File

# Create your models here.
class Introductions(models.Model):
	brief_intro=models.CharField(u'简写', max_length=128)
	title = models.CharField(u'标题', max_length=256)
	content = models.TextField(u'内容')
	pub_date = models.DateTimeField('date published',auto_now_add=True,editable = True)#publish date
	def __str__(self):# 在Python3中用 __str__ 代替 __unicode__
		return self.brief_intro

class Gallery(models.Model):
    class Meta:
    	verbose_name_plural = 'Galleries'
    title = models.CharField('Title', max_length=20)

    def __str__(self):
        return self.title 

class Image(models.Model):
    file = models.FileField('File', upload_to='static/img/')
    gallery = models.ForeignKey('Gallery', related_name='images', blank=True, null=True)
    def __str__(self):
        return self.filename

    @property
    def filename(self):
        return self.file.name.rsplit('/', 1)[-1]


