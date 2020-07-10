import batik.remote.base as base
import requests



def me():

    headers = {"Authorization": base.get_auth_token()}

    r = requests.get(f"{base.HUB_URL}/user/me", headers = headers)

    r.raise_for_status()

    print(r.content)

    return get_user_by_id(r.json()['id'])


def get_users():
    params = {

    }

    r = requests.get(f"{base.HUB_URL}/user/", params)

    return r.json()


def get_user_by_name(name):

    r = requests.get(f"{base.HUB_URL}/user/name/{name}")

    return r.json()

def get_user_by_id(id):

    print(id)

    r = requests.get(f"{base.HUB_URL}/user/id/{id}")

    print(r.content)

    return r.json()


def search_users(query):
    params = {
        "query": query
    }

    r = requests.get(f"{base.HUB_URL}/user/search", params)

    return r.json()



def create_user(username, email, password):
    params = {
        "username": username,
        "email": email
    }

    r = requests.get(f"{base.HUB_URL}/user/create", params, auth=(email, password))

    return r.content


def session():
    return requests.Session()


def login(session, email, password):
    params = {
        "email": email
    }

    session.auth = (email, password)


    r = session.get(f"{base.HUB_URL}/user/login", params=params)

    return r.content

