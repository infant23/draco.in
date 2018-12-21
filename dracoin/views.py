from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.mail import BadHeaderError, send_mail
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic, View
from django.utils import timezone

from .models import Article, Tag, Image, Comment

def last_articles(request):
    template = 'dracoin/index.html'
    article_list = Article.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    return render(request, template, context={'article_list' : article_list})

def post_detail(request, slug):
    template = 'dracoin/detail.html'
    article = Article.objects.get(slug__iexact=slug)
    return render(request, template, context={'article' : article})

def article_comments(request, root_id):
    template = 'dracoin/comments.html'
    print(request)
    comment_list = Comment.objects.filter(root=root_id)
    return render(request, template, context={'comment_list' : comment_list})

def all_tags(request):
    template = 'dracoin/tags.html'
    tag_list = Tag.objects.all()
    return render(request, template, context={'tag_list' : tag_list})

def tag_detail(request, slug):
    template = 'dracoin/tag_detail.html'
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, template, context={'tag' : tag})

def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    subject = request.POST['subject']
    message = request.POST['message']
    from_email = request.POST['from_email']

    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['root@localhost'], )
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect(reverse('dracoin:index'))

    else:
        return HttpResponseRedirect(reverse('dracoin:index'))

