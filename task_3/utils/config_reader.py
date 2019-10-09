import json
import os
from collections import namedtuple
from pathlib import Path


class ConfigReader:

    @staticmethod
    def get_inst():
        return namedtuple("Config", ConfigReader._get_data().keys()
                          )(*ConfigReader._get_data().values())

    @staticmethod
    def _get_data(encoding='utf-8'):
        path = Path(os.path.join(os.path.dirname(__file__), '..',
                                 'resources', 'config.json'))
        return json.loads(path.read_text(encoding))
