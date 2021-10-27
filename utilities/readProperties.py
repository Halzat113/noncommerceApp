import configparser
from pathlib import Path


def get_project_root() -> str:
    return str(Path(__file__).parent.parent)


config = configparser.RawConfigParser()
config.read(get_project_root() + "\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationCredential(credential):
        url = config.get('common info', credential)
        if url is None:
            raise Exception("No such credential")
        else:
            return url

