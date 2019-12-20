
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if inserting we must already have a tree/root
        # if value is less that self.value go left, make a new node/tree if its empty, otherwise keep going (recursion)
        # if greater that/equal to the go right, make a new tree/node if epty otherwise keep going (recursion)

        def recurse_inner(node, value):
            new_node = BinarySearchTree(value)
            current = node
            if value >= node.value and node.right == None:
                node.right = new_node
                return
            elif value < node.value and node.left == None:
                node.left = new_node
                return
            elif value >= node.value and node.right != None:
                current = node.right
            elif value < node.value and node.left != None:
                current = node.left
            recurse_inner(current, value)

        return recurse_inner(self, value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target, node='friend'):
        # if target == self.value return it
        #go left or right based on smaller or greater
        if node == 'friend':
            node = self
       
        if node == None:
            return False
        elif node.value == target:
            # print('something else')
            # print('value', node.value, target)
            return True
        else:
            if target < node.value:
                node = node.left
            elif target >= node.value:
                node = node.right
                # print('check')

            
        # print('hello', self.value)
        # print(inner(self, target))
        return self.contains(target, node)