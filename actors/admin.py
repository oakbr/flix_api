from django.contrib import admin
from actors.models import Actor


#Isso é utilizado para exibir a tabela (Entidade) quando acessarmos com usuário admin
@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birthday', 'nationality',)




