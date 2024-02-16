from django.urls import path

from .views import get_rate

app_name = 'rates'

urlpatterns = [
    path('rate/', get_rate, name='get_rate'),
]
