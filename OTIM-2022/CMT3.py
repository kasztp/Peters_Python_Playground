import random


class BTreeNode:
    def __init__(self, parent, num_children):
        self.keys = []   # values contained in this node
        self.n = num_children
        self.children = []
        self.parent = parent

    def is_leaf(self):
        return not self.children

    def is_root(self):
        return self.parent is None

    def overflow(self, left, right, key):
        # easy, we just need to add the new key and readjust the children
        old_child_idx = self.children.index(left)
        self.keys.insert(old_child_idx, key)
        self.children.insert(old_child_idx + 1, right)
        if len(self.keys) >= self.n:
            # we're going to overflow higher
            median_idx = len(self.keys) // 2
            median_key = self.keys[median_idx]

            # we will retain the left half in this node
            # and give the other half to the other node
            if self.is_root():
                # BTrees are funky, in that they grow at the root
                self.parent = BTreeNode(None, self.n)
                self.parent.children.append(self)
            sibling = BTreeNode(self.parent, self.n)
            sibling.keys = self.keys[median_idx+1:]
            sibling.children = self.children[median_idx+1:]
            for c in sibling.children:
                c.parent = sibling
            self.keys = self.keys[:median_idx]
            self.children = self.children[:median_idx+1]
            self.parent.overflow(self, sibling, median_key)

    def insert(self, key):
        if key in self.keys:
            # already in this node
            return

        if self.is_leaf():
            if len(self.keys) < (self.n - 1):
                # we have room
                for i, k in enumerate(self.keys):
                    # there are no children to worry about
                    if k > key:
                        self.keys.insert(i, key)
                        break
                else:
                    self.keys.append(key)

            else:
                all_keys = sorted(self.keys + [key])
                median_idx = len(all_keys) // 2
                median_key = all_keys[median_idx]

                if self.is_root():
                    self.parent = BTreeNode(None, self.n)
                    self.parent.children.append(self)

                # we will retain the left half in this node
                # and give the other half to the other node
                sibling = BTreeNode(self.parent, self.n)
                sibling.keys = all_keys[median_idx+1:]
                self.keys = all_keys[:median_idx]

                self.parent.overflow(self, sibling, median_key)
        else:
            for i, k in enumerate(self.keys + [float('inf')]):
                if k > key:
                    # this is the correct spot for the child
                    self.children[i].insert(key)
                    return

    def checksum(self):
        # recursive checksum
        node_hash = hash(tuple(self.keys))
        if self.children:
            children_hash = hash(tuple(child.checksum() for child in self.children))
            node_hash = hash((node_hash, children_hash))
        return node_hash

    def print(self, l=0):
        print('\t'*l, f"level {l} {self.keys}")
        for c in self.children:
            c.print(l+1)

class BTree:
    def __init__(self, order):
        self.order = order
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = BTreeNode(None, self.order)
        self.root.insert(key)
        if not self.root.is_root():
            # we grew
            self.root = self.root.parent

    def print(self):
        if not self.root:
            print("None")
        else:
            self.root.print(0)


def find_node_with_key(tree: BTree, key: int) -> BTreeNode:
    """
    For a given B-Tree, which is a special type of search tree, return
    the node containing the provided key. You can assume in all cases that
    the key exists in one of the nodes of the tree passed in
    Parameters
    __________
    tree
        A BTree object containing at least one key
    key
        A value to look for within the tree
    
    Returns
    _______
    A BTreeNode object containing the key
    """
    node = tree.root
    while not node.is_leaf():
        for i, k in enumerate(node.keys + [float('inf')]):
            if k > key:
                node = node.children[i]
                break
    return node


def generate_cases(seed):
    # DO NOT MODIFY
    rand = random.Random(seed)

    for i in range(100):
        tree = BTree(1 + 2*rand.randint(1, 4))
        tree_keys = list(range(1000))
        rand.shuffle(tree_keys)
        tree_keys = tree_keys[:rand.randint(20, 100)]
        for key in tree_keys:
            tree.insert(key)
        yield tree, rand.choice(tree_keys)


def checksum(
    implementation,
    seed
):
    # DO NOT MODIFY
    result = 0
    for tree, key in generate_cases(seed):
        node = implementation(tree, key)
        result = hash((result, node.checksum()))

    return result

if __name__ == "__main__":
    #
    # To help testing, checksum(find_node_with_key, 1) should return -2803493182871350012
    #
    seed_1_answer = -2803493182871350012

    #
    # Your final answer is the result of the next line
    #
    print(checksum(find_node_with_key, 0))
