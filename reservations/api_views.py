# -*- coding: utf-8 -*-
"""
products.api_views
Author - Ramiro Gutierrez Alaniz
Date - January, 16th 2017
"""

# Imports
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404, JsonResponse
from django.contrib.auth.models import User
from django.core import serializers
from django.contrib.auth import authenticate
# Rest framework imports
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
# Import classes 
from helpers.encryption_system import SecuritySystem
from custom_auth.permissions import IsApplication, IsSystemWorthy, IsSuperAdmin, IsAdmin
from .models import *
from .serializers import * 
# Import error handler 
from helpers.error_handler import *
from helpers.imgur import *
from helpers.mail_helper import *
import json
import simplejson
# Image decode shit
from PIL import Image
from base64 import *
from datetime import datetime
import mercadopago

"""
Reservation type list api view
this is the kind of reservation like cabin, área, etc etc.
"""
class ReservationTypeListAPIView( generics.ListCreateAPIView, SecuritySystem  ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin, )
    serializer_class = ReservationTypeSerializer
    queryset = ReservationType.objects.all()
    
    def list( self, request, *args, **kwargs ) :
        
        try :
            instance = self.get_queryset()
            serialized = self.get_serializer( instance, many = True )
            data = { DATA : serialized.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : ( "There was an error; Error: {0}" ).format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )

class ReservationTypeCreateAPIView( generics.CreateAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsSuperAdmin, )
    serializer_class = ReservationTypeSerializer
    queryset = ReservationType.objects.all()
    
    def create( self, request, *args, **kwargs ) :
        """ create function; creates an object duuuh """
        try :
            the_data = json.dumps( self.decrypt_long_data( request.body ), ensure_ascii = False )
            json_formated = json.loads( the_data )
            json_decoded = json.loads( json_formated )
            
            instance =  ReservationType( 
                user = request.user,
                name = json_decoded[ 'name' ],
                description = json_decoded[ 'description' ],
                value = int( json_decoded[ 'value' ] )
            )
            instance.save()
            
            serialized = self.get_serializer( instance, many = False )
            data = { DATA : serialized.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_201_CREATED )
        except Exception as e :
            data = { MESSAGE : ( "There was an error; Error: {0}" ).format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )
            
class ReservationTypeRetrieveUpdateDestroyAPIView( generics.RetrieveUpdateDestroyAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsSuperAdmin, )
    serializer_class = ReservationTypeSerializer
    queryset = ReservationType.objects.all()
    
    def retrieve( self, request, *args, **kwargs ) :
        """ retrieve object with id """
        try :
            instance = self.get_object()
            serializer = self.get_serializer( instance, many = False )
            data = { DATA : serializer.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : "There was an error; error: {0}".format( str( e ) ) }
            return Response( self.encrypt_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )
            
    def update( self, request, *args, **kwargs ) :
        """ update object with id """
        try :
            the_data = json.dumps( self.decrypt_long_data( request.body ), ensure_ascii=False )
            json_formated = json.loads( the_data )
            json_decoded = json.loads( json_formated )
            
            instance = self.get_object()
            instance.name = json_decoded['name']
            instance.description = json_decoded['description']
            instance.value = json_decoded['value']
            instance.save()

            serializer = self.get_serializer( instance, many = False )
            data = { DATA : serializer.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : "There was an error; error: {0}".format( str( e ) ) }
            return Response( self.encrypt_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )
    
    def destroy( self, request, *args, **kwargs ) :
        """ delete object with id """
        try : 
            instance = self.get_object()
            instance.delete()
            data = { MESSAGE : "Objecto borrado." }
            return Response( self.encrypt_data( json.dumps( data ) ), status = status.HTTP_204_NO_CONTENT )
        except Exception as e :
            data = { MESSAGE : "There was an error; error: {0}".format( str( e ) ) }
            return Response( self.encrypt_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST ) 
        

