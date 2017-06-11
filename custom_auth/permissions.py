from rest_framework import permissions
from .models import CustomSystemUser, Rol

"""
Is system worthy
this is for super admin, admin, general roles
"""
class IsSystemWorthy( permissions.BasePermission ) :
    
    def has_permission( self, request, view ) :
        """
        This is a function of the base permissions
        will verify the users role under 4 
        """
        the_user = CustomSystemUser.objects.get( user = request.user.id )
        return the_user.name.value < 4 

"""
Is syper admin
this verifies that is just super admin user
"""
class IsSuperAdmin( permissions.BasePermission ) :
    
    def has_permission( self, request, view ) :
        """
        This is a function of the base permissions
        will verify the users role equals to 1 that is the super admin rol 
        """
        the_user = CustomSystemUser.objects.get( user = request.user.id )
        return the_user.name.value == 1

"""
Is admin
this verifies all the admin roles; super admin, admin
"""
class IsAdmin( permissions.BasePermission ) :
    
    def has_permission( self, request, view ) :
        """
        This is a function of the base permissions
        will verify the users role under 3 
        """
        the_user = CustomSystemUser.objects.get( user = request.user.id )
        return the_user.name.value < 3

"""
Is application
the permission for the applications
just for general info and login 
"""
class  IsApplication( permissions.BasePermission ) :
    
    def has_permission( self, request, view ) :
        """
        This is a function of the base permissions
        will verify the users role equals to 5 
        """
        the_user = CustomSystemUser.objects.get( user = request.user.id )
        return the_user.name.value == 5

"""
Is client
this verifies if the user is client
this will be for the auth module of the web site
"""
class IsClient( permissions.BasePermission ) :
    
    def has_permission( self, request, view ) :
        """
        This is a function of the base permissions
        will verify the user is equals to 4 
        """
        the_user = CustomSystemUser.objects.get( user = request.user.id )
        return the_user.name.value == 4