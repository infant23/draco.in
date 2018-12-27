from django.contrib import admin
from django.urls import include, path


from .views import redirect_blog

urlpatterns = [
	path('', redirect_blog),
	path('dracoin/', include('dracoin.urls')),
	path('admin/', admin.site.urls),
]
