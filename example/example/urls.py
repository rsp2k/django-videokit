from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from media.views import list
from media.views import item_create

urlpatterns = [
    url(r'^$', list, name = 'list'),
    url(r'^item_create/', item_create, name = 'item_create'),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
