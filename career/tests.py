tree_list = ["Parents", "Children", "GrandChildren", "Children"]
tree_dict = {}
print(tree_dict)
for key in reversed(tree_list):
    print(key)
    tree_dict = {key: tree_dict}
    print(tree_dict)

print(tree_dict)
