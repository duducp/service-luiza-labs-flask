import os

from dotenv import load_dotenv

load_dotenv(verbose=True)
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    ENVIRONMENT = os.getenv("ENVIRONMENT", "")

    # Flask
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 5000))
    CSRF_ENABLED = os.getenv("CSRF_ENABLED", True)
    SECRET_KEY = os.getenv("SECRET_KEY", "e6cf6d81-a23c-4712-96c8-c8e6c79cf11f")

    # Restplus
    SWAGGER_TITLE = os.getenv("SWAGGER_TITLE", "Lot")
    SWAGGER_DESCRIPTION = os.getenv(
        "SWAGGER_DESCRIPTION", "This service is responsible for the lots"
    )
    SWAGGER_UI_DOC_EXPANSION = None  # None, "list", "full"
    RESTPLUS_VALIDATE = False
    RESTPLUS_MASK_SWAGGER = False
    ERROR_INCLUDE_MESSAGE = False
    ERROR_404_HELP = False

    # Sql Alchemy
    DATABASE_ENGINE = os.getenv("DATABASE_ENGINE", "postgresql")
    DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
    DATABASE_PORT = int(os.getenv("DATABASE_PORT", "5432"))
    DATABASE_USER = os.getenv("DATABASE_USER", "postgres")
    DATABASE_PW = os.getenv("DATABASE_PW", "postgres")
    DATABASE_DB = os.getenv("DATABASE_DB", "xtracelot")

    if DATABASE_ENGINE.lower() == "sqlite":
        SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
    else:
        SQLALCHEMY_DATABASE_URI = f"{DATABASE_ENGINE}"
        SQLALCHEMY_DATABASE_URI += f"://{DATABASE_USER}"
        SQLALCHEMY_DATABASE_URI += f":{DATABASE_PW}"
        SQLALCHEMY_DATABASE_URI += f"@{DATABASE_HOST}"
        SQLALCHEMY_DATABASE_URI += f":{DATABASE_PORT}"
        SQLALCHEMY_DATABASE_URI += f"/{DATABASE_DB}"

    # Others
    SERVICE_PRODUCTS = os.getenv("SERVICE_PRODUCTS", "http://challenge-api.luizalabs.com/api/product")


class Development(Config):
    ENVIRONMENT_NAME = os.getenv("ENVIRONMENT_NAME", "DESENVOLVIMENTO")
    SWAGGER_VISIBLE = os.getenv("SWAGGER_VISIBLE", True)
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", True)
    SQLALCHEMY_ECHO = os.getenv("SQLALCHEMY_ECHO", True)
    TESTING = os.getenv("TESTING", False)
    DEBUG = os.getenv("DEBUG", True)
    FLASK_ENV = os.getenv("FLASK_ENV", "development")


class Staging(Config):
    ENVIRONMENT_NAME = os.getenv("ENVIRONMENT_NAME", "HOMOLOGAÇÃO")
    SWAGGER_VISIBLE = os.getenv("SWAGGER_VISIBLE", True)
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", False)
    SQLALCHEMY_ECHO = os.getenv("SQLALCHEMY_ECHO", False)
    DEBUG = os.getenv("DEBUG", False)
    TESTING = os.getenv("TESTING", True)
    FLASK_ENV = os.getenv("FLASK_ENV", "testing")


class Production(Config):
    ENVIRONMENT_NAME = os.getenv("ENVIRONMENT_NAME", "PRODUÇÃO")
    SWAGGER_VISIBLE = os.getenv("SWAGGER_VISIBLE", False)
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", False)
    SQLALCHEMY_ECHO = os.getenv("SQLALCHEMY_ECHO", False)
    TESTING = os.getenv("TESTING", False)
    DEBUG = os.getenv("DEBUG", False)
    FLASK_ENV = os.getenv("FLASK_ENV", "production")


def load_config():
    envs = {
        "develop": Development,
        "development": Development,
        "staging": Staging,
        "production": Production,
        "master": Production,
    }

    return envs.get(Config.ENVIRONMENT, Development)