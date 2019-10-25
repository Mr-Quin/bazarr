import os
from sqlite3worker import Sqlite3Worker

from get_args import args
from helper import path_replace, path_replace_movie, path_replace_reverse, path_replace_reverse_movie

database = Sqlite3Worker(os.path.join(args.config_dir, 'db', 'bazarr.db'), max_queue_size=256, as_dict=True)


class SqliteDictConverter:
    def __init__(self):
        self.keys = str()
        self.values = str()
        self.items = str()

    def convert(self, values_dict):
        if type(values_dict) is dict:
            for key, value in values_dict.items():
                self.keys += key + ", "
                if type(value) is not str:
                    value = str(value)
                else:
                    value = "'" + value + "'"
                self.values += value + ", "
                self.items += key + "=" + value + ", "
            self.keys = self.keys.rstrip(", ")
            self.values = self.values.rstrip(", ")
            self.items = self.items.rstrip(", ")
            return self
        else:
            pass


dict_converter = SqliteDictConverter()
