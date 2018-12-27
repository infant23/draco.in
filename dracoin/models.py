from django.db import models
from django.shortcuts import reverse

from django.utils.text import slugify
from time import time

def gen_slug(s):
	new_slug = slugify(s, allow_unicode=True)
	return new_slug + '-' + str(int(time()))

class Article(models.Model):
	title = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, blank=True, unique=True)
	content = models.TextField(blank=True, max_length=2000, db_index=True)
	author = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published', auto_now_add=True)
	tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
	
	def get_absolute_url(self):
		return reverse('dracoin:post_detail_url', kwargs={'slug': self.slug})

	def get_update_url(self):
		return reverse('dracoin:post_update_url', kwargs={'slug': self.slug})
	
	def get_delete_url(self):
		return reverse('dracoin:post_delete_url', kwargs={'slug': self.slug})

	def get_comments(self):
		return Comment.objects.filter(root=self.pk)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = gen_slug(self.title)
		super().save(*args, **kwargs)
	
	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-pub_date']

class Tag(models.Model):
	title = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(max_length=200, unique=True)
	
	def get_absolute_url(self):
		return reverse('dracoin:tag_detail_url', kwargs={'slug': self.slug})

	def get_update_url(self):
		return reverse('dracoin:tag_update_url', kwargs={'slug': self.slug})
	
	def get_delete_url(self):
		return reverse('dracoin:tag_delete_url', kwargs={'slug': self.slug})

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['title']

class Image(models.Model):
	title = models.CharField(max_length=200)
	image = models.ImageField(upload_to='pictures')
	
	def __str__(self):
		return self.title

class Comment(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	content = models.TextField(max_length=500, db_index=True)
	root = models.ForeignKey(Article, on_delete=models.CASCADE)
	previous = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
	pub_date = models.DateTimeField('date published', auto_now_add=True)
	
	def __str__(self):
		return self.content