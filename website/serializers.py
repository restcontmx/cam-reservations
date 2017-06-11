from rest_framework import serializers
from .models import *

class OurCompanyContentSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = OurCompanyContent
        fields = ( 'id', 'title', 'content', 'img_url_1', 'img_url_2' )
        
class OurServicesContentSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = OurServicesContent
        fields = ( 'id', 'icon', 'title', 'content' )
        
class RecomendationsSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = Recomendations
        fields = ( 'id', 'content', 'source' )
        
class OurPersonalContentSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = OurPersonalContent
        fields = ( 'id', 'content', 'img_url' )
        
class OurProductsContentSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = OurProductsContent
        fields = ( 'id', 'price_range', 'product_name', 'content' )