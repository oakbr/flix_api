from rest_framework import permissions


class MoviePermissionClass(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTION']:
            return request.user.has_perm('movies.view_movie')

        if request.method in ['PUT', 'PATCH']:
            return request.user.has_perm('movies.change_movie')

        if request.method == 'POST':
            return request.user.has_perm('movies.add_movie')

        if request.method == 'DELETE':
            return request.user.has_perm('movies.delete_movie')

        return False
