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
from .models import AreaType, CabinType, Cabin, Pool, Area
from .serializers import AreaTypeSerializer, CabinTypeSerializer, CabinSerializer, PoolSerializer, AreaSerializer
# Import error handler 
from helpers.error_handler import *
from helpers.imgur import *
import json
import simplejson
# Image decode shit
from PIL import Image
from base64 import *
import datetime

"""
Area type list api view
returns all the area types if you are both admins.all
"""
class AreaTypeListAPIView( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin )
    queryset = AreaType.objects.all()
    serializer_class = AreaTypeSerializer
    
    def list( self, request, *args, **kwargs ) :
        """
        list function that responds to a get
        return the data on a encapsulated data variable as json
        """
        instance = self.get_queryset()
        serializer = self.get_serializer( instance, many=True )
        data = { DATA : serializer.data }
        response_list = self.encrypt_long_data( json.dumps( data ) )
        return Response( response_list, status = status.HTTP_200_OK )

"""
Area type create api view
creates an object then retrieves it
just for super admin
"""
class AreaTypeCreateAPIView( generics.CreateAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsSuperAdmin )
    queryset = AreaType.objects.all()
    serializer_class = AreaTypeSerializer
    
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
            
            instance = AreaType( 
                name = json_decoded[ 'name' ], 
                description = json_decoded[ 'description' ], 
                max_guests = json_decoded[ 'max_guests' ], 
                user = request.user )
            instance.save()
            
            serializer = self.get_serializer( instance, many = False )
            data = { DATA : serializer.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_201_CREATED )
        except Exception as e :
            data = { MESSAGE : "There was an error; error: {0}".format( str( e ) ) }
            return Response( self.encrypt_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )
            

