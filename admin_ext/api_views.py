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
from custom_auth.permissions import IsApplication, IsSystemWorthy
from .models import Task
from .serializers import TaskSerializer
from helpers.error_handler import *
from datetime import datetime

import json

"""
This returns the created tasks by the user
System Worthy
"""
class TaskListCreateAPIView( generics.ListCreateAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsSystemWorthy, )
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    
    def list( self, request, *args, **kwargs ) :
        """ list function that returns a list of objects """
        try :
        
            tasks = Task.objects.filter( user = request.user.id )
            serializer = self.get_serializer( tasks, many = True )
            data = { DATA : serializer.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : "There was an error; error:{0}".format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )
            
    def create( self, request, *args, **kwargs ) :
        """ creates a task """
        try :
            the_data = json.dumps( self.decrypt_long_data( request.body ), ensure_ascii = False )
            json_formated = json.loads( the_data )
            json_decoded = json.loads( json_formated )
            
            instance = Task( 
                name = json_decoded['name'],
                description = json_decoded['description'],
                date_end = datetime.strptime( json_decoded['date_end'], "%Y/%m/%d %H:%M"),
                value = int( json_decoded['value'] ),
                user = request.user,
                user_assigned = User.objects.get( pk = int( json_decoded['user_assigned'] ) )
            )
            instance.save()
        
            serializer = self.get_serializer( instance, many = False )
            data = { DATA : serializer.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_201_CREATED )
        except Exception as e :
            data = { MESSAGE : ("There was an error creating the object; error{0}" ).format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )
            
"""
This returns the user tasks that were assigned to him
system worthy authorization
"""
class MyTasksListAPIView( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsSystemWorthy, )
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    
    def list( self, request, *args, **kwargs ) :
        """ list function that returns a list of objects """
        try :
            tasks = Task.objects.filter( user_assigned = request.user.id )
            serializer = self.get_serializer( tasks, many = True )
            data = { DATA : serializer.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : "There was an error; error:{0}".format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )

"""
This will return the tasks created by user not done by due time
"""
class ListNotDoneTasksAPIView( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsSystemWorthy, )
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    
    def list( self, request, *args, **kwargs ) :
        """ This will return a list of objects """
        try :
            tasks = Task().get_tasks_not_done_by_duedate( request.user )
            serialized = self.get_serializer( tasks, many=True )
            data = { DATA : serialized.data }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : "There was an error; error {0}".format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )
            
class TaskRetrieveUpdateDestroyAPIView( generics.RetrieveUpdateDestroyAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, IsSystemWorthy, )
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    
    def update( self, request, *args, **kwargs ) :
        """ update model with pk """
        try :
            the_data = json.dumps( self.decrypt_long_data( request.body ), ensure_ascii=False )
            json_formated = json.loads( the_data )
            json_decoded = json.loads( json_formated )
            
            instance = self.get_object()
            instance.name = json_decoded[ 'name' ]
            instance.description = json_decoded[ 'description' ]
            instance.value = int( json_decoded[ 'value' ] )
            instance.state = int( json_decoded[ 'state' ] )
            
            instance.save()
            
            data = { DATA : self.get_serializer( instance, many = False ).data }            
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : ( "There was an error; Error: {0}" ).format( str( e ) ) }
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