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


# TODO dir is ignored, dummy...
def compose_image(image_name, dir):
    print("compose_image")

    mfst = load_manifest("./batik.yaml")

    if not (os.path.isdir('.batik.build')):
        os.mkdir('.batik.build')

    print(mfst)

    alias = mfst['alias']

    image_name = f"{alias}.tar.xz"

    image_name = os.path.join('.batik.build', image_name)


    ignore = os.path.abspath('.batikignore')

    print(ignore)

    if(os.path.exists(ignore)):
        matches = parse_gitignore(ignore)
    else:
        matches = None

    with tarfile.open(image_name, "w:xz") as tar:
        for file in os.listdir(dir):
            print(file)

            if(file == image_name):
                print(f"Skipping {file}")
                continue

            if(matches and matches(file)):
                print(f"Skipping {file}")
                continue

            tar.add(file, arcname=os.path.join(alias, file))