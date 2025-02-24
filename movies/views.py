from django.db.models import Count, Avg
from rest_framework import generics, views, response
from movies.models import Movie
from movies.serializers import MovieSerializer, MovieStatsSerializer, MovieDetailSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from app.permissions import GlobalDefatulPermissions
from reviews.models import Review

# from movies.permissions import MoviePermissionClass

# Usando função individual
# class MovieCreateListView(generics.ListCreateAPIView):
#     permission_classes = (IsAuthenticated, MoviePermissionClass,)
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer

# class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthenticated, MoviePermissionClass, )
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer


class MovieCreateListView(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticated, GlobalDefatulPermissions,)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieDetailSerializer

        return MovieSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthenticated, GlobalDefatulPermissions, )
    queryset = Movie.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieDetailSerializer

class MovieStatsView(views.APIView):

    # Configurações da View
    permission_classes = (IsAuthenticated, GlobalDefatulPermissions,)
    queryset = Movie.objects.all()

    def get(self, request):

        # Buscar Todos os Dados
        # Montar Resposta
        # Devolver Resposta para o usuário com todas as estastísticas

        total_movies = self.queryset.count()

        # Comando semelhante ao SQL usando Count('id') Group by 'id' = name_genge, quantidade_genre
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))

        total_reviews = Review.objects.count()
        # Media das Notas de Review
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']
        # Montado na mão sem utilizar serializer
        # return response.Response(data={
        #         'total_movies': total_movies,
        #         'movies_by_genre': movies_by_genre,
        #         'total_reviews': total_reviews,
        #         'average_stars': round(average_stars,1) if average_stars else 0,
        #         },status=status.HTTP_200_OK)

        movie_stats = {'total_movies': total_movies, 'movies_by_genre': movies_by_genre, 'total_reviews': total_reviews, 'average_stars': round(average_stars, 1) if average_stars else 0, }

        serializer = MovieStatsSerializer(data=movie_stats)

        serializer.is_valid(raise_exception=True)

        return response.Response(data=serializer.validated_data, status=status.HTTP_200_OK,)
