from django.db import models
from django.contrib.auth.models import User

class AreaType( models.Model ) :

    user = models.ForeignKey( User, on_delete=models.CASCADE )
    name = models.CharField( max_length = 100, default = "", blank = False, unique = True )
    description = models.CharField( max_length = 200, default = "", blank = True, unique = False )
    max_guests = models.IntegerField( default = 0 )
    
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )
    
    def __str__( self ) : 
        return ( "{0}" ).format( self.name )


class CabinType( models.Model ) :
    
    user = models.ForeignKey( User, on_delete = models.CASCADE )
    name = models.CharField( max_length = 100, default = "", blank = False, unique = True )
    description = models.CharField( max_length = 500, default = "", blank = True )
    rooms = models.IntegerField( default = 0 )
    max_guests = models.IntegerField( default = 0 )
    max_extra_guests = models.IntegerField( default = 0 )
    
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )
    
    def __str__( self ) :
        return ( "{0}" ).format( self.name )
        

class Cabin( models.Model ) :
    
    user = models.ForeignKey( User, on_delete = models.CASCADE )
    name = models.CharField( max_length = 100, default = "", unique = True )
    cabin_type = models.ForeignKey( CabinType, on_delete = models.CASCADE )
    description = models.CharField( max_length = 500, default = "", blank = True )
    price = models.DecimalField( max_digits = 9, decimal_places = 2, default = 0.00, blank = False )
    img_url = models.CharField( max_length = 500, default = "http://i.imgur.com/0i6g2kx.png" )
    
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )
    updated = models.DateField( auto_now_add = False, auto_now = True )
    
    def __str__( self ) :
        return ( "{0}" ).format( self.name )
        

class Pool( models.Model ) :
    
    user = models.ForeignKey( User, on_delete = models.CASCADE )
    name = models.CharField( max_length = 100, default = "", unique = True )
    description = models.CharField( max_length = 500, default = "", blank = True )
    max_people = models.IntegerField( default = 0, blank = True )
    price = models.DecimalField( max_digits = 9, decimal_places = 2, default = 0.00 )
    img_url = models.CharField( max_length = 500, default = "http://i.imgur.com/0i6g2kx.png", blank = True )
    
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )
    
    def __str__( self ) :
        return ( "{0}" ).format( self.name )
        

class Area( models.Model ) :
    
    user = models.ForeignKey( User, on_delete = models.CASCADE )
    name = models.CharField( max_length = 100, default = "" )
    description = models.CharField( max_length = 500, default = "", blank = True )
    price = models.DecimalField( max_digits = 9, decimal_places = 2, default = 0.00 )
    pools = models.ManyToManyField( Pool, blank = True )
    area_type = models.ForeignKey( AreaType, on_delete = models.CASCADE )
    
    timestamp = models.DateField( auto_now_add = True, auto_now = False )
    updated = models.DateField( auto_now_add = False, auto_now = True )
    
    def __str__( self ) :
        return ( "{0}" ).format( self.name )