# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from products.models import Cabin, Pool, Area
import datetime

class Detail( models.Model ) :
    
    user = models.ForeignKey( User )
    qty = models.IntegerField( default = 0, blank = True )
    
class DetailCabin( Detail ) :
    
    product = models.ForeignKey( Cabin )
    
    def __str__( self ) :
        return ( "Cabin : {0}; Qty : {1}" ).format( self.cabin.name, self.qty )

class DetailArea( Detail ) :
    
    product = models.ForeignKey( Area )
    
    def __str__( self ) :
        return ( "Area : {0}; Qty : {1}" ).format( self.area.name, self.qty )
    
class DetailPool( Detail ) :
    
    product = models.ForeignKey( Pool )
    
    def __str__( self ) :
        return ( "Pool : {0}; Qty : {1}" ).format( self.pool.name, self.qty )
        
class ReservationType( models.Model ) :
    
    user = models.ForeignKey( User )
    name = models.CharField( max_length = 100, default = "", blank = False )
    description = models.CharField( max_length = 200, default = "", blank = True )
    value = models.IntegerField( default = 0, blank = True )
    
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )
    
    def __str__( self ) :
        return self.name
    
class ReservationInfo( models.Model ) :
    
    user = models.ForeignKey( User )
    
    full_name = models.CharField( max_length = 500, blank = True )
    address1 = models.CharField( max_length = 500, blank = True )
    address2 = models.CharField( max_length = 500, blank = True )
    zip_code = models.IntegerField( default = 0, blank = True )
    city = models.CharField( max_length = 100, blank = True )
    state = models.CharField( max_length = 100, blank = True )
    country = models.CharField( max_length = 100, blank = True )
    
    email = models.EmailField( max_length = 500, blank=True, unique = True, default='' )
    
    phone_regex = RegexValidator( regex=r'^\+?1?\d{9,15}$', message="Número de teléfono incorrecto." )
    phone_number = models.CharField( max_length = 200, validators=[phone_regex], blank=True, default='' )
    
    def __str__( self ) :
        return ( "{0}" ).format( self.full_name )
        
class Reservation( models.Model ) :
    
    user = models.ForeignKey( User, related_name="user_creator" )
    user_client = models.ForeignKey( User, related_name="client_user", blank = True )
    reservation_info = models.ForeignKey( ReservationInfo, blank = True )
    reservation_type = models.ForeignKey( ReservationType )
    details = models.ManyToManyField( Detail )
    
    date_start = models.DateTimeField( blank = True )
    date_end = models.DateTimeField( blank = True )
    
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )
    
    def __str__( self ) :
        return ( "This is reservation {0}" ).format( self.id )
   
class PaymentStatus( models.Model ) :
    
    user = models.ForeignKey( User )
    name = models.CharField( max_length = 100, default = "", blank = False )
    description = models.CharField( max_length = 500, default = "", blank = True )
    value = models.IntegerField( default = 0 )
    
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )
    
    def __str__( self ) :
        return self.name

class Promotion( models.Model ) :
    
    user = models.ForeignKey( User )
    name = models.CharField( max_length = 100, blank = False, default = "" )
    description = models.CharField( max_length = 500, blank = True, default = "" )
    
    discount = models.DecimalField( max_digits = 9, decimal_places = 2, default = 0.00, blank = True )
    
    date_start = models.DateField()
    date_end = models.DateField()
    
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )
    
    def __str__( self ) :
        return self.name

class Payment( models.Model ) :
    
    user = models.ForeignKey( User )
    reservation = models.ForeignKey( Reservation )
    promotion = models.ForeignKey( Promotion )
    payment_status = models.ForeignKey( PaymentStatus )
    total = models.DecimalField( max_digits = 9, decimal_places = 2, default = 0.00, blank = False )
    
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )
    
    def __str__( self ) :
        return str( self.reservation )