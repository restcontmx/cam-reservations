from django.db import models
from django.contrib.auth.models import User

"""
This is a task to assign tasks to users on the admin panel
"""
class Task( models.Model ) :
    
    name = models.CharField( max_length = 500, default = "", blank = False )
    description = models.CharField( max_length = 500, default = "", blank = True )
    date_end = models.DateTimeField( blank = False )
    value = models.IntegerField( default = 0, blank = True )
    
    user = models.ForeignKey( User, related_name="master" )
    user_assigned = models.ForeignKey( User, related_name="assigned_user" )
    
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )
    
    def __str__( self ) :
        """ this returns a string that represents the model """
        return self.name
        