from rest_framework import serializers
from .models import AreaType, Area, CabinType, Cabin, Pool


class AreaTypeSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = AreaType
        fields = ( 'id', 'user', 'name', 'description', 'max_guests', 'timestamp', 'updated', )

class AreaSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = Area
        fields = ( 'id', 'user', 'name', 'description', 'price', 'pools', 'area_type', 'timestamp', 'updated', )

class CabinTypeSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = CabinType
        fields = ( 'id', 'user', 'name', 'description', 'rooms', 'max_guests', 'max_extra_guests', 'timestamp', 'updated', )

class CabinSerializer( serializers.ModelSerializer ) :
    cabin_type = CabinTypeSerializer( many = False )
    class Meta :
        model = Cabin
        fields = ( 'id', 'user', 'name', 'description', 'cabin_type', 'price', 'img_url', 'timestamp', 'updated', )

class PoolSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = Pool
        fields = ( 'id', 'user', 'name', 'description', 'max_people', 'price', 'img_url', 'timestamp', 'updated', )