from django.urls import path
from .views import tr_text, translator

urlpatterns = [
    path('trText/', tr_text, name='tr_text'),
    path('form/', translator, name='translator'),
]