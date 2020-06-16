import batik.remote.base 
import batik.remote.user as user
import batik.local.batik_env as batik_env
import os 

URL = os.environ.get('BATIK_BASE_URL') or "http://localhost:4210"
HUB_URL = os.environ.get('BATIK_HUB_URL') or "http://localhost:4220"

def get_auth_token():
    return batik_env.get("token")

    if not batik_env.get("token"):
        print(f"Logging into {HUB_URL}")
        email    = batik.env("email") or input("Email: ") 
        password = batik.env("password") or input("Password: ") 

        with user.session() as session:
            res = user.login(session, email, password)
            print("login", res)