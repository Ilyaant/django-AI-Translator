from django.urls import path
from .views import tr_text

urlpatterns = [
    path('trText/', tr_text, name='tr_text'),
]