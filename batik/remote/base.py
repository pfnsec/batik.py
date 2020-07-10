import batik.remote.base 
import batik.remote.user as user
import batik.local.batik_env as batik_env
import os 

#URL = os.environ.get('BATIK_BASE_URL') or "https://localhost:4210"

URL = batik_env.get('cluster_url') or "http://localhost:4210"
HUB_URL = batik_env.get('hub_url') or "https://hub.batik.sh"

def get_auth_token():

    if not batik_env.get("token"):
        print(f"Logging into {HUB_URL}")
        email    = batik.env("email") or input("Email: ") 
        password = batik.env("password") or input("Password: ") 

        with user.session() as session:
            res = user.login(session, email, password)
            print("login", res)
    else:
        return batik_env.get("token")