from django.urls import path
from .views import hello


urlpatterns = [
    path('hellos/', hello, name="prueba"),
]
