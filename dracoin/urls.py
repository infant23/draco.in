from django.urls import path

from . import views

app_name = 'dracoin'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('tags/', views.TagsView.as_view(), name='tags'),
	# path('contacts/', views.feedback, name='feedback'),
	path('mail/', views.FeedBack.send_email, name='mail'),
    # path('', views.index, name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:article_id>/', views.detail, name='detail'),
    # path('<int:tag_id>/tag/', views.results, name='results'),
    # path('<int:image_id>/img/', views.vote, name='vote'),
]


# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
#     path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#     path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]