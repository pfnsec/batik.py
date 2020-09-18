import batik.remote.base as base
import requests



def get_deployments():
    params = {

    }

    headers = {"Authorization": base.get_auth_token()}

    r = requests.get(f"{base.CLUSTER_URL}/cmd/deployment", params, headers=headers)

    return r.json()


def get_deployment(id):
    params = {

    }

    headers = {"Authorization": base.get_auth_token()}

    r = requests.get(f"{base.CLUSTER_URL}/cmd/deployment/{id}", params, header=headers)

    return r.json()


def deploy(manifest):

    data = {
        "manifest": manifest
    }

    headers = {"Authorization": base.get_auth_token()}

    r = requests.post (
        f"{base.CLUSTER_URL}/cmd/deployment", 

        json = data,

        headers = headers
    )

    print("Deployed : ", r.json())

    return r.content


def undeploy(id):
    params = {
    }

    headers = {"Authorization": base.get_auth_token()}

    r = requests.delete(f"{base.CLUSTER_URL}/cmd/deployment/{id}", headers = headers)

    #r = requests.delete(f"{base.CLUSTER_URL}/deployment/{id}", params)

    return r.content

def trigger(id, payload):
    params = {
    }

    data = {
        "payload": payload
    }

    headers = {"Authorization": base.get_auth_token()}

    r = requests.post (
        f"{base.CLUSTER_URL}/cmd/deployment/{id}/trigger", 

        json = data,

        headers = headers
    )

    print("Triggered: ", r.json())

    return r.content

def download(id, manifest):
    params = {
    }

    data = {
        "manifest": manifest
    }

    headers = {"Authorization": base.get_auth_token()}

    dep = requests.get(f"{base.CLUSTER_URL}/cmd/deployment/{id}", params, header=headers)

    r = requests.post (
        f"{base.CLUSTER_URL}/cmd/deployment/{id}/download", 

        json = data,

        headers = headers
    )

    print("Triggered: ", r.json())

    return r.content