class ReservationInfoCreateAPIView( generics.CreateAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin,  )
    serializer_class = ReservationInfoSerializer
    queryset = ReservationInfo.objects.all()
    
    def create( self, request, *args, **kwargs ) :
        """ create function; creates an object duuuh """
        try :
            the_data = json.dumps( self.decrypt_long_data( request.body ), ensure_ascii = False )
            json_formated = json.loads( the_data )
            json_decoded = json.loads( json_formated )
            
            instance =  ReservationInfo( 
                user = request.user,
                full_name = json_decoded[ 'full_name' ],
                address1 = json_decoded[ 'address1' ],
                address2 = json_decoded[ 'address2' ],
                zip_code = json_decoded[ 'zip_code' ],
                city = json_decoded[ 'city' ],
                state = json_decoded[ 'state' ],
                country = json_decoded[ 'country' ],
                email = json_decoded[ 'email' ], 
                phone_number = json_decoded[ 'phone_number' ]
            )
            instance.save()
            
            serialized = self.get_serializer( instance, many = False )
            data = { DATA : serialized.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_201_CREATED )
        except Exception as e :
            data = { MESSAGE : ( "There was an error; Error: {0}" ).format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )
        
class ReservationInfoRetrieveUpdateDestroyAPIView( generics.RetrieveUpdateDestroyAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin,  )
    serializer_class = ReservationInfoSerializer
    queryset = ReservationInfo.objects.all()

    def retrieve( self, request, *args, **kwargs ) :
        """ retrieve object with id """
        try :
            instance = self.get_object()
            serializer = self.get_serializer( instance, many = False )
            data = { DATA : serializer.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : "There was an error; error: {0}".format( str( e ) ) }
            return Response( self.encrypt_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )
            
    def update( self, request, *args, **kwargs ) :
        """ update object with id """
        try :
            the_data = json.dumps( self.decrypt_long_data( request.body ), ensure_ascii=False )
            json_formated = json.loads( the_data )
            json_decoded = json.loads( json_formated )
            
            instance = self.get_object()
            
            instance.full_name = json_decoded[ 'full_name' ]
            instance.address1 = json_decoded[ 'address1' ]
            instance.address2 = json_decoded[ 'address2' ]
            instance.zip_code = json_decoded[ 'zip_code' ]
            instance.city = json_decoded[ 'city' ]
            instance.state = json_decoded[ 'state' ]
            instance.country = json_decoded[ 'country' ]
            instance.email = json_decoded[ 'email' ] 
            instance.phone_number = json_decoded[ 'phone_number' ]
            
            instance.save()

            serializer = self.get_serializer( instance, many = False )
            data = { DATA : serializer.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : "There was an error; error: {0}".format( str( e ) ) }
            return Response( self.encrypt_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )

    def destroy( self, request, *args, **kwargs ) :
        """ delete object with id """
        try : 
            instance = self.get_object()
            instance.delete()
            data = { MESSAGE : "Objecto borrado." }
            return Response( self.encrypt_data( json.dumps( data ) ), status = status.HTTP_204_NO_CONTENT )
        except Exception as e :
            data = { MESSAGE : "There was an error; error: {0}".format( str( e ) ) }
            return Response( self.encrypt_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST ) 
        
class PaymentStatusListAPIView( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin,  )
    serializer_class = PaymentStatusSerializer
    queryset = PaymentStatus.objects.all()

    def list( self, request, *args, **kwargs ) :
        
        try :
            instance = self.get_queryset()
            serialized = self.get_serializer( instance, many = True )
            data = { DATA : serialized.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : ( "There was an error; Error: {0}" ).format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )

class PaymentStatusCreateAPIView( generics.CreateAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin,  )
    serializer_class = PaymentStatusSerializer
    queryset = PaymentStatus.objects.all()

    def create( self, request, *args, **kwargs ) :
        """ create function; creates an object duuuh """
        try :
            the_data = json.dumps( self.decrypt_long_data( request.body ), ensure_ascii = False )
            json_formated = json.loads( the_data )
            json_decoded = json.loads( json_formated )
            
            instance =  PaymentStatus( 
                user = request.user,
                name = json_decoded[ 'name' ],
                description = json_decoded[ 'description' ],
                value = int( json_decoded[ 'value' ] )
            )
            
            instance.save()
            
            serialized = self.get_serializer( instance, many = False )
            data = { DATA : serialized.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_201_CREATED )
        except Exception as e :
            data = { MESSAGE : ( "There was an error; Error: {0}" ).format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )
    
