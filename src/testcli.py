import os

class Directory:
    def __init__(self, name):
        self._name = name

    def create(self):
        if os.path.isdir(self._name):
            print(f"{self._name} directory already exists.")
            return
        print(f"creating directory {self._name}")
        os.mkdir(self._name)
    
    def delete(self):
        if not os.path.exists(self._name):
            print(f"{self._name} does not exists.")
            return
        print(f"deleting directory {self._name}")
        os.rmdir(self._name)