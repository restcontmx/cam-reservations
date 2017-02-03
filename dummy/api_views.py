# -*- coding: utf-8 -*-

# Imports
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404, JsonResponse
from django.contrib.auth.models import User
from django.core import serializers
# Rest framework imports
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# Import classes 
from helpers.encryption_system import SecuritySystem
from custom_auth.permissions import IsSystemWorthy, IsApplication

import json

""""
Simple back end connection
"""
class SimpleBEConnection( APIView ) :
    
    def post( self, request, format=None ) :
        """
        This is the post data from the simple back end connection 
        simple as not using basic authentication
        """
        data = {
            "message" : "This is a message from the Back end."
        }
        return Response( data )
    # End of post function
    
# End of simple back end connection 

"""
Basic authentication connection
"""
class BasicAuthenticationCon( APIView ) :

    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsApplication, )

    def post( self, request, format=None ) :
        """
        This is the post data from the authentication connection
        """
        data = {
            "message" : "This is a message from the back end with basic authentication"
        }
        return Response( data )
    # End of post function
    
# End of Basic Authentication connection view class

"""
Encyption test api view
"""
class EncryptionTestCon( APIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsApplication, )
    
    def post( self, request, format=None ) :
        """
        Post function 
        TODOs:
            get data and print it
            return a message
            decrypt data with private key
        """
        sended_data = request.body
        the_data = json.loads( self.decrypt_data( sended_data ) )
        data = {
            "message" : "This is a message fro the back end with encryption system and authentication"
        }
        return Response( self.encrypt_data( json.dumps( data ) ) )
    # End of post function 
    
# End of Enctyption test con class view