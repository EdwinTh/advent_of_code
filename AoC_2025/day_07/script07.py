from collections import Counter
with open('data07.txt') as d:
    data = [el.strip() for el in d.readlines()]

beam_at = set([i for i in range(len(data[0])) if data[0][i] == 'S'])

splitted = 0

for i in range(1, len(data)):
    new_beam_at = []
    for ba in beam_at:
        if data[i][ba] == '^':
            splitted += 1
            new_beam_at += [ba-1,ba+1]
        else:
            new_beam_at += [ba]
    beam_at = set(new_beam_at)

print("Star 1:", splitted)

class Beam:
    def __init__(self, column):
        self.column = column

class Node:
    def __init__(self, i, j, is_root=False):
        self.id = str(i) + '-' + str(j)
        self.children = [Beam(j-1), Beam(j+1)]
        if is_root:
            self.children = [Beam(j)]

    def replace_beam_by_node_id(self, j, node_id):
        new_children = []
        for child in self.children:
            if isinstance(child, Beam) and child.column == j:
                    new_children.append(node_id)
            else:
                new_children.append(child)
        self.children = new_children
    
class Tree:
    def __init__(self, root_i, root_j):
        self.root_id = str(root_i) + '-' + str(root_j)
        self.nodes = [Node(root_i, root_j, is_root=True)]

    def _get_node(self, node_id):
        return [n for n in self.nodes if n.id == node_id][0]

    def _add_node(self, i, j):
        self.nodes += [Node(i, j)]

    def _replace_beam_by_node_id_nodes(self, j, node_id):
        for node in self.nodes:
            node.replace_beam_by_node_id(j, node_id)

    def new_node(self, i, j):
        self._add_node(i, j)
        self._replace_beam_by_node_id_nodes(j, str(i) + '-' + str(j))

    ## This was my first attempt, building up a list with all the possible paths
    ## This was never going to finish in time, but it is correct
    def get_all_paths(self):
        paths = [[self.root_id]]
        while True:
            new_paths = []
            for p in paths:
                if isinstance(p[-1], Beam):
                    new_paths.append(p)
                else:
                    for c in self._get_node(p[-1]).children:
                        p_iter = p + [c]
                        new_paths.append(p_iter)
                paths = new_paths
            if all([isinstance(p[-1], Beam) for p in paths]):
                break
        return paths
    
    # This is the final implementation and runs just a sec
    # It counts for each node how many paths are leading there by taking the sum
    # of all the paths that lead to its parents. If a child is a beam and not a node
    # it will lead to the floor and thus is the end. Then we add the paths leading to
    # that path to the total.

    def count_paths(self):
        total_paths = 0
        active_nodes = {self.root_id:1}
        while True:
            new_nodes = {}
            for k,v in active_nodes.items():
                children = self._get_node(k).children
                for c in children:
                    if isinstance(c, Beam):
                        total_paths += v
                    elif c in new_nodes:
                        new_nodes[c] += v
                    else:
                        new_nodes[c] = v
            if len(new_nodes) == 0:
                return(total_paths)
            active_nodes = new_nodes

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "S":
            tree = Tree(i, j)
        elif data[i][j] == "^":
            tree.new_node(i, j)

print("Star 2:", tree.count_paths())
