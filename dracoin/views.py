from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Article, Tag, Image

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# def index(request):
#     latest_article_list = Article.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.title for q in latest_article_list])
#     return HttpResponse(output)

# def index(request):
#     latest_article_list = Article.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('dracoin/index.html')
#     context = {
#         'latest_article_list': latest_article_list,
#     }
#     return HttpResponse(template.render(context, request))

class IndexView(generic.ListView):
    template_name = 'dracoin/index.html'
    context_object_name = 'latest_article_list'

    def get_queryset(self):
        return Article.objects.order_by('-pub_date')[:5]
    # def get_queryset(self):
    #     """
    #     Return the last five published questions (not including those set to be
    #     published in the future).
    #     """
    #     return Question.objects.filter(
    #         pub_date__lte=timezone.now()
    #     ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Article
    template_name = 'dracoin/detail.html'

