from django.db import models
from django.contrib.auth.models import User

#创建app模型
# Create your models here.

#博客类型
class BlogType(models.Model):
	type_name=models.CharField(max_length=15)

	def __str__(self):
		return self.type_name

#博客
class Blog(models.Model):
	title=models.CharField(max_length=50)
	blog_type=models.ForeignKey(BlogType,on_delete=models.DO_NOTHING) #设置和模板关联 是外键 删除方式是不删除
	content=models.TextField()
	author=models.ForeignKey(User,on_delete=models.DO_NOTHING)
	created_time=models.DateTimeField(auto_now_add=True) #发表时间
	last_updated_time=models.DateTimeField(auto_now=True)

	def __str__(self):
		return "<Blog:%s>" % self.title

	class Meta:
		#排序, 按发表时间倒叙排列
		ordering=['-created_time']