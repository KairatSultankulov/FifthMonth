from rest_framework import serializers
from .models import Film, Director, Genre


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id', 'fio'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class FilmDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'


class FilmSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    genres = GenreSerializer(many=True)
    director_fio = serializers.SerializerMethodField()

    class Meta:
        model = Film
        #fields = ['id', 'name', 'kp_rating', 'created']
        fields = 'id name kp_rating text director genres director_fio genre_names'.split()

    def get_director_fio(self, film):
        return film.director.fio if film.director_id else None