from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.mail import BadHeaderError, send_mail
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import View
from django.utils import timezone

from .models import Article, Tag, Image, Comment
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from .forms import PostForm, TagForm

class PostDetail(ObjectDetailMixin, View):
    model = Article
    template = 'dracoin/post_detail.html'

class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'dracoin/post_create.html'

class PostUpdate(ObjectUpdateMixin, View):
    model = Article
    model_form = PostForm
    template = 'dracoin/post_update.html'

class PostDelete(ObjectDeleteMixin, View):
    model = Article
    template = 'dracoin/post_delete.html'
    page = 'dracoin:index'

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'dracoin/tag_detail.html'

class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'dracoin/tag_create.html'

class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'dracoin/tag_update.html'

class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    template = 'dracoin/tag_delete.html'
    page = 'dracoin:tags_list_url'

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

