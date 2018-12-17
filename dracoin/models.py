from django.db import models

class Article(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField(max_length=2000)
	autor = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.title

class Tag(models.Model):
	title = models.CharField(max_length=200)
	def __str__(self):
		return self.title

class Image(models.Model):
	title = models.CharField(max_length=200)
	image = models.FileField(upload_to='uploads/')
	def __str__(self):
		return self.title
		