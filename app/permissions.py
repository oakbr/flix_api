from rest_framework import permissions


#Classe utilizada por todas as apps do sistema.
class GlobalDefatulPermissions(permissions.BasePermission):
    def has_permission(self, request, view):

        model_permission_codename = self.__get_model_permission_codename(
            method=request.method, 
            view=view,
        )

        if not model_permission_codename:
            return False
        
        return request.user.has_perm(model_permission_codename)
     
    
    #Busca os nomes para montar string para a classe Global.
    def __get_model_permission_codename(self,method, view):

        try:
            app_label = view.queryset.model._meta.app_label

            action = self.__get_action_sufix(method)

            model_name = view.queryset.model._meta.model_name

            return f'{app_label}.{action}_{model_name}'
        
        except AttributeError:
            return None    

        
    
    def __get_action_sufix(self, method):
        method_actions = {
            'GET':     'view',
            'POST':    'add',
            'PUT':     'change',
            'PATCH':   'change',
            'DELETE':  'delete',
            'OPTIONS': 'view',
            'HEAD':    'view',

        } 
        return method_actions.get(method, '' )