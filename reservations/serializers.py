# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import *
from products.serializers import *
from custom_auth.serializers import UserCatSerializer

class DetailSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = Detail
        fields = ( 'id', 'user', 'qty', )
        
class DetailCabinSerializer( serializers.ModelSerializer ) :
    product = CabinSerializer( many = False )
    class Meta :
        model = DetailCabin
        fields = '__all__'

class DetailPoolSerializer( serializers.ModelSerializer ) :
    
    product = PoolSerializer( many = False )
    
    class Meta :
        model = DetailPool
        fields = ( 'id', 'product', )

class DetailAreaSerializer( serializers.ModelSerializer ) :
    
    product = AreaSerializer( many = False )
    
    class Meta :
        model = DetailArea
        fields = ( 'id', 'product', )

class ReservationTypeSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = ReservationType
        fields = ( 'id', 'user', 'name', 'description', 'value', 'timestamp', 'updated', )

class ReservationInfoSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = ReservationInfo
        fields = ( 'id', 'user', 'full_name', 'address1', 'address2', 'zip_code', 'city', 'state', 'country', 'email', 'phone_number', )
        
class ReservationSerializer( serializers.ModelSerializer ) :
    
    user = UserCatSerializer( many = False )
    reservation_type = ReservationTypeSerializer( many = False )
    reservation_info = ReservationInfoSerializer( many = False )
    details = DetailCabinSerializer( many = True )
    class Meta :
        model = Reservation
        fields = ( 'id', 'user', 'user_client', 'reservation_info', 'reservation_type', 'date_start', 'date_end', 'details', 'timestamp', 'updated', )

class PaymentStatusSerializer( serializers.ModelSerializer ) :
    
    class Meta :
        model = PaymentStatus
        fields = ( 'id', 'name', 'description', 'value', 'timestamp', 'updated', )
        
class PaymentSerializer( serializers.ModelSerializer ) :
    
    payment_status = PaymentStatusSerializer( many = False )
    
    class Meta :
        model = Payment
        fields = ( 'id', 'preference_mp_id', 'preference_mp_init_point', 'collection_id', 'payment_status', 'timestamp', 'updated', )
        
class ReservationCabinSerializer( serializers.ModelSerializer ) :
    
    user = UserCatSerializer( many = False )
    reservation_info = ReservationInfoSerializer( many = False )
    details = DetailCabinSerializer( many = True )
    payment_status = PaymentStatusSerializer( many = False )
    payment_info = PaymentSerializer( many = False )
    
    class Meta :
        model = ReservationCabin
        fields = ( 'id', 'extended_token', 'user', 'user_client', 'payment_status', 'payment_info', 'reservation_info', 'total', 'date_start', 'max_guests', 'extra_guests_child', 'extra_guests_adult', 'date_end', 'details', 'timestamp', 'updated', )

class PromotionSerializer( serializers.ModelSerializer ) :
    
    user = UserCatSerializer( many = False )
    
    class Meta :
        model = Promotion
        fields = ( 'id', 'name', 'description', 'discount', 'user', 'date_start', 'date_end', 'timestamp', 'updated', )