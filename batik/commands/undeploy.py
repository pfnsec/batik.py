from .base import Base

from json import dumps

import batik.remote.deployment as deployment

import os 

class Undeploy(Base):
    """Undeploy"""

    def run(self):
        deployment.undeploy(self.options["<deployId>"])

       #print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
