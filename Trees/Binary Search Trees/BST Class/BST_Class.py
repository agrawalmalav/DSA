class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    
    def __init__(self):
        self.root = None
        self.numNodes = 0
    
    def printTreeHelper(self, root):
        if root == None:
            return
        print(root.data, ':', sep = '', end= '' )
        if root.left!= None:
            print('L:', root.left.data, ',', sep ='', end = '')
        if root.right!= None:
            print('R:', root.right.data, sep ='', end= '')
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)
        return

    def printTree(self):
    ##################################
    # PLEASE IMPLEMENT THIS FUNCTION #
    ##################################
        self.printTreeHelper(self.root)
        return
    
    
    def search(self, data):
    ##################################
    # PLEASE IMPLEMENT THIS FUNCTION #
    ##################################
        curr = self.root
        while curr != None:
            if curr.data == data:
                return True
            elif curr.data > data:
                curr = curr.left
            else:
                curr = curr.right
        else:
            return False


    def insertHelper(self, root, value):
        if root == None:
            return BinaryTreeNode(value)
        if value <= root.data:
            root.left = self.insertHelper(root.left, value)
        else:
            root.right = self.insertHelper(root.right, value)
        return root


        
    def insert(self, data):
    ##################################
    # PLEASE IMPLEMENT THIS FUNCTION #
    ##################################
        self.root = self.insertHelper(self.root, data)
        self.numNodes += 1
        return self.root
    
    def deleteHelper(self, root, data, deleted= False):
        if root == None:
            return False, root
        if root.data == data:
            if root.left == None and root.right == None:
                root = None
                return True, root
            elif root.left != None and root.right ==  None:
                return True, root.left
            elif root.right != None and root.left == None:
                return True, root.right
            else:
                root.data = root.right.data
                deleted, root.right = self.deleteHelper(root.right, root.data, deleted)
        elif root.data > data:
            deleted, root.left = self.deleteHelper(root.left, data, deleted)
        else:
            deleted, root.right = self.deleteHelper(root.right, data, deleted)
        return deleted, root


      
    def delete(self, data):
    ##################################
    # PLEASE IMPLEMENT THIS FUNCTION #
    ##################################
        deleted, self.root = self.deleteHelper(self.root, data)
        if deleted:
            self.numNodes -=1
        return self.root
    
    def count(self):
        return self.numNodes
        
b = BST()
q = int(input())
while (q > 0) :
    li = [int(ele) for ele in input().strip().split()]
    choice = li[0]
    q-=1
    if choice == 1:
        data = li[1]
        b.insert(data)
    elif choice == 2:
        data = li[1]
        b.delete(data)
    elif choice == 3:
        data = li[1]
        ans = b.search(data)
        if ans is True:
            print('true')
        else:
            print('false')
    else:
        b.printTree()
