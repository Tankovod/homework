# ------------- LESSON 6, EXERCISE 13 -------------------
# Write recursive function, received integer (depth) , function must
# generate tree with specified depth (every branch has 2 child branches)

def generate_list_tree(depth, tree=None):
    if depth > 0: tree = []
    if depth > 1: tree = [[], []]
    if depth > 2:
        for i in tree:
            tree[tree.index(i)] = generate_list_tree(depth-1, i)
    return tree


print(generate_list_tree(6))
