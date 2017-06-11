# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class AlertNumbers( models.Model ) :
    
    name = models.CharField( max_length = 100, blank = False, default = "" )
    phone_regex = RegexValidator( regex=r'^\+?1?\d{9,15}$', message="Número de teléfono incorrecto." )
    phone_number = models.CharField( max_length = 200, validators=[phone_regex], blank=True, default='' )
    
    def set_default_models( self ) :
        """
        This will init all the first rows of the table as we need them in that order
        Do not erease this models
        """
        an1 = AlertNumbers( name = "Primer Número", phone_number = "4931143334" )
        an2 = AlertNumbers( name = "Segundo Número", phone_number = "4931143334" )
        an3 = AlertNumbers( name = "Tercer Número", phone_number = "4931143334" )
        
        an1.save()
        an2.save()
        an3.save()
        
    def __str__( self ) :
        return ("{0} {1}").format( self.pk, self.phone_number )

class AlertEmails( models.Model ) :
    
    name = models.CharField( max_length = 100, blank = False, default = "" )
    email = models.EmailField( max_length = 500, blank=True, unique = False, default='', null=True )
    
    def set_default_models( self ) :
        """
        This will init all the first rows of the table as we need them in that order
        Do not erease this models
        """
        ae1 = AlertEmails( name = "Primer Email", email = "gunt.raro@gmail.com" )
        ae2 = AlertEmails( name = "Segundo Email", email = "restcontmx@gmail.com" )
        ae3 = AlertEmails( name = "Tercer Email", email = "codethefunkout@gmail.com" )
        
        ae1.save()
        ae2.save()
        ae3.save()
        
    def __str__( self ) :
        return ( "{0} {1}" ).format( self.pk, self.email )

class ContactEmail( models.Model ) :
    
    name = models.CharField( max_length = 100, blank = False, default = "" )
    email = models.EmailField( max_length = 500, blank=True, unique = False, default='', null=True )
    
    def set_default_models( self ) :
        """
        This will init all the first rows of the table as we need them in that order
        Do not erease this models
        """
        ce = ContactEmail( name = "Primer Email", email = "restcontmx@gmail.com" )
        ce.save()
    
    def __str__( self ) :
        return ("{0} {1}").format( self.name, self.email )

class TicketPrices( models.Model ) :
    
    name = models.CharField( max_length = 100, blank = False, default = "" )
    price = models.DecimalField( max_digits = 9, decimal_places = 2, default = 0.00, blank = False )
    
    def set_default_models( self ) :
        """
        This will init all the first rows of the table as we need them in that order
        Do not erease this models
        """
        tp1 = TicketPrices( name = "Niño", price = 30.00 )
        tp2 = TicketPrices( name = "Adulto", price = 30.00 )
        
        tp1.save()
        tp2.save()
        
    def __str__( self ) :
        return ("{0} {1}").format( self.pk, self.price )

class Signatures( models.Model ) :

    name = models.CharField( max_length = 100, blank = False, default = "" )
    img_url = models.CharField( max_length = 500, default = "http://i.imgur.com/0i6g2kx.png" )
    
    def set_default_models( self ) :
        """
        This will init all the first rows of the table as we need them in that order
        Do not erease this models
        """
        sign = Signatures( name = "Ramiro Gutierrez Alaniz" )
        sign.save()
    
    def __str__( self ) :
        return ("{0} {1}").format( self.name, self.img_url )