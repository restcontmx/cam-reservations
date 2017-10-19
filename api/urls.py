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
from website.api_views import *
from general.api_views import *
from balpresresclient.api_views import *
from reports.api_views import *

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
    url( r'^task/(?P<pk>[0-9]+)$', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task.detail' ),
    url( r'^task/assigned/$', MyTasksListAPIView.as_view(), name="task.assigned" ),
    url( r'^task/notdonebydue/$', ListNotDoneTasksAPIView.as_view(), name="task.notdonebydue" ),
    
    # reservation type routes
    url( r'^reservationtype/$', ReservationTypeListAPIView.as_view(), name="reservationtype.list" ),
    url( r'^reservationtype/new/$', ReservationTypeCreateAPIView.as_view(), name="reservationtype.create" ),
    url( r'^reservationtype/detail/(?P<pk>[0-9]+)$', ReservationTypeRetrieveUpdateDestroyAPIView.as_view(), name="reservationtype.detail" ),

    # reservation info routes
    url( r'^reservationinfo/new/$', ReservationInfoCreateAPIView.as_view(), name="reservationinfo.create" ),
    url( r'^reservationinfo/detail/(?P<pk>[0-9]+)$', ReservationInfoRetrieveUpdateDestroyAPIView.as_view(), name="reservationinfo.detail" ),
    
    # reservation routes
    url( r'^reservation/$', ReservationListAdminAPIView.as_view(), name="reservation.listadmin" ),
    url( r'^reservation/cabin/new/$', ReservationCabinListCreateAPIView.as_view(), name="reservationcabin.listcreate" ),
    url( r'^reservation/cabins/$', ProductCabinListFromDatesAPIView.as_view(), name="reservation.cabins" ),
    url( r'^reservation/cabin/paymentstatus/(?P<pk>[0-9]+)$', ReservationCabinUpdatePaymentStatusAPIView.as_view(), name="reservation.cabins.paymentstatus" ),
    
    url( r'^notifications$', NotificationsAPIView.as_view(), name="notifications" ),

    # Payment status routes
    url( r'^paymentstatus/$', PaymentStatusListAPIView.as_view(), name="paymentstatus.list" ),
    url( r'^paymentstatus/new/$', PaymentStatusCreateAPIView.as_view(), name="paymentstatus.create" ),
    url( r'^paymentstatus/detail/(?P<pk>[0-9]+)$', PaymentStatusRetrieveUpdateDestroyAPIView.as_view(), name="paymentstatus.detail" ),

    # promotion routes
    url( r'^promotion/$', PromotionListAPIView.as_view(), name="promotion.list" ),
    url( r'^promotion/new/$', PromotionCreateAPIView.as_view(), name="promotion.create" ),
    url( r'^promotion/detail/(?P<pk>[0-9]+)$', PromotionRetrieveUpdateDestroyAPIView.as_view(), name="promotion.detail" ),

    # general routes
    url( r'^settings/alertnumbers/$', AlertNumbersSettingsListAPIView.as_view(), name="general.alertnumbers.list" ),
    url( r'^settings/alertemails/$', AlertEmailsSettingsListAPIView.as_view(), name="general.alertemails.list" ),
    url( r'^settings/contactemail/$', ContactEmailSettingsListAPIView.as_view(), name="general.contactemail.list" ),
    url( r'^settings/ticketprices/$', TicketPricesSettingsListAPIView.as_view(), name="general.ticketprices.list" ),
    url( r'^settings/signatures/$', SignaturesSettingsListAPIView.as_view(), name="general.signatures.list" ),
    
    url( r'^settings/alertnumbers/edit/$', AlertNumbersSettingsUpdateAPIView.as_view(), name="general.alertnumbers.edit" ),
    url( r'^settings/alertemails/edit/$', AlertEmailsSettingsUpdateAPIView.as_view(), name="general.alertemails.edit" ),
    url( r'^settings/contactemail/edit/$', ContactEmailSettingsUpdateAPIView.as_view(), name="general.contactemail.edit" ),
    url( r'^settings/ticketprices/edit/$', TicketPricesSettingsUpdateAPIView.as_view(), name="general.ticketprices.edit" ),
    
    # website contents 
    url( r'^website/ourcompanycontent/$', OurCompanyContentListAPIView.as_view(), name="website.ourcompanycontent.list" ),
    url( r'^website/ourservicescontent/$', OurServicesContentListAPIView.as_view(), name="website.ourservicescontent.list" ),
    url( r'^website/recomendations/$', RecomendationsListAPIView.as_view(), name="website.recomendations.list" ),
    url( r'^website/ourpersonalcontent/$', OurPersonalContentListAPIView.as_view(), name="website.ourpersonalcontent.list" ),
    url( r'^website/ourproductscontent/$', OurProductsContentListAPIView.as_view(), name="website.ourproductscontent.list" ),
    
    url( r'^website/ourcompanycontent/edit/$', OurCompanyContentUpdateAPIView.as_view(), name="website.ourcompanycontent.edit" ),
    url( r'^website/ourservicescontent/edit/$', OurServicesContentUpdateAPIView.as_view(), name="website.ourservicescontent.edit" ),
    url( r'^website/recomendations/edit/$', RecomendationsUpdateAPIView.as_view(), name="website.recomendations.edit" ),
    url( r'^website/ourpersonalcontent/edit/$', OurPersonalContentUpdateAPIView.as_view(), name="website.ourpersonalcontent.edit" ),
    url( r'^website/ourproductscontent/edit/$', OurProductsContentUpdateAPIView.as_view(), name="website.ourproductscontent.edit" ),
    url( r'^website/contactform/$', ContactFormCreateAPIView.as_view(), name="website.contactform.create" ),
    
    url( r'^website/ourcompanycontent/image1/(?P<pk>[0-9]+)$', Image1ToOurCompanyContent.as_view(), name="website.ourcompanycontent.image1" ),
    url( r'^website/ourcompanycontent/image2/(?P<pk>[0-9]+)$', Image2ToOurCompanyContent.as_view(), name="website.ourcompanycontent.image2" ),
    url( r'^website/ourpersonalcontent/image/(?P<pk>[0-9]+)$', ImageToOurPersonalContent.as_view(), name="website.ourpersonalcontent.image" ),
    
    url( r'^balpresresclient/reservationcabin/(?P<pk>[\w{}.-]{1,40})$', ReservationCabinByToken.as_view(), name="balpresresclient.reservationcabin.detail" ),
    
    #reports
    url( r'^reports/bymonth/$', ReportsByMonthList.as_view(), name="reports.bymonth" ),
    url( r'^reports/byyear/$', ReportsByYearList.as_view(), name="reports.byyear" ),
    url( r'^reports/bydates/$', ReportsByDatesList.as_view(), name="reports.bydates" ),
    url( r'^reports/payedbymonth/$', PayedReportsByMonthList.as_view(), name="reports.payedbymonth" ),
    url( r'^reports/pendingbymonth/$', PendingReportsByMonthList.as_view(), name="reports.pendingbymonth" ),
    url( r'^reports/payedbydates/$', PayedReportsByDatesList.as_view(), name="reports.payedbydates" ),
    url( r'^reports/pendingbydates/$', PendingReportsByDatesList.as_view(), name="reports.pendingbydates" ),
    url( r'^reports/payedbyyear/$', PayedReportsByYearList.as_view(), name="reports.payedbyyear" ),
    
    url( r'^reports/cabinsbymonth/$', CabinReportsByMonthList.as_view(), name="reports.cabinsbymonth" ),
    url( r'^reports/cabinsbyyear/$', CabinReportsByYearList.as_view(), name="reports.cabinsbyyear" ),
    
)