import requests
import re
import os
import tarfile

import batik.remote.base as base
import batik.local.batik_env as batik_env
import batik.local.image as image
import json


def get_packages():
    params = {

    }

    r = requests.get(f"{base.HUB_URL}/package/", params)

    return r.json()


def get_package(user, alias):
    params = {
        "user": user,
        "alias": alias,
    }

    r = requests.get(f"{base.HUB_URL}/package/name/{user}/{alias}")

    return r.json()

def search_packages(query):
    params = {
        "query": query
    }

    r = requests.get(f"{base.HUB_URL}/package/search", params)

    return r.json()


# TODO: do package images need tags? I mean, of course they do. Add tags.
def upload_package_image(id, file):

    params = {
        # "tag": tag,

        # "hash": hash
    }

    headers = {"Authorization": base.get_auth_token()}

    mfst = image.load_manifest('./batik.yaml')

    data = {
        "manifest": json.dumps(mfst)
    }
    
    r = requests.post (
        f"{base.HUB_URL}/package/id/{id}/upload", 

        files = {
            "file": file
        }, 

        data = data,

        headers = headers
        
    )

    return r.json()


def download_package_image(id, subdir, alias):

    subdir = os.path.join('batik_layers', subdir)

    layer_path = os.path.join(subdir, alias)


    if not os.path.isdir('batik_layers'):
        os.mkdir('batik_layers')

    if not os.path.isdir(subdir):
        os.mkdir(subdir)

    if not os.path.isdir(layer_path):
        os.mkdir(layer_path)
    else:
        print(f"skipping {layer_path}")
        return layer_path


    params = {

        # "tag": tag,

        # "hash": hash
    }

    r = requests.get(f"{base.HUB_URL}/package/id/{id}/latest", params)
    r.raise_for_status()

    cd = r.headers['content-disposition']

    filename = re.findall("filename=(.+)", cd)[0]

    #filename = os.path.join('.batik.download', filename)
    filename = os.path.join(subdir, filename)


    with open(filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192): 
            # If you have chunk encoded response uncomment if
            # and set chunk_size parameter to None.
            #if chunk: 
            f.write(chunk)


    tar = tarfile.open(filename, "r:xz")

    tar.extractall(path=layer_path)

    tar.close()

    os.remove(filename)

    return filename


def get_package_by_id(id):
    params = {

    }

    r = requests.get(f"{base.HUB_URL}/package/id/{id}", params)

    return r.json()


def get_package_by_name(user, alias):
    params = {

    }

    r = requests.get(f"{base.HUB_URL}/package/name/{user}/{alias}", params)

    return r.json()


def create_package(alias):
    params = {
        "alias": alias
    }

    headers = {"Authorization": base.get_auth_token()}

    r = requests.get(f"{base.HUB_URL}/package/create", params, headers=headers)

    return r.content


def delete_package(packageId):
    params = {
        "packageId": packageId
    }

    r = requests.get(f"{base.HUB_URL}/package/delete", params)

    return r.content
