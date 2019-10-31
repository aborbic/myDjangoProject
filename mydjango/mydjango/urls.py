from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tausite/', include('django.contrib.auth.urls')),
    url('^tausite/', include(('tausite.urls', 'home'), namespace='tausite')),
    url('^tausite/', include(('tausite.urls', 'announcement_list'), namespace='Announcement List')),
    url('^tausite/', include(('tausite.urls', 'announcement_detail'), namespace='Announcement Details')),
    url('^tausite/', include(('tausite.urls', 'picture_image_view'), namespace='upload')),
    url('^tausite/', include(('tausite.urls', 'success'), namespace='success')),
    url('^tausite/', include(('tausite.urls', 'display_picture_images'), namespace='display_picture_images')),
    url('^tausite/', include(('tausite.urls', 'interviews'), namespace='interviews')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
