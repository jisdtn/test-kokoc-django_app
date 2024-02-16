from django.urls import path

from .views import get_rate

urlpatterns = [
    path('rate/', get_rate, name='get_rate'),
]
