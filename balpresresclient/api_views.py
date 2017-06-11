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
# Import error handler 
from helpers.error_handler import *
from helpers.mail_helper import *
from reservations.models import ReservationCabin
from reservations.serializers import ReservationCabinSerializer

import json
import simplejson

class ReservationCabinByToken( APIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsAdmin )
    
    def get_object( self, pk ) :
        """Get object function """
        try :
            return ReservationCabin.objects.get( extended_token=pk )
        except ReservationCabin.DoesNotExist :
            raise Http404
            
    def get( self, request, pk, format=None ) :
        try :
            instance = self.get_object( pk )
            serialized = ReservationCabinSerializer( instance, many = None )
            data = { DATA : serialized.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : "There was an error; error: {0}".format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )