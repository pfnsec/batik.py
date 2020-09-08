from .base import Base

from json import dumps

import batik.remote.deployment as deployment

import os 
import tarfile
import batik.local.image as image



class Deploy(Base):
    """Deploy"""

    def run(self):
        mfst = image.load_manifest('./batik.yaml')

        deployment.deploy(mfst)

        #print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
