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
from reservations.models import *
from reservations.serializers import * 
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

class ReportsByMonthList( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = (  IsAuthenticated, IsSystemWorthy, )
    serializer_class = ReservationCabinSerializer
    queryset = ReservationCabin.objects.all()
    
    def list( self, request, *args, **kwargs ) :
        try :
            data = { DATA : ReservationCabin().get_reports_with_month( datetime.strptime( request.GET['date'], '%Y-%m-%d' ).date() ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e : 
            data = { MESSAGE : ( "There was an error; Error: {0}" ).format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )
            
class ReportsByYearList( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = (  IsAuthenticated, IsAdmin, )
    serializer_class = ReservationCabinSerializer
    queryset = ReservationCabin.objects.all()
    
    def list( self, request, *args, **kwargs ) :
        try :
            data = { DATA : ReservationCabin().get_reports_with_year( request.GET['year'] ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : ( "There was an error; Error: {0}" ).format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )
            
class PayedReportsByMonthList( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = (  IsAuthenticated, IsSystemWorthy, )
    serializer_class = ReservationCabinSerializer
    queryset = ReservationCabin.objects.all()
    
    def list( self, request, *args, **kwargs ) :
        try :
            data = { DATA : ReservationCabin().get_payed_reports_with_month( datetime.strptime( request.GET['date'], '%Y-%m-%d' ).date() ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : ( "There was an error; Error: {0}" ).format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )

class PendingReportsByMonthList( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = (  IsAuthenticated, IsSystemWorthy, )
    serializer_class = ReservationCabinSerializer
    queryset = ReservationCabin.objects.all()
    
    def list( self, request, *args, **kwargs ) :
        try :
            data = { DATA : ReservationCabin().get_pending_reports_with_month( datetime.strptime( request.GET['date'], '%Y-%m-%d' ).date() ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : ( "There was an error; Error: {0}" ).format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )
            
class PayedReportsByYearList( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = (  IsAuthenticated, IsAdmin, )
    serializer_class = ReservationCabinSerializer
    queryset = ReservationCabin.objects.all()
    
    def list( self, request, *args, **kwargs ) :
        try :
            data = { DATA : ReservationCabin().get_payed_reports_with_year( request.GET['year'] ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : ( "There was an error; Error: {0}" ).format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )

class PayedReportsByDatesList( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = (  IsAuthenticated, IsSystemWorthy, )
    
    def list( self, request, *args, **kwargs ) :
        try :
            data = { DATA : ReservationCabin().get_payed_reports_with_dates( datetime.strptime(  request.GET['d1'], '%Y-%m-%d' ).date(), datetime.strptime(  request.GET['d2'], '%Y-%m-%d' ).date() ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : ( "There was an error; Error: {0}" ).format( str( e ) ) }
            print data
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )

class PendingReportsByDatesList( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = (  IsAuthenticated, IsSystemWorthy, )
    
    def list( self, request, *args, **kwargs ) :
        try :
            data = { DATA : ReservationCabin().get_pending_reports_with_dates( datetime.strptime(  request.GET['d1'], '%Y-%m-%d' ).date(), datetime.strptime(  request.GET['d2'], '%Y-%m-%d' ).date() ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : ( "There was an error; Error : {0}" ).format( str( e ) ) }
            print data
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )
            
class ReportsByDatesList( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = (  IsAuthenticated, IsSystemWorthy, )
    
    def list( self, request, *args, **kwargs ) :
        try :
            data = { DATA : ReservationCabin().get_reports_with_dates( datetime.strptime( request.GET['d1'], '%Y-%m-%d' ), datetime.strptime( request.GET['d2'], '%Y-%m-%d' ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : ( "There was an error; Error {0}" ).format( str( e ) ) }
            print data
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )
            
class CabinReportsByMonthList( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = (  IsAuthenticated, IsSystemWorthy, )
    
    def list( self, request, *args, **kwargs ) :
        try :
            data = { DATA : ReservationCabin().get_cabin_reports_by_month( datetime.strptime( request.GET['date'], '%Y-%m-%d' ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : ( "There was an error; Error {0}" ).format( str( e ) ) }
            print data
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )

class CabinReportsByYearList( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = (  IsAuthenticated, IsAdmin, )
    
    def list( self, request, *args, **kwargs ) :
        try :
            data = { DATA : ReservationCabin().get_cabin_reports_by_year( request.GET['year'] ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : ( "There was an error; Error: {0}" ).format( str( e ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )

class CabinReportsByDatesList( generics.ListAPIView, SecuritySystem ) :
    
    authentication_classes = ( BasicAuthentication, )
    permission_classes = (  IsAuthenticated, IsAdmin, )
    
    def list( self, request, *args, **kwargs ) :
        try :
            data = { DATA : ReservationCabin().get_cabin_reports_by_dates( datetime.strptime( request.GET['d1'], '%Y-%m-%d' ), datetime.strptime( request.GET['d2'], '%Y-%m-%d' ) ) }
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_200_OK )
        except Exception as e :
            data = { MESSAGE : ( "There was an error; Error {0}" ).format( str( e ) ) }
            print data
            return Response( self.encrypt_long_data( json.dumps( data ) ), status = status.HTTP_400_BAD_REQUEST )