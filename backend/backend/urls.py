
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import get_user_model


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/',include('users.urls')),
    path('api/tasks/',include('tasks.urls')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
