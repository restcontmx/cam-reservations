# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class OurCompanyContent( models.Model ) :
    
    title = models.CharField( max_length = 500, default = "", null = True )
    content = models.CharField( max_length = 1000, default = "", null = True )
    img_url_1 = models.CharField( max_length = 500, default = "http://i.imgur.com/0i6g2kx.png" )
    img_url_2 = models.CharField( max_length = 500, default = "http://i.imgur.com/0i6g2kx.png" )
    
    def set_default_models( self ) :
        OurCompanyContent( title = "Our Company has created 1928..." ).save()
    
    def __str__( self ) :
        return self.title
        
class OurServicesContent( models.Model ) :
    
    icon = models.CharField( max_length = 50, default = "", null = True )
    title = models.CharField( max_length = 500, default = "", null = True )
    content = models.CharField( max_length = 1000, default = "", null = True )
    
    def set_default_models( self ) :
        OurServicesContent( icon = "fa fa-cog", title = "Easy to Customize" ).save()
        OurServicesContent( icon = "fa fa-dropbox", title = "Ready to Use" ).save()
        OurServicesContent( icon = "fa fa-desktop", title = "Responsive Layout" ).save()
    
    def __str__( self ) :
        return self.title

class Recomendations( models.Model ) :
    
    content = models.CharField( max_length = 1000, default = "", null = True )
    source = models.CharField( max_length = 500, default = "", null = True )
    
    def set_default_models( self ) :
        Recomendations( source = "Fuente 1" ).save()
        Recomendations( source = "Fuente 2" ).save()
    
    def __str__( self ) :
        return self.source

class OurPersonalContent( models.Model ) :
    
    content = models.CharField( max_length = 1000, default = "", null = True )
    img_url = models.CharField( max_length = 500, default = "http://i.imgur.com/0i6g2kx.png" )
    
    def set_default_models( self ) :
        OurPersonalContent().save()
    
    def __str__( self ) :
        return self.img_url

class OurProductsContent( models.Model ) :
    
    price_range = models.CharField( max_length = 100, default = "", null = True )
    product_name = models.CharField( max_length = 100, default = "", null = True )
    content = models.CharField( max_length = 1000, default = "", null = True )
    
    def set_default_models( self ) :
        OurProductsContent( product_name = "Cabañas" ).save()
        OurProductsContent( product_name = "Albercas" ).save()
        OurProductsContent( product_name = "Áreas Recreativas" ).save()
    
    def __str__( self ) :
        return self.product_name