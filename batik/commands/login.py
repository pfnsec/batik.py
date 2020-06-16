from .base import Base

from json import dumps

import batik.remote.deployment as deployment
import batik.remote.package as package
import batik.remote.user as user

import os 
import batik.env 
import tarfile

hub_url = batik.env("hub_url") 


class Login(Base):
    """Login"""

    def run(self):
        #res = deployment.get_deployments()
        if self.options["create"]:
            print(f"Creating new account for {hub_url}")
            email = input("Email: ")
            username = input("Username: ")
            password = input("password: ")

            res = user.create_user(username, email, password)
            print(res)

        else: 
            print(f"Logging into {hub_url}")
            email    = batik.env("email") or input("Email: ") 
            password = batik.env("password") or input("Password: ") 

            with user.session() as session:
                res = user.login(session, email, password)
                print("login", res)

