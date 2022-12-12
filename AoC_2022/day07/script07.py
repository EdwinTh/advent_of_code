import re
with open("data07.txt") as file:
    data = [f.strip() for f in file.readlines()]
data = [d for d in data if d not in ['$ cd ..', '$ ls']]

folders = {}
files = {}
current_folder = "/"
filesize = 0
for d in data[1:]:
    if d[:4] == '$ cd':
        files[current_folder] = filesize
        filesize = 0
        current_folder = d[5:]
    elif d[:3] == 'dir':
        folders[d[4:]] = current_folder
    else:        
        filesize += int(re.findall(r'\d+', d)[0])
files[current_folder] = filesize

all_dirs = list(set(list(folders.keys()) + list(folders.values())))
children = {}
for d in all_dirs:
    children[d] = [k for k,v in folders.items() if v == d]
print(children)

def get_sizes(cs):
    for c in cs:
        return get_sizes(children[c])
        

print(get_sizes(children['/']))