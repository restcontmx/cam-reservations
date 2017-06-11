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
from .models import*
from .serializers import *
# Import error handler 
from helpers.error_handler import *
from helpers.imgur import *
from helpers.mail_helper import *
from reservations.models import ReservationCabin
from reservations.serializers import ReservationCabinSerializer

import json
import simplejson

class OurCompanyContentListAPIView( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin )
    queryset = OurCompanyContent.objects.all()
    serializer_class = OurCompanyContentSerializer

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

class OurCompanyContentUpdateAPIView( generics.UpdateAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin )
    queryset = OurCompanyContent.objects.all()
    serializer_class = OurCompanyContentSerializer
    
    def update( self, request, *args, **kwargs ) :
        """ List objects; """
        try :
            the_data = json.dumps( self.decrypt_long_data( request.body ), ensure_ascii = False )
            json_formated = json.loads( the_data )
            json_decoded = json.loads( json_formated )
            
            for occ_d in json_decoded :
                occ = OurCompanyContent.objects.get( pk = int( occ_d['id'] ) )
                occ.content = occ_d['content']
                occ.title = occ_d['title']
                occ.save()
                
            instance = self.get_queryset()
            serialized = self.get_serializer( instance, many = True )
            data = { DATA : serialized.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : ( "There was an error; Error: {0}" ).format( str( e ) ) }
       
class OurServicesContentListAPIView( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin )
    queryset = OurServicesContent.objects.all()
    serializer_class = OurServicesContentSerializer

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

class OurServicesContentUpdateAPIView( generics.UpdateAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin )
    queryset = OurServicesContent.objects.all()
    serializer_class = OurServicesContentSerializer
    
    def update( self, request, *args, **kwargs ) :
        """ List objects; """
        try :
            the_data = json.dumps( self.decrypt_long_data( request.body ), ensure_ascii = False )
            json_formated = json.loads( the_data )
            json_decoded = json.loads( json_formated )
            
            for osc_d in json_decoded :
                osc = OurServicesContent.objects.get( pk = int( osc_d['id'] ) )
                osc.content = osc_d['content']
                osc.title = osc_d['title']
                osc.icon = osc_d['icon']
                osc.save()
                
            instance = self.get_queryset()
            serialized = self.get_serializer( instance, many = True )
            data = { DATA : serialized.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : ( "There was an error; Error: {0}" ).format( str( e ) ) }
          
class RecomendationsListAPIView( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin )
    queryset = Recomendations.objects.all()
    serializer_class = RecomendationsSerializer

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

class RecomendationsUpdateAPIView( generics.UpdateAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin )
    queryset = Recomendations.objects.all()
    serializer_class = RecomendationsSerializer
    
    def update( self, request, *args, **kwargs ) :
        """ List objects; """
        try :
            the_data = json.dumps( self.decrypt_long_data( request.body ), ensure_ascii = False )
            json_formated = json.loads( the_data )
            json_decoded = json.loads( json_formated )
            
            for r_d in json_decoded :
                r = Recomendations.objects.get( pk = int( r_d['id'] ) )
                r.content = r_d['content']
                r.source = r_d['source']
                r.save()
                
            instance = self.get_queryset()
            serialized = self.get_serializer( instance, many = True )
            data = { DATA : serialized.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : ( "There was an error; Error: {0}" ).format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )

class OurPersonalContentListAPIView( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin )
    queryset = OurPersonalContent.objects.all()
    serializer_class = OurPersonalContentSerializer

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

class OurPersonalContentUpdateAPIView( generics.UpdateAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin )
    queryset = OurPersonalContent.objects.all()
    serializer_class = OurPersonalContentSerializer

    def update( self, request, *args, **kwargs ) :
        """ List objects; """
        try :
            the_data = json.dumps( self.decrypt_long_data( request.body ), ensure_ascii = False )
            json_formated = json.loads( the_data )
            json_decoded = json.loads( json_formated )
            
            for opc_d in json_decoded :
                opc = OurPersonalContent.objects.get( pk = int( opc_d['id'] ) )
                opc.content = opc_d['content']
                opc.save()
                
            instance = self.get_queryset()
            serialized = self.get_serializer( instance, many = True )
            data = { DATA : serialized.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : ( "There was an error; Error: {0}" ).format( str( e ) ) }

class OurProductsContentListAPIView( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin )
    queryset = OurProductsContent.objects.all()
    serializer_class = OurProductsContentSerializer

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

