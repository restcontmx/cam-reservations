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
import json
import simplejson

class AlertNumbersSettingsListAPIView( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin )
    queryset = AlertNumbers.objects.all()
    serializer_class = AlertNumbersSerializer
    
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

class AlertNumbersSettingsUpdateAPIView( generics.UpdateAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin )
    queryset = AlertNumbers.objects.all()
    serializer_class = AlertNumbersSerializer
    
    def update( self, request, *args, **kwargs ) :
        """ List objects; """
        try :
            the_data = json.dumps( self.decrypt_long_data( request.body ), ensure_ascii = False )
            json_formated = json.loads( the_data )
            json_decoded = json.loads( json_formated )
            
            for an_d in json_decoded :
                an = AlertNumbers.objects.get( pk = int( an_d['id'] ) )
                an.name = an_d['name']
                an.phone_number = an_d['phone_number']
                an.save()
                
            instance = self.get_queryset()
            serialized = self.get_serializer( instance, many = True )
            data = { DATA : serialized.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : ( "There was an error; Error: {0}" ).format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )
          
class AlertEmailsSettingsListAPIView( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin )
    queryset = AlertEmails.objects.all()
    serializer_class = AlertEmailsSerializer
    
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

class AlertEmailsSettingsUpdateAPIView( generics.UpdateAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin )
    queryset = AlertEmails.objects.all()
    serializer_class = AlertEmailsSerializer
    
    def update( self, request, *args, **kwargs ) :
        """ List objects; """
        try :
            the_data = json.dumps( self.decrypt_long_data( request.body ), ensure_ascii = False )
            json_formated = json.loads( the_data )
            json_decoded = json.loads( json_formated )
            
            for ae_d in json_decoded :
                ae = AlertEmails.objects.get( pk = int( ae_d['id'] ) )
                ae.name = ae_d['name']
                ae.email = ae_d['email']
                ae.save()
                
            instance = self.get_queryset()
            serialized = self.get_serializer( instance, many = True )
            data = { DATA : serialized.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : ( "There was an error; Error: {0}" ).format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )

class ContactEmailSettingsListAPIView( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin )
    queryset = ContactEmail.objects.all()
    serializer_class = ContactEmailSerializer
    
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

class ContactEmailSettingsUpdateAPIView( generics.UpdateAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin )
    queryset = ContactEmail.objects.all()
    serializer_class = ContactEmailSerializer
    
    def update( self, request, *args, **kwargs ) :
        """ List objects; """
        try :
            the_data = json.dumps( self.decrypt_long_data( request.body ), ensure_ascii = False )
            json_formated = json.loads( the_data )
            json_decoded = json.loads( json_formated )
            
            for ce_d in json_decoded :
                ce = ContactEmail.objects.get( pk = int( ce_d['id'] ) )
                ce.name = ce_d['name']
                ce.email = ce_d['email']
                ce.save()
                
            instance = self.get_queryset()
            serialized = self.get_serializer( instance, many = True )
            data = { DATA : serialized.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : ( "There was an error; Error: {0}" ).format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )
 
class TicketPricesSettingsListAPIView( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsSystemWorthy )
    queryset = TicketPrices.objects.all()
    serializer_class = TicketPricesSerializer 
    
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

class TicketPricesSettingsUpdateAPIView( generics.UpdateAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin )
    queryset = TicketPrices.objects.all()
    serializer_class = TicketPricesSerializer
    
    def update( self, request, *args, **kwargs ) :
        """ List objects; """
        try :
            the_data = json.dumps( self.decrypt_long_data( request.body ), ensure_ascii = False )
            json_formated = json.loads( the_data )
            json_decoded = json.loads( json_formated )
            
            for tp_d in json_decoded :
                tp = TicketPrices.objects.get( pk = int( tp_d['id'] ) )
                tp.name = tp_d['name']
                tp.price = float( tp_d['price'] )
                tp.save()
            
            instance = self.get_queryset()
            serialized = self.get_serializer( instance, many = True )
            data = { DATA : serialized.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : ( "There was an error; Error: {0}" ).format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )

class SignaturesSettingsListAPIView( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin )
    queryset = Signatures.objects.all()
    serializer_class = SignaturesSerializer
    
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