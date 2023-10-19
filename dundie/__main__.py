import argparse

def load(filepath):
    """ Loads data from filepath to the database"""
    try:
        with open(filepath) as file_:
            for line in file_:
                print(line)
    except FileNotFoundError as e:
        print(f"File not Found {e}")


def main():
    parser = argparse.ArgumentParser(
    description="Dundie CLI",
    epilog="Enjoy and use with cautions.",
    )
    parser.add_argument(
        "subcommand",
        type=str,
        help="Ajuda",
        choices=('load',"show","send"),
        default="help",
    )

    parser.add_argument(
        "filepath",
        type=str,
        help="File path to load",
        default=None,
    )

    args = parser.parse_args()
    try:
        globals()[args.subcommand](args.filepath)
    except KeyError:
        print("Subcommand is invalid")


if __name__ == "__main__":
    main()