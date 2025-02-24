from rest_framework import generics
from actors.models import Actor
from actors.serializers import ActorSerializer
from rest_framework.permissions import IsAuthenticated

from app.permissions import GlobalDefatulPermissions




class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefatulPermissions,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefatulPermissions,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer



#SEM UASAR CLASSE GLOBAL:

#from actors.permissions import ActorsPermissionClass




# class ActorCreateListView(generics.ListCreateAPIView):
#     permission_classes = (IsAuthenticated, ActorsPermissionClass,)
#     queryset = Actor.objects.all()
#     serializer_class = ActorSerializer


# class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthenticated, ActorsPermissionClass,)
#     queryset = Actor.objects.all()
#     serializer_class = ActorSerializer

