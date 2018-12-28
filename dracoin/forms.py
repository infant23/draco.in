from django import forms
from .models import Article, Tag, Comment
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):

	class Meta:
		model = Article
		fields = ['title', 'slug', 'content', 'author', 'tags']

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'slug': forms.TextInput(attrs={'class': 'form-control'}),
			'content': forms.Textarea(attrs={'class': 'form-control'}),
			'author': forms.TextInput(attrs={'class': 'form-control'}),
			'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
		}

	def clean_slug(self):
		new_slug = self.cleaned_data['slug'].lower()
		if new_slug == 'create':
			raise ValidationError('Slug may be not "Create"')
		if self.model.objects.filter(slug__iexact=new_slug).count():
			raise ValidationError('There is "{}" slug already'.format(new_slug))
		return new_slug


class TagForm(forms.ModelForm):

	class Meta:
		model = Tag
		fields = ['title', 'slug']

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'slug': forms.TextInput(attrs={'class': 'form-control'}),
		}

	def clean_slug(self):
		new_slug = self.cleaned_data['slug'].lower()
		if new_slug == 'create':
			raise ValidationError('Slug may be not "Create"')
		if self.model.objects.filter(slug__iexact=new_slug).count():
			raise ValidationError('There is "{}" slug already'.format(new_slug))
		return new_slug


class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ['name', 'email', 'content', 'root']

		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.TextInput(attrs={'class': 'form-control'}),
			'content': forms.Textarea(attrs={'class': 'form-control'}),
		}
