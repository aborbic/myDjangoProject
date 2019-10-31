from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('list_all', views.announcement_list, name='Announcement List'),
    path('show_detail/<id>/', views.announcement_detail, name='Announcement Details'),
    path('upload', picture_image_view, name='image_upload'),
    path('success', success, name='success'),
    path('picture_images', views.display_picture_images, name="picture_images"),
    path('interviews', views.email_list, name="interviews"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)