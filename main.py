import tree

# test empty
root1 = tree.Node(None, 1, None)
empty1 = root1.left
empty2 = root1.right

tree.test(empty1, empty2, 0, 0, -1, -1, True)


# test one node identical trees
root2 = tree.Node(None, 1, None)

tree.test(root1, root2, 1, 1, 0, 0, True)


# add node
root1.left = tree.Node(None, 1, None)
root2.left = tree.Node(None, 1, None)

tree.test(root1, root2, 1, 1, 1, 1, True)


# add one mor node so that there are 2 leaves
root1.right = tree.Node(None, 1, None)
root2.right = tree.Node(None, 1, None)

tree.test(root1, root2, 2, 2, 1, 1, True)


# increase depth of the trees
root1.left.left = tree.Node(None, 1, None)
root2.left.left = tree.Node(None, 1, None)
root1.left.left.left = tree.Node(None, 1, None)
root2.left.left.left = tree.Node(None, 1, None)

tree.test(root1, root2, 2, 2, 3, 3, True)


# change value of node to differ the trees
root2.left.left.left = tree.Node(None, 2, None)

tree.test(root1, root2, 2, 2, 3, 3, False)


# change some node to None to differ the tree.py structure
root2.left.left.left = None

tree.test(root1, root2, 2, 2, 3, 2, False)
