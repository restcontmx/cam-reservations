# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from products.models import Cabin, Pool, Area
from products.serializers import CabinSerializer
import datetime, uuid, json , calendar
from datetime import timedelta

class Detail( models.Model ) :
    """
    Detail 
    this is parent detail
    """
    user = models.ForeignKey( User )
    qty = models.IntegerField( default = 0, blank = True )
    
class DetailCabin( Detail ) :
    """
    Detail Cabin
    Detail product for cabin model
    """
    product = models.ForeignKey( Cabin )
    
    def __str__( self ) :
        return ( "Cabin : {0}; Qty : {1}" ).format( self.product.name, self.qty )

class DetailArea( Detail ) :
    """
    Detail area
    Detail product for area model
    """
    product = models.ForeignKey( Area )
    
    def __str__( self ) :
        return ( "Area : {0}; Qty : {1}" ).format( self.product.name, self.qty )
    
class DetailPool( Detail ) :
    """
    Detail Pool
    Detail product for pool model
    """
    product = models.ForeignKey( Pool )
    
    def __str__( self ) :
        return ( "Pool : {0}; Qty : {1}" ).format( self.product.name, self.qty )
        
class ReservationType( models.Model ) :
    """
    Reservation Type
    Will return the reservation type
    ex : Cabin, Area, Pool
    """
    user = models.ForeignKey( User )
    name = models.CharField( max_length = 100, default = "", blank = False )
    description = models.CharField( max_length = 200, default = "", blank = True )
    value = models.IntegerField( default = 0, blank = True )
    
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )
    
    def __str__( self ) :
        return self.name
    
class ReservationInfo( models.Model ) :
    """
    Reservation Information 
    This will contain the client information for reservation
    """
    user = models.ForeignKey( User )
    
    full_name = models.CharField( max_length = 500, blank = False )
    address1 = models.CharField( max_length = 500, blank = True, null=True )
    address2 = models.CharField( max_length = 500, blank = True, null=True )
    zip_code = models.IntegerField( default = 0, blank = True, null=True )
    city = models.CharField( max_length = 100, blank = True )
    state = models.CharField( max_length = 100, blank = True )
    country = models.CharField( max_length = 100, blank = True )
    
    email = models.EmailField( max_length = 500, blank=False, unique = False, default='' )
    
    phone_regex = RegexValidator( regex=r'^\+?1?\d{9,15}$', message="Número de teléfono incorrecto." )
    phone_number = models.CharField( max_length = 200, validators=[phone_regex], blank=False, default='' )
    
    def __str__( self ) :
        return ( "{0}" ).format( self.full_name )
 
class PaymentStatus( models.Model ) :
    
    user = models.ForeignKey( User )
    name = models.CharField( max_length = 100, default = "", blank = False )
    description = models.CharField( max_length = 500, default = "", blank = True )
    value = models.IntegerField( default = 0, unique=True )
    
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )
    
    def __str__( self ) :
        return ( "{0}" ).format( self.id )
        
class Payment( models.Model ) :
    """
    Payment model
    Right now it only contains mercadopago api information
    """
    preference_mp_id = models.CharField( max_length=100, blank=True, null=True, default="" )
    preference_mp_init_point = models.CharField( max_length=256, blank=True, null=True, default="" )
    payment_status = models.ForeignKey( PaymentStatus, default=1, null=True )
    collection_id = models.BigIntegerField( default=0, null=True, blank=True )
    
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )
    
    def __str__( self ) :
        return str( self.preference_mp_id )
    
