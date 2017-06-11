#Libraries
from imgurpython import ImgurClient
from products.models import Cabin, Pool
from django.conf import settings
import os, json

#this variables are the ones that the imgur api give us after registering the aplication
client_id = 'a9e5cbb0585d300'
client_secret = '534f7fa674d788358fdced77e7e30e90336fa766'
# Set te client_id on the imgurClient method and the client_secret variables
client = ImgurClient(client_id, client_secret)

def save_image( file ) :
    """
    Saves an image to imgur server and then
    returns the link
    """
    json_shit = client.upload_from_path( file, config=None, anon=True )
    os.remove( file )
    return json_shit['link']