import os
import json


class JsonDB:
    def __init__(self, filepath):
        self.filepath = filepath

    def add(self, dct):
        jfile = self.read()
        newjfile = jfile.update(dct)
        self.write(newjfile)

    def delete_key(self, key):
        jfile = self.read()
        del jfile[key]
        self.write(jfile)

    def write(self, data):
        jfile =  open(self.filepath, "w")
        json.dump(data, jfile)
        jfile.close()

    def read(self):
        jfile = open(self.filepath, "r")
        dct = json.loads(jfile.read())
        jfile.close()
        return dct

