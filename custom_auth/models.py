from django.db import models
from django.contrib.auth.models import User

# Create your models here.

"""
Rol Model
This is for every kind of user authentication on the system
There are deined as the next:
    value - 1; name - Super Admin
    value - 2; name - Admin
    value - 3; name - General
    value - 4; name - Client
    value - 5; name - Application
"""
class Rol( models.Model ) : 
    
    name = models.CharField( max_length = 100, default="", blank=False, unique=True )
    description = models.CharField( max_length = 200, default="", blank=True )
    value = models.IntegerField( default=1, blank=False )
    
    def __str__( self ):
        """ Returns the string representation of the object """
        return ( 'name : {0} value : {1}' ).format( self.name, self.value )

"""
Custom system user
This works for relationships between the user model from the django framework 
and the rol
"""
class CustomSystemUser( models.Model ) :
    
    user = models.OneToOneField( User, on_delete=models.CASCADE )
    name = models.ForeignKey( Rol, on_delete=models.CASCADE )
    
    def __str__( self ) :
        """ Returns the string representation of the object """
        return ( '{0}' ).format( self.user )