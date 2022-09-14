from pyexpat import model
from rest_framework import serializers
from .models import Filmes

class FilmesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Filmes
        fields = '__all__'