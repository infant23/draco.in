from django.urls import path

from . import views

app_name = 'dracoin'
urlpatterns = [
	path('', views.last_articles, name='index'),
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('tags/', views.all_tags, name='tags'),
	path('<int:pk>/comments/', views.article_comments, name='comments'),
	path('mail/', views.send_email, name='mail'),
	# path('mail/', views.FeedBack.send_email, name='mail'),
    # path('', views.index, name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:article_id>/', views.detail, name='detail'),
    # path('<int:tag_id>/tag/', views.results, name='results'),
    # path('<int:image_id>/img/', views.vote, name='vote'),
]
