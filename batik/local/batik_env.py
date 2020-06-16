import yaml
import os

if(os.path.isfile("./batik.env.yaml")):
    with open("./batik.env.yaml", 'r') as stream:
        try:
            env = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

if env is None:
    env = {}

get = env.get