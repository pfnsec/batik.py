from .base import Base

from json import dumps

import batik.remote.deployment as deployment

import os 
import tarfile



class Deploy(Base):
    """Deploy"""

    def run(self):
        deployment.deploy()


        #print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
