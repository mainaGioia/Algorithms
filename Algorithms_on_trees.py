#LCA least common ancestor between 2 nodes in Binary Tree

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#O(n)
def findLCA(root, val1, val2):
    path1 = []
    path2 = []
    if not findPath(root, val1, path1) or not findPath(root, val2, path2):
        print("please insert nodes belonging to the tree")
        return -1
    i = 0
    l1 = len(path1)
    l2 = len(path2)
    while (i < l1 and i < l2):
        if path1[i] != path2[i]:
            break
        i += 1
    return path[i-1]


def findPath(root, val, path):
    if root is None:
        return False
    path.append(root.val)
    print("added "+str(root.val)+" to the path to node "+str(val))
    #put here otherwise for 2 nodes that are parent and child, the node itself will not be in the path
    if root.val == val:
        return True
    if findPath(root.left, val, path) or findPath(root.right, val, path):
        print("i have found the subtree to "+str(val))
        return True
    print(str(root.val)+" does not belong to the path to "+str(val))
    path.pop()
    return False



#LCA in BST
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

#O(h) time and extra space for recursive calls
def findLCA(root, n1, n2):
     if (root is None):
             return False
     if n1 < root.val:
             return findLCA(root.left, n1, n2)
     if n1 > root.val:
             return findLCA(root.right, n1, n2)
     return root.val



#iterative
#O(h) time and O(h) space
def findLCA(root, n1, n2):
     while(root != None):
             if n1<root.val and n2< root.val:
                     root = root.left
             if n1 > root.val and n2 > root.val:
                     root = root.right
             else:
                     break
     return root.val
