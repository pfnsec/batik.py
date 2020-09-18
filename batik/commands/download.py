from .base import Base

from json import dumps

import batik.remote.deployment as deployment

import os 


class Download(Base):
    """Download"""

    def run(self):
        deployment.download(self.options["<deployId>"])

       #print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
