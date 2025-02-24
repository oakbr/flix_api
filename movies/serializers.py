from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from actors.serializers import ActorSerializer
from genres.serializers import GenreSerializer


class MovieSerializer(serializers.ModelSerializer):


    class Meta:

        model = Movie
        fields = '__all__'

    # Inicio Criado Manualmente.
        # Está relacionado no Models do Reviews movie =  models.ForeignKey(Movie,on_delete=models.PROTECT,related_name='reviews')
        # reviews = obj.reviews.all()

        # sum_reviews = 0
        # if reviews:
        #     for review in reviews:
        #       sum_reviews += review.stars
        #       reviews_count = reviews.count()
        #      return round(sum_reviews / reviews_count,1)

    # Fim Criado Manualmente
    # Para fazer a validação é só escrever o começo da função com a palavra validate_<nome_do_campo>

    def validate_release_date(self, value):

        if value.year < 1900:
            raise serializers.ValidationError('Data de lançamento do filme não pode ser inferior a 1990.')
        else:
            return value

    def validate_resume(self, value):

        if len(value) > 500:
            raise serializers.ValidationError('Não é permitido resumo com mais de 200 caracteres.')
        else:
            return value

class MovieDetailSerializer(serializers.ModelSerializer):

    # Campo Caulculado Será Exibido no Retorno do JSON.
    genre = GenreSerializer()
    actors = ActorSerializer(many=True)
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)
        else:
            return None


class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()
