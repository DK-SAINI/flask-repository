import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    password = "asdf"
    username = "bizzappdev"
    host = "localhost"
    port = 5432
    db_name = "cfx_flask"

    SQLALCHEMY_DATABASE_URI = f"postgresql://{username}:{password}@{host}:{port}/{db_name}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
