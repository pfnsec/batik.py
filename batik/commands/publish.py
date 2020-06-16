from .base import Base

from json import dumps

import batik.remote.deployment as deployment
import batik.remote.package as package

import batik.local.image as image

import os 
import tarfile



class Publish(Base):
    """Publish"""

    def run(self):

        mf = image.load_manifest("./batik.yaml")

        alias = mf['alias']

        pkg = package.search_packages(alias)

        res = image.compose_image(f"{alias}.tar.xz", "./")

        #res = image.files_in_workflow()
