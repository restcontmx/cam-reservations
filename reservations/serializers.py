# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Detail, DetailCabin, DetailArea, DetailPool, ReservationType, ReservationInfo, Reservation, PaymentStatus, Promotion, Payment
from products.serializers import CabinSerializer, AreaSerializer, PoolSerializer
from custom_auth.serializers import UserCatSerializer

class DetailSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = Detail
        fields = ( 'id', 'user', 'qty', )
        
class DetailCabinSerializer( serializers.ModelSerializer ) :
    
    product = CabinSerializer( many = False )
    
    class Meta :
        model = DetailCabin
        fields = ( 'id', 'product', )

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
    details = DetailSerializer( many = True )
    
    class Meta :
        model = Reservation
        fields = ( 'id', 'user', 'user_client', 'reservation_info', 'reservation_type', 'details', 'timestamp', 'updated', )

class PaymentStatusSerializer( serializers.ModelSerializer ) :
    
    class Meta :
        model = PaymentStatus
        fields = ( 'id', 'name', 'description', 'value', 'timestamp', 'updated', )
        
class PromotionSerializer( serializers.ModelSerializer ) :
    
    user = UserCatSerializer( many = False )
    
    class Meta :
        model = Promotion
        fields = ( 'id', 'name', 'description', 'discount', 'user', 'date_start', 'date_end', 'timestamp', 'updated', )
        
class PaymentSerializer( serializers.ModelSerializer ) :
    
    reservation = ReservationSerializer( many = False )
    payment_status = PaymentStatusSerializer( many = False )
    promotion = PromotionSerializer( many = False )
    
    class Meta :
        model = Payment
        fields = ( 'id', 'reservation', 'promotion', 'payment_status', 'total', 'timestamp', 'updated', )
        