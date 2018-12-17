from django.contrib import admin
from django.urls import include, path

urlpatterns = [
	path('dracoin/', include('dracoin.urls')),
	path('admin/', admin.site.urls),
]
