from django.urls import path
from .views import *

app_name = 'dracoin'
urlpatterns = [
	path('', last_articles, name='index'),
	path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
	# path('post/<str:slug>/', post_detail, name='post_detail_url'),
	path('tags/', all_tags, name='tags_list_url'),
	path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
	# path('tag/<str:slug>/', tag_detail, name='tag_detail_url'),
	path('comments/<int:root_id>', article_comments, name='comments'),
]
