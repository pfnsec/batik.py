
from .base import Base

from json import dumps

import batik.remote.deployment as deployment
import batik.remote.package as package
import batik.local.image as image

import os 
import tarfile


def make_tarfile(tar_file, source_file, inside_dir):
    with tarfile.open(tar_file, "w:xz") as tar:
        tar.add(source_file, arcname=os.path.join(inside_dir, source_file))



class Hub(Base):
    """Hub"""

    def run(self):
        #res = deployment.get_deployments()
        if self.options["add"]:
            res = package.create_package("batik-test")
            print(res)


        elif self.options["list"]:
            res = package.get_packages()

            print(res)


        elif self.options["search"]:
            res = package.search_packages(self.options["<query>"])

            print(res)


        elif self.options["download"]:
            res = package.download_package_image(self.options["<packageId>"], "batik-out-pkg.tar.xz")

            print(res)


        elif self.options["mkimg"]:

            #res = package.get_packages()
            res = image.compose_image("", "")

            print(res)



        elif self.options["upload"]:
            with open("batik-pkg.tar.xz", 'rb') as f:
                package.upload_package_image(self.options["<packageId>"], f)


        #print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
