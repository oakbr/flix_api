from rest_framework import permissions


class GenrePermissionClass(permissions.BasePermission):

    def has_permission(self, request, view):
        #return request.user.is_authenticated and request.user.is_active

        if request.method in ['GET', 'OPTION', 'HEAD']:
            return request.user.has_perm('genres.view_genre')
        
        if request.method == 'POST':
            return request.user.has_perm('genres.add_genre')


        if request.method in ['PUT', 'PATCH']:
            return request.user.has_perm('genres.change_genre')
        
        if request.method == 'DELETE':
                return request.user.has_perm('genres.delete_genre')


        return False
        
    
