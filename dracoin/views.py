from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.mail import BadHeaderError, send_mail
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic, View
from django.utils import timezone

from .models import Article, Tag, Image, Comment

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

class TagsView(generic.ListView):
    template_name = 'dracoin/tags.html'
    context_object_name = 'tag_list'
    def get_queryset(self):
        return Tag.objects.all()

# class FeedBack(View):
#     template_name = 'dracoin/mail.html'
#     def get(self, request):
#         subject = request.POST.get('subject', '')
#         message = request.POST.get('message', '')
#         from_email = request.POST.get('from_email', '')
#         subject = request.POST['subject']
#         message = request.POST['message']
#         from_email = request.POST['from_email']

#         if subject and message and from_email:
#             try:
#                 send_mail(subject, message, from_email, ['root@localhost'], )
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return HttpResponseRedirect(reverse('dracoin:index'))

#         else:
#             return HttpResponseRedirect(reverse('dracoin:index'))

class FeedBack():
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
            return HttpResponseRedirect(reverse('dracoin:mail'))

class CommentsView(generic.ListView):
    template_name = 'dracoin/comments.html'
    context_object_name = 'comment_list'
    def get_context_data(self, request):
        return Comment.objects.get(root=request.POST.get('root', ''))
