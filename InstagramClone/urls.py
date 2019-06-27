"""InstaClone URLs"""

# Django
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from posts import views as posts_view

urlpatterns = [

    path('posts/', posts_view.list_posts),
    path('admin/', admin.site.urls)



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
