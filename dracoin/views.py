from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.mail import BadHeaderError, send_mail
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import View
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q


from .models import Article, Tag, Image, Comment
from .utils import ObjectPaginationlMixin, ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from .forms import PostForm, TagForm, CommentForm, ImageForm


class PostIndex(ObjectPaginationlMixin, View):
    model = Article
    template = 'dracoin/index.html'
    page_value = 5

# class PostDetail(ObjectDetailMixin, View):
#     model = Article
#     template = 'dracoin/post_detail.html'

class PostDetail(View):
    model = Article
    template = 'dracoin/post_detail.html'
    page_value = 2
    model_form = CommentForm

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        comments = Comment.objects.filter(root=obj.pk)
        paginator = Paginator(comments, self.page_value)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
        else:
            prev_url = ''
        if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
        else:
            next_url = ''
        context = {
            self.model.__name__.lower() : obj,
            'admin_object': obj,
            'detail': True,
            'page_object': page,
            'is_paginated': is_paginated,
            'next_url': next_url,
            'prev_url': prev_url,
            'form': self.model_form
        }
        return render(request, self.template, context=context)
    def post(self, request, slug):
        print(request.POST)
        bound_form = self.model_form(request.POST)
        obj = self.model.objects.get(slug__iexact=slug)
        print(obj)
        # bound_form.root = obj.pk
        print(obj.pk)
        # bound_form['root'] = obj.pk
        if bound_form.is_valid():
            new_obj = bound_form.save()
            # return redirect(new_obj)
        # return render(request, self.template, context=context)
        return redirect(reverse('dracoin:index'))

class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = PostForm
    template = 'dracoin/post_create.html'
    raise_exception = True

class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Article
    model_form = PostForm
    template = 'dracoin/post_update.html'
    raise_exception = True

class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Article
    template = 'dracoin/post_delete.html'
    page = 'dracoin:index'
    raise_exception = True

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'dracoin/tag_detail.html'

class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = TagForm
    template = 'dracoin/tag_create.html'
    raise_exception = True

class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'dracoin/tag_update.html'
    raise_exception = True

class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'dracoin/tag_delete.html'
    page = 'dracoin:tags_list_url'
    raise_exception = True

def last_articles(request):
    template = 'dracoin/index.html'
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Article.objects.filter(
            Q(title__icontains=search_query) | Q(content__icontains=search_query)
        )
    else:
        posts = Article.objects.all()
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''
    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url':prev_url
    }
    return render(request, template, context=context)

def all_images(request):
    template = 'dracoin/image_list.html'
    image_list = Image.objects.all()
    return render(request, template, context={'image_list' : image_list})

class ImageDetail(ObjectDetailMixin, View):
    model = Image
    template = 'dracoin/image_detail.html'

class ImageCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = ImageForm
    template = 'dracoin/image_create.html'
    raise_exception = True

class ImageUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Image
    model_form = ImageForm
    template = 'dracoin/tag_update.html'
    raise_exception = True

class ImageDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Image
    template = 'dracoin/image_delete.html'
    page = 'dracoin:image_list_url'
    raise_exception = True


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

