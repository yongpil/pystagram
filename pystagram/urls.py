from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^photo/(?P<photo_id>\d+)$','photo.views.single_photo', name='view_single_photo'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^photo/upload/$', 'photo.views.new_photo', name='new_photo'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
