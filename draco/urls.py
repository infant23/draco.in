from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from .views import redirect_blog

urlpatterns = [
	path('', redirect_blog),
	path('dracoin/', include('dracoin.urls')),
	path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
