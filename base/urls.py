from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.urls import include, path


urlpatterns = (
    path("", admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
) + tuple(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)) if settings.DEBUG else tuple()
