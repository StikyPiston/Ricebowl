import argparse
from ricebowl import repo

def main():
    parser = argparse.ArgumentParser(description="Ricebowl - Linux rice installer")
    subparsers = parser.add_subparsers(dest="command")

    # `list` command
    list_parser = subparsers.add_parser("list", help="List available rices")

    # `install` command
    install_parser = subparsers.add_parser("install", help="Install a rice")
    install_parser.add_argument("name", help="Name of the rice to install")

    args = parser.parse_args()

    if args.command == "list":
        repo.list_rices()
    elif args.command == "install":
        repo.install_rice(args.name)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