class OurProductsContentUpdateAPIView( generics.UpdateAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin )
    queryset = OurProductsContent.objects.all()
    serializer_class = OurProductsContentSerializer
    
    def update( self, request, *args, **kwargs ) :
        """ List objects; """
        try :
            the_data = json.dumps( self.decrypt_long_data( request.body ), ensure_ascii = False )
            json_formated = json.loads( the_data )
            json_decoded = json.loads( json_formated )
            
            for opc_d in json_decoded :
                opc = OurProductsContent.objects.get( pk = int( opc_d['id'] ) )
                opc.content = opc_d['content']
                opc.product_name = opc_d['product_name']
                opc.price_range = opc_d['price_range']
                opc.save()
                
            instance = self.get_queryset()
            serialized = self.get_serializer( instance, many = True )
            data = { DATA : serialized.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : ( "There was an error; Error: {0}" ).format( str( e ) ) }
   
class Image1ToOurCompanyContent( APIView ) :
    
    def get_object( self, pk ) :
        """Get object function """
        try :
            return OurCompanyContent.objects.get( pk=pk )
        except OurCompanyContent.DoesNotExist :
            raise Http404
    
    def put( self, request, pk, format=None ) :
        try :
            fh = open( "imageToSaveOurCompanyContent" + pk + ".png", "wb" )
            fh.write( request.data.decode( "base64" ) )
            fh.close()
            instance = self.get_object( pk )
            instance.img_url_1 = save_image( "imageToSaveOurCompanyContent" + pk + ".png" )
            instance.save()
            serialized = OurCompanyContentSerializer( instance, many = None )
            data = { DATA : serialized.data }
            return Response( data, status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : "There was an error; error: {0}".format( str( e ) ) }
            return Response( data, status = status.HTTP_400_BAD_REQUEST )

class Image2ToOurCompanyContent( APIView ) :
    
    def get_object( self, pk ) :
        """Get object function """
        try :
            return OurCompanyContent.objects.get( pk=pk )
        except OurCompanyContent.DoesNotExist :
            raise Http404
    
    def put( self, request, pk, format=None ) :
        try :
            fh = open( "imageToSaveOurCompanyContent" + pk + ".png", "wb" )
            fh.write( request.data.decode( "base64" ) )
            fh.close()
            instance = self.get_object( pk )
            instance.img_url_2 = save_image( "imageToSaveOurCompanyContent" + pk + ".png" )
            instance.save()
            serialized = OurCompanyContentSerializer( instance, many = None )
            data = { DATA : serialized.data }
            return Response( data, status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : "There was an error; error: {0}".format( str( e ) ) }
            return Response( data, status = status.HTTP_400_BAD_REQUEST )
            
class ImageToOurPersonalContent( APIView ) :
    
    def get_object( self, pk ) :
        """Get object function """
        try :
            return OurPersonalContent.objects.get( pk=pk )
        except OurPersonalContent.DoesNotExist :
            raise Http404
    
    def put( self, request, pk, format=None ) :
        try :
            fh = open( "imageToSaveOurPersonalContent" + pk + ".png", "wb" )
            fh.write( request.data.decode( "base64" ) )
            fh.close()
            instance = self.get_object( pk )
            instance.img_url = save_image( "imageToSaveOurPersonalContent" + pk + ".png" )
            instance.save()
            serialized = OurPersonalContentSerializer( instance, many = None )
            data = { DATA : serialized.data }
            return Response( data, status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : "There was an error; error: {0}".format( str( e ) ) }
            return Response( data, status = status.HTTP_400_BAD_REQUEST )
            
class ContactFormCreateAPIView( generics.CreateAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin )
    
    def create( self, request, *args, **kwargs ) :
        """
        Create; post function
        decrypt data sended by the client
        format json and then decoded
        """
        try :
            the_data = json.dumps( self.decrypt_long_data( request.body ), ensure_ascii=False )
            json_formated = json.loads( the_data )
            json_decoded = json.loads( json_formated )
            send_contact_form( 
                json_decoded['name'], 
                json_decoded['email'], 
                json_decoded['subject'], 
                json_decoded['message'] )
            verification_contact_email(
                json_decoded['name'], 
                json_decoded['email'], 
                json_decoded['subject'], 
                json_decoded['message'] )
            data = { DATA : "Mensaje correctamente enviado." }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_201_CREATED )
        except Exception as e :
            data = { MESSAGE : "There was an error; error: {0}".format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )