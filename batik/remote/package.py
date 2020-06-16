import batik.remote.base as base
import requests
import batik.local.batik_env as batik_env

token = batik_env.get("token")

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

    r = requests.get(f"{base.HUB_URL}/package/", params)

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
    
    r = requests.post(f"{base.HUB_URL}/package/{id}/upload", files={"file": file}, headers=headers)

    return r.json()


def download_package_image(id, file):
    params = {

        # "tag": tag,

        # "hash": hash
    }

    r = requests.get(f"{base.HUB_URL}/package/{id}/download", params)
    r.raise_for_status()

    with open(file, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192): 
            # If you have chunk encoded response uncomment if
            # and set chunk_size parameter to None.
            #if chunk: 
            f.write(chunk)

    return r.json()


def get_package_by_id(id):
    params = {

    }

    r = requests.get(f"{base.HUB_URL}/package/{id}", params)

    return r.json()


def create_package(alias):
    params = {
        "alias": alias
    }

    headers = {"Authorization": base.get_auth_token()}

    r = requests.get(f"{base.HUB_URL}/package/create", params, headers=headers)

    return r.content


def delete_pacakge(packageId):
    params = {
        "packageId": packageId
    }

    r = requests.get(f"{base.HUB_URL}/package/delete", params)

    return r.content
