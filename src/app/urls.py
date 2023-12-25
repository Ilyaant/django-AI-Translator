from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('dev/api/', include('aitranslate.urls')),
]
