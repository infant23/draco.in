from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.mail import BadHeaderError, send_mail
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Article, Tag, Image

class IndexView(generic.ListView):
    template_name = 'dracoin/index.html'
    context_object_name = 'latest_article_list'
    def get_queryset(self):
        return Article.objects.filter(
            pub_date__lte=timezone.now()
            ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Article
    template_name = 'dracoin/detail.html'
    # send_mail('subject', 'message', 'admin@example.com', ['admin@example.com'])

class TagsView(generic.ListView):
    template_name = 'dracoin/tags.html'
    context_object_name = 'tag_list'
    def get_queryset(self):
        return Tag.objects.all()

# class FeedBack(object):
#     """docstring for FeedBack"""
#     def __init__(self, arg):
#         super(FeedBack, self).__init__()
#         self.arg = arg

# def feedback(request):
#     model = Article
#     template_name = 'dracoin/mail.html'
def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    # return HttpResponseRedirect(reverse('dracoin:index'))
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
        return HttpResponseRedirect(reverse('dracoin:mail'))