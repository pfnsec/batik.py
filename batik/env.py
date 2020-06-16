
import os 
import yaml

batik_env = {}
env = batik_env.get

def set_env_file(file):
    with open(file, 'r') as stream:
        try:
            batik_env = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)


# TODO eventually check other paths?
if(os.path.exists("./batik.env.yaml")):
    set_env_file("./batik.env.yaml")