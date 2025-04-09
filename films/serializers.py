from rest_framework import serializers
from .models import Film


class FilmDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        #fields = ['id', 'name', 'kp_rating', 'created']
        fields = 'id name kp_rating text'.split()