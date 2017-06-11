from rest_framework import serializers
from .models import *

class AlertNumbersSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = AlertNumbers
        fields = ( 'id', 'name', 'phone_number' )

class AlertEmailsSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = AlertEmails
        fields = ( 'id', 'name', 'email' )

class ContactEmailSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = ContactEmail
        fields = ( 'id', 'name', 'email' )

class TicketPricesSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = TicketPrices
        fields = ( 'id', 'name', 'price' )

class SignaturesSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = Signatures
        fields = ( 'id', 'name', 'img_url' )