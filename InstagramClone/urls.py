"""InstaClone URLs"""

from django.conf import settings
from django.conf.urls.static import static
# Django
from django.contrib import admin
from django.urls import path, include

# Views
urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include(('posts.urls', 'posts'), namespace='posts')),
    path('', include(('users.urls', 'users'), namespace='users')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
