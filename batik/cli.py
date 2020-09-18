"""
batik

Usage:
  batik deploy 
  batik deployments
  batik download <deployId> 
  batik trigger <deployId> <payload>
  batik undeploy <deployId>
  batik hub [add]
  batik hub [publish]
  batik hub [mkimg]
  batik hub [resolve]
  batik hub [list <query> [-p <page>]]
  batik hub [search <query>]
  batik hub [get <package>]
  batik hub [download <packageId>]
  batik hub [delete <packageId>]
  batik -h | --help
  batik --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  batik deployments

Help:
  For help using this tool, please open an issue on the Github repository:
"""


from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION

def main():
    """Main CLI entrypoint."""
    import batik.commands
    options = docopt(__doc__, version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.

    for (k, v) in options.items(): 
        if hasattr(batik.commands, k) and v:
            module = getattr(batik.commands, k)

            batik.commands = getmembers(module, isclass)
            print("batik.commands")
            print(batik.commands)

            command = [command[1] for command in batik.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
