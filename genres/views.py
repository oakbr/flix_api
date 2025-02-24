from rest_framework import generics
from genres.models import Genre
from genres.serializers import GenreSerializer
from rest_framework.permissions import IsAuthenticated

from app.permissions import GlobalDefatulPermissions

#from genres.permissions import GenrePermissionClass


# class GenreCreateListView(generics.ListCreateAPIView):
#     permission_classes = (IsAuthenticated,GenrePermissionClass,)
#     queryset = Genre.objects.all()
#     serializer_class = GenreSerializer


# class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthenticated,GenrePermissionClass,)
#     queryset = Genre.objects.all()
#     serializer_class = GenreSerializer


class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefatulPermissions,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefatulPermissions,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
















# @csrf_exempt
# def genre_create_list_view(request):
   
#    if request.method == 'GET':
   
#         #SELECIONAR TODAS OS GENEROS DA TABELA.
#         genres = Genre.objects.all()

#         #Serializar o retorno da base de dados.
#         data = [{'id': genre.id, 'name': genre.name} for genre in genres]
#         return JsonResponse(data,safe=False)
#    elif request.method == 'POST':
#        data = json.loads(request.body.decode('utf-8'))
#        new_genre = Genre(name=data['name'])
#        new_genre.save()
#        return JsonResponse(
#            {'id': new_genre.id, 'name': new_genre.name},
#              status=201,
#         )


#FORMA MANUAL DE FAZER 
# @csrf_exempt  
# def genre_detail_view(request, pk):
    
#     genre = get_object_or_404(Genre, pk=pk)

#     if request.method =='GET':
#         data = {'id': genre.id, 'name': genre.name}
#         return JsonResponse(data)
    
#     elif request.method =='PUT':
#         data = json.loads(request.body.decode('utf-8'))
#         genre.name = data['name']
#         genre.save()
#         return JsonResponse(
#            {'id': genre.id, 'name': genre.name},)
#     elif request.method == 'DELETE':
#         genre.delete()
#         return JsonResponse({'message': 'Genero excluído com sucesso!!!'},status=204,)

        
        


     

    
    
