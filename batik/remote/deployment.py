import batik.remote.base as base
import requests



def get_deployments():
    params = {

    }

    r = requests.get(f"{base.URL}/deployment/", params)

    return r.json()


def get_deployment(id):
    params = {

    }

    r = requests.get(f"{base.URL}/deployment/{id}", params)

    return r.json()


def deploy():
    params = {

    }

    r = requests.get(f"{base.URL}/deployment/create", params)

    return r.content


def undeploy(id):
    params = {
        "deployId": id
    }

    r = requests.get(f"{base.URL}/deployment/delete", params)

    #r = requests.delete(f"{base.URL}/deployment/{id}", params)

    return r.content