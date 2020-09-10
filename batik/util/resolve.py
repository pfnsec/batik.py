import re
import os

import batik.remote.package as package
import batik.remote.user as user
import batik.local.image as image


def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        pass
        #globals()[package] = importlib.import_module(package)



def fetch(manifest):
    deps = {}


    if manifest.get('pip_deps'):
        for d in manifest['pip_deps']:
            print("Installing pip dep: ", d)
            install_and_import(d)


    for s in manifest['steps']:
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

        path = os.path.join(username, f"{alias}.tar.xz")

        res = package.download_package_image(username, alias)

        print(res)
