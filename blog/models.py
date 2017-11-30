from django.db import models

# Create your models here.
class Introductions(models.Model):
	brief_intro=models.CharField(u'简写', max_length=128)
	title = models.CharField(u'标题', max_length=256)
	content = models.TextField(u'内容')
	#models.FileField(upload_to='./jpg')
	pub_date = models.DateTimeField('date published',auto_now_add=True,editable = True)#publish date
	def __str__(self):# 在Python3中用 __str__ 代替 __unicode__
		return self.brief_intro