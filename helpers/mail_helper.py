# -*- coding: utf-8 -*-
from general.models import *
from reservations.models import *
from django.template.loader import get_template, render_to_string
import requests

MAIL_URL = "https://api.mailgun.net/v3/balneariolaspalmas.co/messages"
API_KEY = "key-93786709ada1dde6b5857ed681388ac8"

def send_contact_form( name, email, subject, message ) :
    '''
    Send message to mailgun api as a contact form
    email - the email that you are sending to
    subject - the title of the mail
    message - Well the content
    '''
    return requests.post(
        MAIL_URL,
        auth = ( "api", API_KEY ),
        data = {
            "from" : ( "{0} <{1}>" ).format( name, email ),
            "to" : [ ContactEmail.objects.get( pk = 1 ).email ],
            "subject" : subject,
            "text" : message 
        }
    )

def verification_contact_email( name, email, subject, message ) :
    contact = ContactEmail.objects.get( pk = 1 )
    data = {
        "name" : name,
        "message" : message
    }
    htmly = render_to_string( 'ver_contact_email.html', data )
    return requests.post(
        MAIL_URL,
        auth = ( "api", API_KEY ),
        data = {
            "from" : ( "{0} <{1}>" ).format( contact.name, contact.email ),
            "to" : [ email ],
            "subject" : "Balneario Las Palmas",
            "html" :  htmly
        }
    )
    
def reservation_cabin_to_alert( reservation ) :
    
    ticket_prices = TicketPrices.objects.all()
    
    subtotal = ( ticket_prices[0].price * reservation.extra_guests_child )
    subtotal += ( ticket_prices[1].price * reservation.extra_guests_adult )
    
    for d in reservation.details.all() :
        subtotal += ( d.qty * d.product.price )
        
    data = {
        "reservation" : reservation,
        "details" : reservation.details.all(),
        "reservation_info" : reservation.reservation_info,
        "price_ticket_adult" : ticket_prices[1].price,
        "price_ticket_child" : ticket_prices[0].price,
        "subtotal" : subtotal,
        "nights" : int( float( reservation.total ) / float( subtotal ) ) + (float( reservation.total ) % float( subtotal ) > 0)
    }
    htmly = render_to_string( "ver_reservation_cabin.html", data )
    
    return requests.post(
        MAIL_URL,
        auth = ( "api", API_KEY ),
        data = {
            "from" : ( "{0} <{1}>" ).format( "Balneario Las Palmas", "reservaciones@balneariolaspalmas.co" ),
            "to" : [ reservation.reservation_info.email ],
            "subject" : "Recibo de reservación",
            "html" : htmly
        }
    )
    
def reservation_cabin_to_alerts( reservation ) :
    
    ticket_prices = TicketPrices.objects.all()
    
    subtotal = ( ticket_prices[0].price * reservation.extra_guests_child )
    subtotal += ( ticket_prices[1].price * reservation.extra_guests_adult )
    
    for d in reservation.details.all() :
        subtotal += ( d.qty * d.product.price )
        
    data = {
        "reservation" : reservation,
        "details" : reservation.details.all(),
        "reservation_info" : reservation.reservation_info,
        "price_ticket_adult" : ticket_prices[1].price,
        "price_ticket_child" : ticket_prices[0].price,
        "subtotal" : subtotal,
        "nights" : int( float( reservation.total ) / float( subtotal ) ) + (float( reservation.total ) % float( subtotal ) > 0)
    }
    htmly = render_to_string( "ver_reservation_cabin.html", data )
    mails = [ c.email for c in AlertEmails.objects.all() ]

    requests.post(
        MAIL_URL,
        auth = ( "api", API_KEY ),
        data = {
            "from" : ( "{0} <{1}>" ).format( "Balneario Las Palmas", "reservaciones@balneariolaspalmas.co" ),
            "to" : mails,
            "subject" : "Alerta de reservación",
            "html" : htmly
        }
    )
    
def alert_test( ) :
    
    reservation = ReservationCabin.objects.get( pk = 23 )
    ticket_prices = TicketPrices.objects.all()
    
    subtotal = ( ticket_prices[0].price * reservation.extra_guests_child )
    subtotal += ( ticket_prices[1].price * reservation.extra_guests_adult )
    
    for d in reservation.details.all() :
        subtotal += ( d.qty * d.product.price )
        
    data = {
        "reservation" : reservation,
        "details" : reservation.details.all(),
        "reservation_info" : reservation.reservation_info,
        "price_ticket_adult" : ticket_prices[1].price,
        "price_ticket_child" : ticket_prices[0].price,
        "subtotal" : subtotal,
        "nights" : int( float( reservation.total ) / float( subtotal ) ) + (float( reservation.total ) % float( subtotal ) > 0)
    }
    htmly = render_to_string( "ver_reservation_cabin.html", data )
    return requests.post(
        MAIL_URL,
        auth = ( "api", API_KEY ),
        data = {
            "from" : ( "{0} <{1}>" ).format( "Balneario Las Palmas", "reservaciones@balneariolaspalmas.co" ),
            "to" : [ reservation.reservation_info.email ],
            "subject" : "Recibo de reservación",
            "html" : htmly
        }
    )