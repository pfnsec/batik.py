import os 
import tarfile 
import yaml

from batik.util.gitignore_parser import parse_gitignore



def files_in_workflow():
    print("file")
    for file in os.listdir("./"):
        print(file)
        print(os.path.join("./", file))



def load_manifest(file):
    with open(file, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)


def compose_image(image_name, dir):

    ignore = os.path.abspath('.batikignore')
    print(ignore)
    if(os.path.exists(ignore)):
        matches = parse_gitignore(ignore)
    else:
        matches = None

    with tarfile.open(image_name, "w:xz") as tar:
        for file in os.listdir(dir):

            if(file == image_name):
                print(f"Skipping {file}")
                continue

            if(matches and matches(file)):
                print(f"Skipping {file}")
                continue

            tar.add(file, arcname=os.path.join(image_name, file))