class PaymentStatusRetrieveUpdateDestroyAPIView( generics.RetrieveUpdateDestroyAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin,  )
    serializer_class = PaymentStatusSerializer
    queryset = PaymentStatus.objects.all()
    
    def retrieve( self, request, *args, **kwargs ) :
        """ retrieve object with id """
        try :
            instance = self.get_object()
            serializer = self.get_serializer( instance, many = False )
            data = { DATA : serializer.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : "There was an error; error: {0}".format( str( e ) ) }
            return Response( self.encrypt_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )
            
    def update( self, request, *args, **kwargs ) :
        """ update object with id """
        try :
            the_data = json.dumps( self.decrypt_long_data( request.body ), ensure_ascii=False )
            json_formated = json.loads( the_data )
            json_decoded = json.loads( json_formated )
            
            instance = self.get_object()
            
            instance.name = json_decoded[ 'name' ]
            instance.description = json_decoded[ 'description' ]
            instance.value = int( json_decoded[ 'value' ] )
            
            instance.save()

            serializer = self.get_serializer( instance, many = False )
            data = { DATA : serializer.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : "There was an error; error: {0}".format( str( e ) ) }
            return Response( self.encrypt_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )

    def destroy( self, request, *args, **kwargs ) :
        """ delete object with id """
        try : 
            instance = self.get_object()
            instance.delete()
            data = { MESSAGE : "Objecto borrado." }
            return Response( self.encrypt_data( json.dumps( data ) ), status = status.HTTP_204_NO_CONTENT )
        except Exception as e :
            data = { MESSAGE : "There was an error; error: {0}".format( str( e ) ) }
            return Response( self.encrypt_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST ) 
        
    
class PromotionListAPIView( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin,  )
    serializer_class = PromotionSerializer
    queryset = Promotion.objects.all()
    
    def list( self, request, *args, **kwargs ) :
        """ List objects; """
        try :
            instance = self.get_queryset()
            serialized = self.get_serializer( instance, many = True )
            data = { DATA : serialized.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : ( "There was an error; Error: {0}" ).format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )

class PromotionCreateAPIView( generics.CreateAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin,  )
    serializer_class = PromotionSerializer
    queryset = Promotion.objects.all()

    def create( self, request, *args, **kwargs ) :
        """ create function; creates an object duuuh """
        try :
            the_data = json.dumps( self.decrypt_long_data( request.body ), ensure_ascii = False )
            json_formated = json.loads( the_data )
            json_decoded = json.loads( json_formated )
            
            instance =  Promotion( 
                user = request.user,
                name = json_decoded[ 'name' ],
                description = json_decoded[ 'description' ],
                discount = float( json_decoded[ 'discount' ] ),
                date_start = datetime.strptime( json_decoded['date_start'], "%Y/%m/%d %H:%M").date(),
                date_end = datetime.strptime( json_decoded['date_end'], "%Y/%m/%d %H:%M").date()
            )
            instance.save()
            
            serialized = self.get_serializer( instance, many = False )
            data = { DATA : serialized.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_201_CREATED )
        except Exception as e :
            data = { MESSAGE : ( "There was an error; Error: {0}" ).format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )
    
class PromotionRetrieveUpdateDestroyAPIView( generics.RetrieveUpdateDestroyAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin,  )
    serializer_class = PromotionSerializer
    queryset = Promotion.objects.all()
    
    def retrieve( self, request, *args, **kwargs ) :
        """ retrieve object with id """
        try :
            instance = self.get_object()
            serializer = self.get_serializer( instance, many = False )
            data = { DATA : serializer.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : "There was an error; error: {0}".format( str( e ) ) }
            return Response( self.encrypt_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )
            
    def update( self, request, *args, **kwargs ) :
        """ update object with id """
        try :
            the_data = json.dumps( self.decrypt_long_data( request.body ), ensure_ascii=False )
            json_formated = json.loads( the_data )
            json_decoded = json.loads( json_formated )
            
            instance = self.get_object()
            
            instance.name = json_decoded[ 'name' ]
            instance.description = json_decoded[ 'description' ]
            instance.discount = float( json_decoded[ 'discount' ] )
            instance.date_start = datetime.strptime( json_decoded['date_start'], "%Y/%m/%d %H:%M").date()
            instance.date_end = datetime.strptime( json_decoded['date_end'], "%Y/%m/%d %H:%M").date()
            
            instance.save()

            serializer = self.get_serializer( instance, many = False )
            data = { DATA : serializer.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : "There was an error; error: {0}".format( str( e ) ) }
            return Response( self.encrypt_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )

    def destroy( self, request, *args, **kwargs ) :
        """ delete object with id """
        try : 
            instance = self.get_object()
            instance.delete()
            data = { MESSAGE : "Objecto borrado." }
            return Response( self.encrypt_data( json.dumps( data ) ), status = status.HTTP_204_NO_CONTENT )
        except Exception as e :
            data = { MESSAGE : "There was an error; error: {0}".format( str( e ) ) }
            return Response( self.encrypt_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST ) 
        
