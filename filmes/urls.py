from .views import FilmesListAPIView, FilmesRetrieveUpdateDestroyAPIView
from django.urls import path

urlpatterns = [
    path('api', FilmesListAPIView.as_view()),
    path('api/<int:pk>', FilmesRetrieveUpdateDestroyAPIView.as_view()),
]