from django.urls import path
from .views import *


app_name = 'dracoin'
urlpatterns = [
	path('', PostIndex.as_view(), name='index'),
	# path('', last_articles, name='index'),
	path('post/create/', PostCreate.as_view(), name='post_create_url'),
	path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
	path('post/<str:slug>/add_comment/', PostDetail.as_view(), name='add_comment_url'),
	path('post/<str:slug>/update/', PostUpdate.as_view(), name='post_update_url'),
	path('post/<str:slug>/delete/', PostDelete.as_view(), name='post_delete_url'),
	path('tags/', all_tags, name='tags_list_url'),
	path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
	path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
	path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
	path('tag/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url'),
	path('images/', all_images, name='image_list_url'),
	path('image/create/', ImageCreate.as_view(), name='image_create_url'),
	path('image/<str:slug>/', ImageDetail.as_view(), name='image_detail_url'),
	path('image/<str:slug>/update/', ImageUpdate.as_view(), name='image_update_url'),
	path('image/<str:slug>/delete/', ImageDelete.as_view(), name='image_delete_url'),
	path('comments/<int:root_id>', article_comments, name='comments'),
]
