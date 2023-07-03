import re
with open("data07.txt") as file:
    data = [f.strip() for f in file.readlines()]

class FileSystem:
    def __init__(self):
        self.fs = {}

    def get_dirs(self):
        return self.fs.keys()

    def display(self):
        for k,v in self.fs.items():
            print(k)

    def add(self, dirname, dir):
        self.fs[dirname] = dir

    def get_file_size(self, dirname):
        return self.fs[dirname].filesize

    def get_children(self, dirname):
        return self.fs[dirname].children

    def get_full_size(self, dirname):
        file_size = self.get_file_size(dirname)
        children = self.get_children(dirname)
        while len(children) > 0:
            child = children[0]
            file_size += self.get_file_size(child)
            children = children[1:] + self.get_children(child)
        return file_size

class Dir:
    def __init__(self, filesize, children):
        self.filesize = filesize
        self.children = children

def dir_to_string(dir):
    if dir == ["/"]: 
        return "/"
    return "/".join(dir)[1:]


fs = FileSystem()
wd = []
collecting_info = False
for d in data:
    if re.match(r'\$ cd (.*)', d):
        if collecting_info:
            fs.add(dir_to_string(wd), Dir(file_size, children))
            collecting_info = False
        if d == '$ cd ..':
            wd.pop(-1)
        else:
            wd.append(re.findall(r'\$ cd (.+)', d)[0])
    if d == "$ ls":
        collecting_info = True
        children = []
        file_size = 0
    if re.match("\d+", d):
        file_size += int(re.findall("\d+", d)[0])
    if d.startswith("dir"):
        child_path = wd + [re.findall("dir (.+)", d)[0]]
        children.append(dir_to_string(child_path))

fs.add(dir_to_string(wd), Dir(file_size, children))

sizes = []
for dir in fs.get_dirs():
    sizes.append(fs.get_full_size(dir))

print("star 1: " + str(sum([s for s in sizes if s < 100000])))

mem_available = 70000000 - fs.get_full_size("/")
mem_needed = 30000000 - mem_available

print("star 2: " + str(min([s for s in sizes if s > mem_needed])))