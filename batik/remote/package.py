import requests
import re
import os
import tarfile

import batik.remote.base as base
import batik.local.batik_env as batik_env
import batik.local.image as image
import json
from clint.textui.progress import Bar as ProgressBar
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor


def create_callback(encoder):
    encoder_len = encoder.len
    bar = ProgressBar(expected_size=encoder_len, filled_char='=')

    def callback(monitor):
        bar.show(monitor.bytes_read)

    return callback


def get_packages(query, page):
    params = {
        'query': query,
        'page': page,
    }

    r = requests.get(f"{base.HUB_URL}/cmd/package", params)

    return r.json()


def get_package(username, alias):
    params = {
        "username": username,
        "alias": alias,
    }

    r = requests.get(f"{base.HUB_URL}/cmd/package/{username}/{alias}")

    return r.json()


# Marked for delete...
def search_packages(query):
    params = {
        "query": query
    }

    r = requests.get(f"{base.HUB_URL}/package/search", params)

    return r.json()


# TODO: do package images need tags? I mean, of course they do. Add tags.
def upload_package_image(username, alias, file):

    params = {
        # "tag": tag,

        # "hash": hash
    }


    mfst = image.load_manifest('./batik.yaml')

    data = {
        "manifest": json.dumps(mfst)
    }

    encoder = MultipartEncoder({
        "manifest": json.dumps(mfst),
        'file': (f'{alias}.tar.xz', file, "application/octet-stream")
        })
    
    callback = create_callback(encoder)

    monitor = MultipartEncoderMonitor(encoder, callback)

    
    r = requests.post (
        f"{base.HUB_URL}/cmd/package/{username}/{alias}/upload", 

        #files = monitor,
        #files = {
        #    "file": file
        #}, 

        data = monitor,

        headers = {
            "Authorization": base.get_auth_token(),
            "Prefer": "respond-async", 
            "Content-Type": encoder.content_type
        }
        
    )

    print(r.content)

    return r.json()


def download_package_image(username, alias):

    subdir = os.path.join('batik_layers', username)

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

    r = requests.get(f"{base.HUB_URL}/cmd/package/{username}/{alias}/latest", params)
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

    try:
        r = requests.get(f"{base.HUB_URL}/cmd/package/{user}/{alias}", params)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        return None

    return r.json()


def create_package(username, alias):
    data = {
        "username": username,
        "alias": alias
    }

    headers = {"Authorization": base.get_auth_token()}

    r = requests.post (
        f"{base.HUB_URL}/cmd/package", 


        json = data,

        headers = headers
        
    )

    return r.content


def delete_package(username, alias):
    params = {
        #"packageId": packageId
    }

    r = requests.delete(f"{base.HUB_URL}/cmd/package/{username}/{alias}", params)

    return r.content
