# -*- coding: utf-8 -*-
"""
Author - Ramiro Gutierrez Alaniz
Date - January, 9th 2017
"""

# Imports
from django.conf.urls import patterns, url
from .views import *
from dummy.api_views import *
from custom_auth.api_views import *
from products.api_views import *
from admin_ext.api_views import *
from reservations.api_views import *

# Url patterns
urlpatterns = patterns(
    
    'api.views',
    # every module urls from api urls
    url( r'^sbec/$', SimpleBEConnection.as_view(), name='dummy.sbec' ),  
    url( r'^baec/$', BasicAuthenticationCon.as_view(), name='dummy.baec' ),
    url( r'^esec/$', EncryptionTestCon.as_view(), name='dummy.esec' ),
    
    # Auth urls
    url( r'^login/$', LoginAdminPanelAPIView.as_view(), name='auth.login' ),
    url( r'^usercat/$', UserListAPIView.as_view(), name="users.get_permitted" ),
    
    # area type routes 
    url( r'^areatype/$', AreaTypeListAPIView.as_view(), name='areatype.list' ),
    url( r'^areatype/new/$', AreaTypeCreateAPIView.as_view(), name='areatype.create' ),
    url( r'^areatype/detail/(?P<pk>[0-9]+)$', AreaTypeDetailAPIView.as_view(), name='areatype.detail' ),
    # cabin type routes
    url( r'^cabintype/$', CabinTypeListAPIView.as_view(), name='cabintype.list' ),
    url( r'^cabintype/new/$', CabinTypeCreateAPIView.as_view(), name='cabintype.create' ),
    url( r'^cabintype/detail/(?P<pk>[0-9]+)$', CabinTypeDetailAPIView.as_view(), name='cabintype.detail' ),
    # pool routes
    url( r'^pool/$', PoolListAPIView.as_view(), name='pool.list' ),
    url( r'^pool/new/$', PoolCreateAPIView.as_view(), name='pool.create' ),
    url( r'^pool/detail/(?P<pk>[0-9]+)$', PoolDetailAPIView.as_view(), name='pool.detail' ),
    # area routes
    url( r'^area/$', AreaListAPIView.as_view(), name='area.list' ),
    url( r'^area/new/$', AreaCreateAPIView.as_view(), name='area.create' ),
    url( r'^area/detail/(?P<pk>[0-9]+)$', AreaDetailAPIView.as_view(), name='area.detail' ),
    # cabin routes 
    url( r'^cabin/$', CabinListAPIView.as_view(), name='cabin.list' ),
    url( r'^cabin/new/$', CabinCreateAPIView.as_view(), name='cabin.create' ),
    url( r'^cabin/detail/(?P<pk>[0-9]+)$', CabinDetailAPIView.as_view(), name='cabin.detail' ),
    url( r'^cabin/image/(?P<pk>[0-9]+)$', ImageToCabin.as_view(), name='cabin.image' ),
    
    # tasks routes
    url( r'^task/$', TaskListCreateAPIView.as_view(), name='task.listcreate' ),
    url( r'^task/assigned/$', MyTasksListAPIView.as_view(), name="task.assigned" ),
    
    # reservation type routes
    url( r'^reservationtype/$', ReservationTypeListAPIView.as_view(), name="reservationtype.list" ),
    url( r'^reservationtype/new/$', ReservationTypeCreateAPIView.as_view(), name="reservationtype.create" ),
    url( r'^reservationtype/detail/(?P<pk>[0-9]+)$', ReservationTypeRetrieveUpdateDestroyAPIView.as_view(), name="reservationtype.detail" ),

    # reservation info routes
    url( r'^reservationinfo/new/$', ReservationInfoCreateAPIView.as_view(), name="reservationinfo.create" ),
    url( r'^reservationinfo/detail/(?P<pk>[0-9]+)$', ReservationInfoRetrieveUpdateDestroyAPIView.as_view(), name="reservationinfo.detail" ),
    
    # reservation routes
    url( r'^reservation/$', ReservationListAdminAPIView.as_view(), name="reservation.listadmin" ),
    url( r'^reservation/new/$', ReservationListCreateAPIView.as_view(), name="reservation.listcreate" ),
    url( r'^reservation/detail/(?P<pk>[0-9]+)$', ReservationRetrieveUpdateDestroyAPIView.as_view(), name="reservation.detail" ),

    # Payment status routes
    url( r'^paymentstatus/$', PaymentStatusListAPIView.as_view(), name="paymentstatus.list" ),
    url( r'^paymentstatus/new/$', PaymentStatusCreateAPIView.as_view(), name="paymentstatus.create" ),
    url( r'^paymentstatus/detail/(?P<pk>[0-9]+)$', PaymentStatusRetrieveUpdateDestroyAPIView.as_view(), name="paymentstatus.detail" ),

    # promotion routes
    url( r'^promotion/$', PromotionListAPIView.as_view(), name="promotion.list" ),
    url( r'^promotion/new/$', PromotionCreateAPIView.as_view(), name="promotion.create" ),
    url( r'^promotion/detail/(?P<pk>[0-9]+)$', PromotionRetrieveUpdateDestroyAPIView.as_view(), name="promotion.detail" ),

    # payment routes

)