
from .base import Base

from json import dumps

import batik.remote.deployment as deployment
import batik.remote.package as package
import batik.remote.user as user
import batik.local.image as image
import batik.local.batik_env as batik_env

import os 
import re 
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

        elif self.options["me"]:
            res = user.me()

            print(res)


        elif self.options["list"]:
            page = self.options.get("<page>") or 1
            query = self.options.get("<query>") or ""
            res = package.get_packages(self.options["<query>"], page)

            print(res)


        elif self.options["publish"]:
            username = batik_env.get('username')

            mfst = image.load_manifest('./batik.yaml')
            alias = mfst['alias']
            
            #print(mfst)

            pkg_info = package.get_package_by_name(username, alias)
            print(pkg_info)

            if pkg_info == None:
                res = package.create_package(username, alias)
                print(res)

                pkg_info = package.get_package_by_name(username, alias)
            print(pkg_info)


            print(f"Publishing to @{username}/{alias}...")
            print(f"Package ID: {pkg_info}")

            image_name = f"{alias}.tar.xz"
            image_name = os.path.join('./.batik.build', image_name)

            with open(image_name, 'rb') as f:
                package.upload_package_image(username, alias, f)


        elif self.options["search"]:
            res = package.search_packages(self.options["<query>"])

            print(res)


        elif self.options["get"]:

            r = re.match("@(.+)/(.+)", self.options["<package>"])

            username = r.group(1)
            alias = r.group(2)
            print(username, alias)

            res = package.get_package_by_name(username, alias)

            package_id = res['id']

            path = os.path.join(username, f"{alias}.tar.xz")

            res = package.download_package_image(username, alias)
            



        elif self.options["download"]:
            #res = package.download_package_image(self.options["<packageId>"], "batik-out-pkg.tar.xz")

            print(res)


        elif self.options["mkimg"]:
            print("mkimg")

            #res = package.get_packages()
            res = image.compose_image("", os.curdir)

            print(res)


        elif self.options["resolve"]:
            #res = package.get_packages()
            print("resolve")

            deps = {}

            mfst = image.load_manifest('./batik.yaml')

            for s in mfst['steps']:
                r = re.match("(.+)/(.+)\.(.+)", s['name'])

                username = r.group(1)
                alias = r.group(2)
                print(username, alias)

                layer = f'{username}/{alias}'

                # Already fetched this layer?
                if(layer in deps): 
                    continue
                else:
                    deps[layer] = "unloaded"


                res = package.get_package_by_name(username, alias)
                print(res)

                package_id = res['id']

                path = os.path.join(username, f"{alias}.tar.xz")

                res = package.download_package_image(username, alias)

                print(res)




        #print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
