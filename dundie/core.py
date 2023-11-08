def load(filepath):
    """ Loads data from filepath to the database"""
    try:
        with open(filepath) as file_:
            return file_.readlines()
    except FileNotFoundError as e:
        print(f"File not Found {e}")
