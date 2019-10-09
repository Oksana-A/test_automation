import json
import os
from collections import namedtuple
from pathlib import Path


class ConfigReader:
    __instance = None

    def __init__(self):
        self.__framework_config = self.__get_namedtuple(
            'framework_config', os.path.join(os.path.dirname(__file__),
                                             '..', 'resources', 'config.json'))
        self.__projects_config = self.__get_namedtuple(
            'projects_config', os.path.join(os.path.dirname(
                os.path.dirname(__file__)), '..', 'projects', 'config.json'))
        self.__project_config = self.__get_namedtuple(
            'project_config', os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                '..', 'projects', 'aviasales', 'resources', 'config.json'))

    @staticmethod
    def get_inst():
        if ConfigReader.__instance is None:
            ConfigReader.__instance = ConfigReader()
        return ConfigReader.__instance

    def __get_namedtuple(self, name, path, encoding='utf-8'):
        data = json.loads(Path(path).read_text(encoding))
        return namedtuple(name, data.keys())(*data.values())

    def get_framework_config(self):
        return self.__framework_config

    def get_projects_config(self):
        return self.__projects_config

    def get_project_config(self):
        return self.__project_config
