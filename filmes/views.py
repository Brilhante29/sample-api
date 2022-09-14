from .models import Filmes
from .serializer import FilmesSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

# Create your views here.

class FilmesListAPIView(ListCreateAPIView):
    queryset = Filmes.objects.all()
    serializer_class = FilmesSerializer

    
class FilmesRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Filmes.objects.all()
    serializer_class = FilmesSerializer
    