class ReservationCabin( models.Model ) :
    """
    Reservation Cabin
    This is a reservation for the cabin details
    """
    user = models.ForeignKey( User, related_name="user_creator_rescab" )
    user_client = models.ForeignKey( User, related_name="client_user_rescab", blank = True, null = True )
    reservation_info = models.ForeignKey( ReservationInfo, null = True )
    details = models.ManyToManyField( DetailCabin )
    max_guests = models.IntegerField( default = 0, null=True )
    extra_guests_child = models.IntegerField( default = 0 )
    extra_guests_adult = models.IntegerField( default = 0 )
    total = models.DecimalField( max_digits = 9, decimal_places = 2, default = 0.00, blank = False )
    extended_token = models.CharField( max_length=100, blank=True, unique=True, default=uuid.uuid4 )

    date_start = models.DateTimeField( blank = True, null = True )
    date_end = models.DateTimeField( blank = True, null = True )
    
    payment_status = models.ForeignKey( PaymentStatus, default=1, null=True )
    payment_info = models.ForeignKey( Payment, null=True, blank=True )
    
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )
    
    def __str__( self ) :
        return ( "This is reservation {0}" ).format( self.id )
        
    def get_cabins_availables( self, start_date, end_date ) :
        """
        Get cabins available
        This gets the cabins available for the dates desired by the reservation
        """
        reservations = ReservationCabin.objects.filter( models.Q( date_start__range=( start_date, end_date ) ) | models.Q( date_end__range=( start_date, end_date ) ) )
        cabins = Cabin.objects.all()
        for r in reservations :
            if r.date_end.date() != start_date and r.date_start.date() != end_date :
                for d in r.details.all() :
                    cabins = cabins.exclude( pk = d.product.id )
        return cabins

    def get_cabins_for_calendar( self, start_date, end_date ) :
        """
        Get cabins for calendar
        Gets the reservations between two dates
        """
        return ReservationCabin.objects.filter( models.Q( date_start__range=( start_date, end_date ) ) | models.Q( date_end__range=( start_date, end_date ) ) )
    
    def get_reports_with_month( self, date ) :
        
        month = date.month
        year = date.year
        s_d = datetime.datetime.strptime( "{0}/{1}/{2}".format( year, month, 1 ), "%Y/%m/%d").date()
        reservations = ReservationCabin.objects.filter( date_start__year = year, date_start__month = month )
        
        reports = []
        
        while s_d.month == month :
            temp_rs = reservations.filter( date_start__day = s_d.day )
            temp_tot = temp_rs.aggregate( models.Sum( 'total' ) )
            reports.append( { 'day' : s_d.day, 'qty' : temp_rs.count(), 'total' : float( 0 if temp_tot['total__sum'] == None else str( temp_tot['total__sum'] ) ) } )
            s_d += timedelta( days = 1 )
        
        return reports
        
    def get_reports_with_year( self, year ) :
        
        month = [ 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Semptiembre', 'Octubre', 'Noviembre', 'Diciembre' ]
        s_d = datetime.datetime.strptime( "{0}/{1}/{2}".format( year, 1, 1 ), "%Y/%m/%d").date()
        reservations = ReservationCabin.objects.filter( date_start__year = year )
        reports = []
        while int(s_d.year) == int(year) :
            temp_rs = reservations.filter( date_start__month = s_d.month )
            temp_tot = temp_rs.aggregate( models.Sum( 'total' ) )
            reports.append( { 'month' : month[s_d.month-1], 'qty' : temp_rs.count(), 'total' : float( 0 if temp_tot['total__sum'] == None else str( temp_tot['total__sum'] ) ) } )
            s_d += timedelta( days = 31 )
        
        return reports
    
    def get_payed_reservations( self ) :
        return ReservationCabin.objects.filter( models.Q(payment_info__payment_status = PaymentStatus.objects.get( value=2 ).pk) )
    
    def get_pending_reservations( self ) :
        return ReservationCabin.objects.filter( models.Q(payment_info__payment_status = PaymentStatus.objects.get( value=1 ).pk ) )
        
    def get_pending_reports_with_month( self, date ) :
        
        month = date.month
        year = date.year
        s_d = datetime.datetime.strptime( "{0}/{1}/{2}".format( year, month, 1 ), "%Y/%m/%d").date()
        reservations = self.get_pending_reservations().filter( date_start__year = year, date_start__month = month )
        
        reports = []
        
        while s_d.month == month :
            temp_rs = reservations.filter( date_start__day = s_d.day )
            temp_tot = temp_rs.aggregate( models.Sum( 'total' ) )
            reports.append( { 'day' : s_d.day, 'qty' : temp_rs.count(), 'total' : float( 0 if temp_tot['total__sum'] == None else str( temp_tot['total__sum'] ) ) } )
            s_d += timedelta( days = 1 )
        
        return reports
    
    def get_payed_reports_with_month( self, date ) :
        
        month = date.month
        year = date.year
        s_d = datetime.datetime.strptime( "{0}/{1}/{2}".format( year, month, 1 ), "%Y/%m/%d").date()
        reservations = self.get_payed_reservations().filter( date_start__year = year, date_start__month = month )
        
        reports = []
        
        while s_d.month == month :
            temp_rs = reservations.filter( date_start__day = s_d.day )
            temp_tot = temp_rs.aggregate( models.Sum( 'total' ) )
            reports.append( { 'day' : s_d.day, 'qty' : temp_rs.count(), 'total' : float( 0 if temp_tot['total__sum'] == None else str( temp_tot['total__sum'] ) ) } )
            s_d += timedelta( days = 1 )
        
        return reports
    
    def get_payed_reports_with_year( self, year ) :
        
        month = [ 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Semptiembre', 'Octubre', 'Noviembre', 'Diciembre' ]
        s_d = datetime.datetime.strptime( "{0}/{1}/{2}".format( year, 1, 1 ), "%Y/%m/%d").date()
        reservations = self.get_payed_reservations().filter( date_start__year = year )
        reports = []
        while int(s_d.year) == int(year) :
            temp_rs = reservations.filter( date_start__month = s_d.month )
            temp_tot = temp_rs.aggregate( models.Sum( 'total' ) )
            reports.append( { 'month' : month[s_d.month-1], 'qty' : temp_rs.count(), 'total' : float( 0 if temp_tot['total__sum'] == None else str( temp_tot['total__sum'] ) ) } )
            s_d += timedelta( days = 31 )
        
        return reports
        
    def get_payed_reports_with_dates( self, date1, date2 ) :
        """ Get the payed reports on a renge of dates """
        daysofweek = [ 'Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sa', 'Do' ]
        reservations = self.get_payed_reservations().filter( date_start__range=( date1, date2 ) )
        reports = []
        while date1 <= date2 :
            temp_rs = reservations.filter( date_start = date1 )
            temp_tot = temp_rs.aggregate( models.Sum( 'total' ) )
            reports.append( { 'date' : ( '{0} {2} {1}' ).format( daysofweek[datetime.datetime.weekday( date1 )], date1.strftime("%B")[:3], date1.day ), 'qty' : temp_rs.count(), 'total' : float( 0 if temp_tot['total__sum'] == None else str( temp_tot['total__sum'] ) ) } )
            date1 += timedelta( days = 1 )
        return reports
        
    def get_pending_reports_with_dates( self, date1, date2 ) :
        """ Get the pending reports on a renge of dates """
        daysofweek = [ 'Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sa', 'Do' ]
        reservations = self.get_pending_reservations().filter( date_start__range=( date1, date2 ) )
        reports = []
        while date1 <= date2 :
            temp_rs = reservations.filter( date_start = date1 )
            temp_tot = temp_rs.aggregate( models.Sum( 'total' ) )
            reports.append( { 'date' : ( '{0} {2} {1}' ).format( daysofweek[datetime.datetime.weekday( date1 )], date1.strftime("%B")[:3], date1.day ), 'qty' : temp_rs.count(), 'total' : float( 0 if temp_tot['total__sum'] == None else str( temp_tot['total__sum'] ) ) } )
            date1 += timedelta( days = 1 )
        return reports
        
    def get_reports_with_dates( self, date1, date2 ) :
        """ Get all reports on a renge of dates """
        daysofweek = [ 'Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sa', 'Do' ]
        reservations = ReservationCabin.objects.filter( date_start__range=( date1, date2 ) )
        reports = []
        while date1 <= date2 :
            temp_rs = reservations.filter( date_start = date1 )
            temp_tot = temp_rs.aggregate( models.Sum( 'total' ) )
            reports.append( { 'date' : ( '{0} {2} {1}' ).format( daysofweek[datetime.datetime.weekday( date1 )], date1.strftime("%B")[:3], date1.day ), 'qty' : temp_rs.count(), 'total' : float( 0 if temp_tot['total__sum'] == None else str( temp_tot['total__sum'] ) ) } )
            date1 += timedelta( days = 1 )
        return reports
        
    def get_cabin_reports_by_month( self, date ) :
        """ Get cabins with total rev each reports by month """
        reports = []
        reservations = self.get_payed_reservations().filter( date_start__year = date.year, date_start__month = date.month )
        cabins = Cabin.objects.all()
        reports = [ { 'cabin' : c, 'total' : 0 } for c in cabins ]
        for r in reservations :
            delta = r.date_end - r.date_start
            for d in r.details.all() :
                for rep in reports :
                    if rep['cabin'] == d.product :
                        rep['total'] += float( d.product.price * delta.days )
        for r in reports :
            r['cabin'] = CabinSerializer( r['cabin'], many=False ).data
        return reports
        
    def get_cabin_reports_by_year( self, year ) :
        """ get cabins with total rev each reports by year """
        reservations = self.get_payed_reservations().filter( date_start__year = year )
        cabins = Cabin.objects.all()
        reports = [ { 'cabin' : c, 'total' : 0 } for c in cabins ]
        for r in reservations :
            delta = r.date_end - r.date_start
            for d in r.details.all() :
                for rep in reports :
                    if rep['cabin'] == d.product :
                        rep['total'] += float( d.product.price * delta.days )
        for r in reports :
            r['cabin'] = CabinSerializer( r['cabin'], many=False ).data
        return reports
        
    def get_cabin_reports_by_dates( self, date1, date2 ) :
        """ get cabin reports with total rev between dates """
        reports = []
        reservations = self.get_payed_reservations().filter( date_start__range=( date1, date2 ) )
        cabins = Cabin.objects.all()
        reports = [ { 'cabin' : c, 'total' : 0 } for c in cabins ]
        for r in reservations :
            delta = r.date_end - r.date_start
            for d in r.details.all() :
                for rep in reports :
                    if rep['cabin'] == d.product :
                        rep['total'] += float( d.product.price * delta.days )
        for r in reports :
            r['cabin'] = CabinSerializer( r['cabin'], many=False ).data
        return reports
        
class Reservation( models.Model ) :
    
    user = models.ForeignKey( User, related_name="user_creator" )
    user_client = models.ForeignKey( User, related_name="client_user", blank = True, null = True )
    reservation_info = models.ForeignKey( ReservationInfo, blank = True )
    reservation_type = models.ForeignKey( ReservationType )
    details = models.ManyToManyField( Detail )
    max_guests = models.IntegerField( default = 0, null=True )
    extra_guests_child = models.IntegerField( default = 0 )
    extra_guests_adult = models.IntegerField( default = 0 )
    total = models.DecimalField( max_digits = 9, decimal_places = 2, default = 0.00, blank = False )
    
    date_start = models.DateTimeField( blank = True )
    date_end = models.DateTimeField( blank = True )
    
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )
    
    def __str__( self ) :
        return ( "This is reservation {0}" ).format( self.id )
   
class Promotion( models.Model ) :
    
    user = models.ForeignKey( User )
    name = models.CharField( max_length = 100, blank = False, default = "" )
    description = models.CharField( max_length = 500, blank = True, default = "" )
    
    discount = models.DecimalField( max_digits = 9, decimal_places = 2, default = 0.00, blank = True )
    
    date_start = models.DateField()
    date_end = models.DateField()
    
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )
    
    def __str__( self ) :
        return self.name
