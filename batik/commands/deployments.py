from .base import Base

from json import dumps

import batik.remote.deployment as deployment

import os 
import tarfile




class Deployments(Base):
    """Deployments"""

    def run(self):
        res = deployment.get_deployments()
        print(res)

        

        #print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
