"""Display KeyPair Info"""


from json import dumps
from Crypto.PublicKey import RSA
from pathlib import Path
import os
import qrcode
import base64

from .base import Base

def printQr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr.print_ascii()

    #img = qr.make_image(fill_color="black", back_color="white")



def createKeyPair():
    key = RSA.generate(2048)
    f = open('mykey.pem','wb')
    f.write(key.export_key('PEM'))
    f.close()


def loadKeyPair():
    if not os.path.exists('mykey.pem'):
        createKeyPair()
    f = open('mykey.pem','r')
    key = RSA.import_key(f.read())

    pubkey = key.publickey().export_key('OpenSSH')
    #pubkey = base64.b64encode(pubkey) 
    print(pubkey)
    return pubkey

    home = str(Path.home())


class Auth(Base):
    """Auth"""

    def run(self):
        pubkey = loadKeyPair()

        #printQr(pubkey)
        print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