class ReservationListAdminAPIView( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin,  )
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()

class ReservationCabinListCreateAPIView( generics.ListCreateAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsSystemWorthy,  )
    serializer_class = ReservationCabinSerializer
    queryset = ReservationCabin.objects.all()
    
    def list( self, request, *args, **kwargs ) :
        """ List objects; """
        try :
            start_date = datetime.strptime( request.GET['d1'], "%Y-%m-%d" ).date()
            end_date = datetime.strptime( request.GET['d2'], "%Y-%m-%d" ).date()
            instance = ReservationCabin().get_cabins_for_calendar( start_date, end_date )
            serialized = self.get_serializer( instance, many = True )
            data = { DATA : serialized.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : ( "There was an error; Error: {0}" ).format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )

    def create( self, request, *args, **kwargs ) :
        """ create function; creates an object duuuh """
        try :
            the_data = json.dumps( self.decrypt_long_data( request.body ), ensure_ascii = False )
            json_formated = json.loads( the_data )
            json_decoded = json.loads( json_formated )

            reservation_info_json = json_decoded['reservationinfo']
            
            reservation_info = ReservationInfo(
                user = request.user,
                full_name = reservation_info_json['full_name'],
                address1 = reservation_info_json['address1'],
                address2 = reservation_info_json['address2'],
                zip_code = reservation_info_json['zip_code'],
                city = reservation_info_json['city'],
                state = reservation_info_json['state'],
                country = reservation_info_json['country'],
                email = reservation_info_json['email'],
                phone_number = reservation_info_json['phone_number'] )
            reservation_info.save()
            
            temp_payment = Payment()
            temp_payment.save()
            
            instance = ReservationCabin(
                user = request.user,
                reservation_info = reservation_info, 
                max_guests = int( json_decoded['max_guests'] ),
                extra_guests_child = int( json_decoded['extra_guests_child'] ),
                extra_guests_adult = int( json_decoded['extra_guests_adult'] ),
                total = float( json_decoded['total'] ),
                date_start = datetime.strptime( json_decoded['date_start'], "%Y/%m/%d").date(),
                date_end = datetime.strptime( json_decoded['date_end'], "%Y/%m/%d").date(),
                payment_info = temp_payment )
            instance.save()
            
            for p in json_decoded['details'] :
                product = p['product']
                detail = DetailCabin( product = Cabin.objects.get( pk = int( product['id'] ) ), qty = int( p['qty'] ), user = request.user )
                detail.save()
                instance.details.add( detail )
            
            # reservation_cabin_to_alert( instance )
            # reservation_cabin_to_alerts( instance )
            
            serialized = self.get_serializer( instance, many = False )
            data = { DATA : serialized.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_201_CREATED )
        except Exception as e :
            data = { MESSAGE : ( "There was an error; Error: {0}" ).format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )

