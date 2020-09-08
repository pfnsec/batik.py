import batik.remote.base 
import batik.remote.user as user
import batik.local.batik_env as batik_env
import os 

#URL = os.environ.get('BATIK_BASE_URL') or "https://localhost:4210"

URL = batik_env.get('cluster_url') or "https://cluster.batik.sh"
HUB_URL = batik_env.get('hub_url') or "https://hub.batik.sh"
CLUSTER_URL = batik_env.get('cluster_url') or "https://cluster.batik.sh"

def get_auth_token():

    if not batik_env.get("token"):
        print("No token!")
        return
    else:
        return batik_env.get("token")