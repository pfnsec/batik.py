import batik.remote.base as base
import requests



def get_deployments():
    params = {

    }

    headers = {"Authorization": base.get_auth_token()}

    r = requests.get(f"{base.CLUSTER_URL}/cmd/deployment/", params, headers=headers)

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

    return r.content


def undeploy(id):
    params = {
    }

    r = requests.delete(f"{base.CLUSTER_URL}/cmd/deployment/{id}", params)

    #r = requests.delete(f"{base.CLUSTER_URL}/deployment/{id}", params)

    return r.content