class ReservationCabinRetrieveUpdateDestroyAPIView( generics.RetrieveUpdateDestroyAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsSystemWorthy, )
    serializer_class = ReservationCabinSerializer
    queryset = ReservationCabin.objects.all()
    
    def update( self, request, *args, **kwargs ) :
        """ update object with id """
        try :
            
            instance = self.get_object()
 
            the_data = json.dumps( self.decrypt_long_data( request.body ), ensure_ascii = False )
            json_formated = json.loads( the_data )
            json_decoded = json.loads( json_formated )

            reservation_info_json = json_decoded['reservation_info']
            payment_info_json = json_decoded['payment_info']
            
            instance.reservation_info.full_name = reservation_info_json['full_name']
            instance.reservation_info.address1 = reservation_info_json['address1']
            instance.reservation_info.address2 = reservation_info_json['address2']
            instance.reservation_info.zip_code = reservation_info_json['zip_code']
            instance.reservation_info.city = reservation_info_json['city']
            instance.reservation_info.state = reservation_info_json['state']
            instance.reservation_info.country = reservation_info_json['country']
            instance.reservation_info.email = reservation_info_json['email']
            instance.reservation_info.phone_number = reservation_info_json['phone_number']
            instance.reservation_info.save()
            
            instance.payment_info.preference_mp_id = payment_info_json['preference_mp_id']
            instance.payment_info.preference_mp_init_point = payment_info_json['preference_mp_init_point'];
            instance.payment_info.collection_id = payment_info_json['collection_id'];
            instance.payment_info.save()
            
            instance.save()
            
            serializer = self.get_serializer( instance, many = False )
            data = { DATA : serializer.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : "There was an error; error: {0}".format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )

    def retrieve( self, request, *args, **kwargs ) :
        """ retrieve function returns the object detail """
        try : 
            instance = self.get_object()
            serializer = self.get_serializer( instance, many = False )
            data = { DATA : serializer.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : "There was an error; error: {0}".format( str( e ) ) }
            return Response( self.encrypt_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )

    def destroy( self, request, *args, **kwargs ) :
        """ delete function that deletes a reservation and a reservation info """
        try :
            instance = self.get_object()
            ri = instance.reservation_info
            instance.delete()
            ri.delete()
            data = { MESSAGE : "Objecto borrado." }
            return Response( self.encrypt_data( json.dumps( data ) ), status = status.HTTP_204_NO_CONTENT )
        except Exception as e :
            data = { MESSAGE : ( "There was an error; Error: {0}" ).format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )
            
class ProductCabinListFromDatesAPIView( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsSystemWorthy, )
    serializer_class = CabinSerializer
    queryset = Cabin.objects.all()
    
    def list( self, request, *args, **kwargs ) :
        """ List objects; """
        try :
            start_date = datetime.strptime( request.GET['d1'], "%Y-%m-%d" ).date()
            end_date = datetime.strptime( request.GET['d2'], "%Y-%m-%d" ).date()
            instance = ReservationCabin().get_cabins_availables( start_date, end_date )
            serialized = self.get_serializer( instance, many = True )
            data = { DATA : serialized.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : ( "There was an error; Error: {0}" ).format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )
            
class ReservationCabinUpdatePaymentStatusAPIView( generics.UpdateAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsSystemWorthy, )
    serializer_class = ReservationCabinSerializer
    queryset = ReservationCabin.objects.all()
    
    def update( self, request, *args, **kwargs ) :
        """ update object with id """
        try :
            instance = self.get_object()
            instance.payment_info.payment_status = PaymentStatus.objects.get( value = 2 )
            instance.payment_info.save()
            data = { DATA : "La reservación se ha establecido como pagada." }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : "There was an error; error: {0}".format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )

"""
This will manage the mercado pago notifications for payments
"""
class NotificationsAPIView( generics.CreateAPIView ) :
    
    queryset = ReservationCabin.objects.all()
    
    def create( self, request, *args, **kwargs ) :
        """ create function; creates an object duuuh """
        mp = mercadopago.MP("2620041704606675", "ek7dhDMzyAx3N2VXoZCQ4awuPi3F12CA")
        
        try :
            payment_id = request.query_params['id']
            payment_info = mp.get_payment_info( payment_id )
            if payment_info["status"] == 200:
                resp = payment_info["response"]
                if resp["collection"]["external_reference"] is not None :
                    reservation = ReservationCabin.objects.get( extended_token = resp["collection"]["external_reference"] )
                    reservation.payment_info.collection_id = int(payment_id)
                    if resp["collection"]["status"] == "approved" :
                        reservation.payment_info.payment_status = PaymentStatus.objects.get( value = 2 )
                    else :
                        reservation.payment_info.payment_status = PaymentStatus.objects.get( value = 1 )
                    reservation.payment_info.save()
            data = { MESSAGE : "OK" }
            return Response( json.dumps( data ), status = status.HTTP_200_OK )
        except Exception as e :
            print( e )
            data = { MESSAGE : "OK" }
            return Response( json.dumps( data ), status = status.HTTP_200_OK )
            