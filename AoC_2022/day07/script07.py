import re
with open("data07.txt") as file:
    data = [f.strip() for f in file]

print(data)
class fs_tree:

    def __init__(self, root = "/", root_files = {}):
        self.folders = {root : {}}
        self.files = {root : root_files}
        self.wd = [root]

    def add_folder(self, folders, name):
        if len(folders) == 1:
            self.folders[folders[0]] = {name: }
        return self.add_folder(self.folders[folders[0]], folders[1:], name)

    def add_files(self, foldername, filedict):
        self.files[foldername] = filedict
    
    def move_loc_down(self, foldername):
        self.loc = self. + [foldername]
    
    def move_loc_up(self):
        self.loc.pop(len(self.loc)-1)

        files = [d.split(" ") for d in data if d[0].isdigit()]
        self.files = {f[1]:int(f[0]) for f in files}
        
        self.folders = []

a = {'b':{'c':3}}


