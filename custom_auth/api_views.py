# -*- coding: utf-8 -*-
"""
custom_auth.api_views
Author - Ramiro Gutierrez Alaniz
Date - January, 9th 2017
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
from custom_auth.permissions import IsApplication, IsSystemWorthy, IsAdmin
from .models import CustomSystemUser, Rol
from .serializers import UserCatSerializer, CustomSystemUserSerializer

# Import error handler 
from helpers.error_handler import *

import json

"""
Log in api view
"""
class LoginAdminPanelAPIView( APIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsApplication, )
    
    def post( self, request, format=None ) :
        """
        Post function
        validate user and password
        validate rol as super admin, admin and general [1, 2, 3]
        """
        real_data = self.decrypt_data( request.body ) 
        the_data = json.loads( real_data )
        user_from_db = authenticate( username = the_data[ 'username' ], password = the_data[ 'password' ] )
        data = { MESSAGE : EMPTY, DATA : EMPTY }
        if user_from_db is not None :
        
            user_system = CustomSystemUser.objects.get( user = user_from_db.id )
            data[ MESSAGE ] = VALID_CREDENTIALS if user_system.name.value < APP_ROL else NO_PERMISSION
            stat = status.HTTP_200_OK if user_system.name.value < APP_ROL else status.HTTP_401_UNAUTHORIZED
            data[ DATA ] = { "name" : user_system.name.name, "value" : user_system.name.value }
            return Response( self.encrypt_data( json.dumps( data ) ), status=stat )
        
        else :
        
            data[ MESSAGE ] = INVALID_CREDENTIALS
            return Response( self.encrypt_data( json.dumps( data ) ), status = status.HTTP_401_UNAUTHORIZED )
            
"""
Get users according of their permission
"""
class UserListAPIView( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = (  IsAuthenticated, IsAdmin, )
    serializer_class = CustomSystemUserSerializer
    
    def list( self, request, format = None ) :
        """
        list all the users according of the permission
        """
        try : 
            instance = CustomSystemUser.objects.exclude( name = 5 ).exclude( name = 4 )
            serializer = self.get_serializer( instance, many = True )
            data = { DATA : serializer.data } 
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : "There was an error; error {0}.".format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )