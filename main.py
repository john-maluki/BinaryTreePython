class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value


class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, value):
    new_node = Node(value)
    if self.root == None:
      self.root = new_node
    else:
      current_node = self.root
      while True:
        if value < current_node.value:
          #left
          if current_node.left == None:
            current_node.left = new_node
            break
          current_node = current_node.left
            
        else:
          #right
          if current_node.right == None:
            current_node.right = new_node
            break
          current_node = current_node.right

  def lookup(self, value):
    if self.root == None:
      return 'The value: {0} Not found.'.format(value)
    
    current_node = self.root
    while current_node != None:
      if value < current_node.value:
        current_node = current_node.left
      elif value > current_node.value:
        current_node = current_node.right
      elif value == current_node.value:
        return 'Value: {0} is available.'.format(current_node.value)
    
    return 'The value: {0} Not found.'.format(value)

  def remove(self, value):
    if self.root == None:
      return None
    
    current_node = self.root
    parent_node = None

    while current_node != None:
      if value < current_node.value:
        parent_node = current_node
        current_node = current_node.left
      elif value > current_node.value:
        parent_node = current_node
        current_node = current_node.right
      elif value == current_node.value:
        #we have match get to work
        #option 1: no right child
        if current_node.right == None:
          if parent_node == None:
            self.root = current_node.left
          else:
            # if parent > current_value, make #current left child a child of the root
            if current_node.value < parent_node.value:
              parent_node.left = current_node.left

            #if parent < current_value, make left child a child of the right
            elif current_node.value > parent_node.value:
              parent_node.right = current_node.left

        #Option 2: Right child which doesnt have a #left child   
        elif current_node.right.left == None:
          current_node.right.left = current_node.left
          if parent_node == None:
            self.root = current_node.right;
          else:
            #if parent > current, make right child #of the left the parent
            if current_node.value < parent_node.value:
              parent_node.left = current_node.right
            
            #if parent < current, make right child #a right child of the parent
            elif current_node.value > parent_node.value:
              parent_node.right = current_node.right

        else:
          #find the Right child's left most child
          leftmost = current_node.right.left
          leftmostParent = current_node.right
          while(leftmost.left != None):
            leftmostParent = leftmost
            leftmost = leftmost.left
          #Parent's left subtree is now leftmost's #right subtree
          leftmostParent.left = leftmost.right
          leftmost.left = current_node.left
          leftmost.right = current_node.right

          if parent_node == None:
            self.root = leftmost
          else:
            if current_node.value < parent_node.value:
              parent_node.left = leftmost
            elif current_node.value > parent_node.value:
              parent_node.right = leftmost

      return True

  
  def tranverse(self, node):
    tree = node.value
    if node.left == None:
      tree.left = None
    else:
      self.traverse(node.left)
    
    if tree.right == None:
      tree.right = None
    else:
      tree.right = self.traverse(node.right);
    return tree
     

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
t = tree.remove(15)

print(t)

s = tree.lookup(15)
print(s)
