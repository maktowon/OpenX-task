class Node:
    def __init__(self, left, val, right):
        self.left = left
        self.right = right
        self.val = val


def count_leaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)


def length(root):
    if root is None:
        return -1
    return max(1 + length(root.left), 1 + length(root.right))


def are_equal(t, u):
    if t is None and u is None:
        return True
    if t is None or u is None or t.val != u.val:
        return False
    return are_equal(t.left, u.left) and are_equal(t.right, u.right)


# t1 - tree1, t2 - tree2
# expected values: l - leaves, d - depth, eq - are equal
def test(t1, t2, l1, l2, d1, d2, eq):
    assert count_leaves(t1) == l1
    assert count_leaves(t2) == l2

    assert length(t1) == d1
    assert length(t2) == d2

    assert are_equal(t1, t2) == eq
