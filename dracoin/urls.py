from django.urls import path

from . import views

app_name = 'dracoin'
urlpatterns = [
	path('', views.last_articles, name='index'),
	path('post/<str:slug>/', views.post_detail, name='post_detail_url'),
	path('tags/', views.all_tags, name='tags_list_url'),
	path('tag/<str:slug>/', views.tag_detail, name='tag_detail_url'),
	path('comments/<int:root_id>', views.article_comments, name='comments'),
	path('mail/', views.send_email, name='mail'),
]
