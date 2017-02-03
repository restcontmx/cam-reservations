# -*- coding: utf-8 -*-
"""
Author - Ramiro Gutierrez Alaniz
Date - January, 9th 2017
"""
from Crypto.PublicKey import RSA
from base64 import b64decode, b64encode
from Crypto.Cipher import PKCS1_OAEP
import json 

"""
SecuritySystem class
this will be extended by the api view that wants to use the encryption system
"""
class SecuritySystem :
    
    def encrypt_data( self, data ) :
        """
        Encryption function
        will encrypt data with the client public key
        """
        try:
            
            f = open( 'certs/client_admin_balpres.pub', 'r+' )
            
            key = RSA.importKey( f.read() )
            cipher = PKCS1_OAEP.new( key )
            encrypted_data = cipher.encrypt( data )
            
            return b64encode( encrypted_data )
            
        except Exception, e:
            print( e )
            raise e
    
    def decrypt_data( self, data ) :
        """
        Decryption function
        Will decrypt with the server private
        """
        try :
            
            f = open( 'certs/server_rsa.key.pem', 'r+' )
            
            key = RSA.importKey( f.read() )
            cipher = PKCS1_OAEP.new( key )
            decrypted_data = cipher.decrypt( b64decode(data) )
            
            return decrypted_data
        
        except Exception, e :
            raise e

    def encrypt_long_data( self, data ) :
        """ Encypts data longer than 200 """
        if len( data ) <= 200 :
            return [ self.encrypt_data( data ) ]
        else :
            data_size = len( data )
            count = data_size / float( 200 )
            div_data = [ [ "" ] for i in range( 0, int( count ) + 1 ) ]
            while count >= 1 :
                div_data[ int( count ) ] = self.encrypt_data( data[:200] )
                data = data[200:]
                count-=1
            div_data[0] = self.encrypt_data( data )
            div_data.reverse()
            return div_data

    def decrypt_long_data( self, data ) :
        """ Decrypts data longer encrypted in peaces of 200 """
        return "".join( [ self.decrypt_data( p ) for p in json.loads( data ) ] )