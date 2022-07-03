from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^', include('apps.mcemails.urls')),
    url('admin/', admin.site.urls),
]