"""
Area type detail api view
updates the object and retrieves its detail
just for super admin
"""
class AreaTypeDetailAPIView( generics.RetrieveUpdateDestroyAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    perission_classes =( IsAuthenticated, IsSuperAdmin, )
    queryset = AreaType.objects.all()
    serializer_class = AreaTypeSerializer
    
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
            instance.max_guests = json_decoded['max_guests']
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
            

"""
Cabin type list api view
returns all the area types if you are both admins.all
"""
class CabinTypeListAPIView( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin )
    queryset = CabinType.objects.all()
    serializer_class = CabinTypeSerializer
    
    def list( self, request, *args, **kwargs ) :
        """
        list function that responds to a get
        return the data on a encapsulated data variable as json
        """
        instance = self.get_queryset()
        serializer = self.get_serializer( instance, many=True )
        data = { DATA : serializer.data }
        response_list = self.encrypt_long_data( json.dumps( data ) )
        return Response( response_list, status = status.HTTP_200_OK )
        

"""
Cabin type create api view
creates an object then retrieves it
just for super admin
"""
class CabinTypeCreateAPIView( generics.CreateAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsSuperAdmin )
    queryset = CabinType.objects.all()
    serializer_class = CabinTypeSerializer
    
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
            
            instance = CabinType( 
                name = json_decoded[ 'name' ], 
                description = json_decoded[ 'description' ], 
                rooms = json_decoded[ 'rooms' ], 
                max_guests = json_decoded[ 'max_guests' ], 
                max_extra_guests = json_decoded[ 'max_extra_guests' ], 
                user = request.user )
            instance.save()
            
            serializer = self.get_serializer( instance, many = False )
            data = { DATA : serializer.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_201_CREATED )
        except Exception as e :
            data = { MESSAGE : "There was an error; error: {0}".format( str( e ) ) }
            return Response( self.encrypt_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )
            
"""
Cabin type detail api view
updates the object and retrieves its detail
just for super admin
"""
class CabinTypeDetailAPIView( generics.RetrieveUpdateDestroyAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    perission_classes =( IsAuthenticated, IsSuperAdmin, )
    queryset = CabinType.objects.all()
    serializer_class = CabinTypeSerializer
    
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
            instance.rooms = json_decoded['rooms']
            instance.max_guests = json_decoded['max_guests']
            instance.max_extra_guests = json_decoded['max_extra_guests']
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
            
"""
Pool list api view
returns all the area types if you are both admins.all
"""
class PoolListAPIView( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin )
    queryset = Pool.objects.all()
    serializer_class = PoolSerializer
    
    def list( self, request, *args, **kwargs ) :
        """
        list function that responds to a get
        return the data on a encapsulated data variable as json
        """
        instance = self.get_queryset()
        serializer = self.get_serializer( instance, many=True )
        data = { DATA : serializer.data }
        response_list = self.encrypt_long_data( json.dumps( data ) )
        return Response( response_list, status = status.HTTP_200_OK )

"""
Pool create api view
creates an object then retrieves it
just for super admin
"""
class PoolCreateAPIView( generics.CreateAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin )
    queryset = Pool.objects.all()
    serializer_class = PoolSerializer
    
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
            
            instance = Pool( 
                name = json_decoded[ 'name' ], 
                description = json_decoded[ 'description' ], 
                max_people = int( json_decoded[ 'max_people' ] ), 
                price = float( json_decoded[ 'price' ] ), 
                user = request.user )
            instance.save()
            
            serializer = self.get_serializer( instance, many = False )
            data = { DATA : serializer.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_201_CREATED )
        except Exception as e :
            data = { MESSAGE : "There was an error; error: {0}".format( str( e ) ) }
            return Response( self.encrypt_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )
            
"""
Pool detail api view
updates the object and retrieves its detail
just for super admin
"""
class PoolDetailAPIView( generics.RetrieveUpdateDestroyAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    perission_classes =( IsAuthenticated, IsSuperAdmin, )
    queryset = Pool.objects.all()
    serializer_class = PoolSerializer
    
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
            instance.max_people = int( json_decoded['max_people'] )
            instance.price = float( json_decoded['price'] )
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
    
"""
Cabin list api view
returns all the area types if you are both admins.all
"""
class CabinListAPIView( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin )
    queryset = Cabin.objects.all()
    serializer_class = CabinSerializer
    
    def list( self, request, *args, **kwargs ) :
        """
        list function that responds to a get
        return the data on a encapsulated data variable as json
        """
        instance = self.get_queryset()
        serializer = self.get_serializer( instance, many=True )
        data = { DATA : serializer.data }
        response_list = self.encrypt_long_data( json.dumps( data ) )
        return Response( response_list, status = status.HTTP_200_OK )

"""
Cabin create api view
creates an object then retrieves it
just for super admin
"""
class CabinCreateAPIView( generics.CreateAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin )
    queryset = Cabin.objects.all()
    serializer_class = CabinSerializer
    
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
            
            instance = Cabin( 
                name = json_decoded[ 'name' ], 
                cabin_type = CabinType.objects.get( pk = int( json_decoded[ 'cabin_type' ] ) ), 
                description = json_decoded[ 'description' ], 
                price = float( json_decoded[ 'price' ] ), 
                user = request.user )
            instance.save()
            
            serializer = self.get_serializer( instance, many = False )
            data = { DATA : serializer.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_201_CREATED )
        except Exception as e :
            data = { MESSAGE : "There was an error; error: {0}".format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )

"""
Cabin detail api view
updates the object and retrieves its detail
just for super admin
"""
class CabinDetailAPIView( generics.RetrieveUpdateDestroyAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    perission_classes =( IsAuthenticated, IsSuperAdmin, )
    queryset = Cabin.objects.all()
    serializer_class = CabinSerializer
    
    def retrieve( self, request, *args, **kwargs ) :
        """ retrieve object with id """
        try :
            instance = self.get_object()
            serializer = self.get_serializer( instance, many = False )
            data = { DATA : serializer.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : "There was an error; error: {0}".format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )
            
    
    def update( self, request, *args, **kwargs ) :
        """ update object with id """
        try :
            the_data = json.dumps( self.decrypt_long_data( request.body ), ensure_ascii=False )
            json_formated = json.loads( the_data )
            json_decoded = json.loads( json_formated )
            
            instance = self.get_object()
            instance.name = json_decoded['name']
            instance.description = json_decoded['description']
            instance.cabin_type = CabinType.objects.get( pk = int( json_decoded[ 'cabin_type' ] ) )
            instance.price = float( json_decoded['price'] )
            instance.save()

            serializer = self.get_serializer( instance, many = False )
            data = { DATA : serializer.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : "There was an error; error: {0}".format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )

    
    def destroy( self, request, *args, **kwargs ) :
        """ delete object with id """
        try : 
            instance = self.get_object()
            instance.delete()
            data = { MESSAGE : "Objecto borrado." }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_204_NO_CONTENT )
        except Exception as e :
            data = { MESSAGE : "There was an error; error: {0}".format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )
            
"""
Area list api view
returns all the area types if you are both admins.all
"""
class AreaListAPIView( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin )
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    
    def list( self, request, *args, **kwargs ) :
        """
        list function that responds to a get
        return the data on a encapsulated data variable as json
        """
        instance = self.get_queryset()
        serializer = self.get_serializer( instance, many=True )
        data = { DATA : serializer.data }
        response_list = self.encrypt_long_data( json.dumps( data ) )
        return Response( response_list, status = status.HTTP_200_OK )

"""
Area create api view
creates an object then retrieves it
just for super admin
"""
class AreaCreateAPIView( generics.CreateAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin )
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    
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
            
            instance = Area( 
                name = json_decoded[ 'name' ], 
                description = json_decoded[ 'description' ], 
                price = float( json_decoded[ 'price' ] ),
                area_type = AreaType.objects.get( pk = int( json_decoded[ 'area_type' ] ) ), 
                user = request.user )
                
            instance.save()
            
            for p in json_decoded['pools'] :
                instance.pools.add( Pool.objects.get( pk = int( p ) ) )
            
            serializer = self.get_serializer( instance, many = False )
            data = { DATA : serializer.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_201_CREATED )
        except Exception as e :
            data = { MESSAGE : "There was an error; error: {0}".format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )

"""
Area detail api view
updates the object and retrieves its detail
just for super admin
"""
class AreaDetailAPIView( generics.RetrieveUpdateDestroyAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    perission_classes =( IsAuthenticated, IsSuperAdmin, )
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    
    def retrieve( self, request, *args, **kwargs ) :
        """ retrieve object with id """
        try :
            instance = self.get_object()
            serializer = self.get_serializer( instance, many = False )
            data = { DATA : serializer.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : "There was an error; error: {0}".format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )
            
    
    def update( self, request, *args, **kwargs ) :
        """ update object with id """
        try :
            the_data = json.dumps( self.decrypt_long_data( request.body ), ensure_ascii=False )
            json_formated = json.loads( the_data )
            json_decoded = json.loads( json_formated )
            
            instance = self.get_object()
            
            instance.name = json_decoded['name']
            instance.description = json_decoded['description']
            instance.price = float( json_decoded['price'] )
            instance.area_type = AreaType.objects.get( pk = int( json_decoded['area_type'] ) )
            
            instance.save()
            
            instance.pools.clear()
            for p in json_decoded['pools'] :
                instance.pools.add( Pool.objects.get( pk = int( p ) ) )

            serializer = self.get_serializer( instance, many = False )
            data = { DATA : serializer.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : "There was an error; error: {0}".format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )

    
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
            
"""
Image to Cabin
Image to set cabins image
"""
class ImageToCabin( APIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin, )
    queryset = Cabin.objects.all()
    serializer_class = CabinSerializer
    
    def put( self, request, format=None ) :
        """
        put function
        will get the cabin by id and then is going to add the 
        image to the image server to then add the link on the 
        cabin model
        """
        try :
            the_data = json.dumps( self.decrypt_long_data( request.body ), ensure_ascii=False )
            json_formated = json.loads( the_data )
            json_decoded = json.loads( json_formated )
            print( the_data )
            instance = self.get_object()
            print( instance )
            serialized = self.get_serializer( instance, many = None )
            data = { DATA : serialized.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : "There was an error; error: {0}".format( str( e ) ) }
            return Response( self.encrypt_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )