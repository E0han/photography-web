from django.db import models

# Create your models here.
class Introductions(models.Model):
	brief_intro=models.CharField(u'简写', max_length=128)
	title = models.CharField(u'标题', max_length=256)
	content = models.TextField(u'内容')
	file=models.ImageField(upload_to='./static/img/')
	pub_date = models.DateTimeField('date published',auto_now_add=True,editable = True)#publish date
	def __str__(self):# 在Python3中用 __str__ 代替 __unicode__
		return self.brief_intro
	def mkdir(self,path):
		import os
		path=path.strip()
		path=path.rstrip("\\")
		isExists=os.path.exists(path)#判断路径是否存在
		if not isExists:
			os.makedirs(path)
			return True
		else:
			return False
