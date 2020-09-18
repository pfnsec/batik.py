from .base import Base

from json import dumps

import batik.remote.deployment as deployment

import os 

class Trigger(Base):
    """Trigger"""

    def run(self):
        deployment.trigger(self.options["<deployId>"], self.options["<payload>"])

       #print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))