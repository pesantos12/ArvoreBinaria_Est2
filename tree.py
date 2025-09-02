from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_level_order(self, data): 
        if(self.root == None):
            self.root = Node(data)
            return
        f = deque()
        f.append(self.root)
        while(len(f) > 0):
            temp = f.pop()
            if(temp.left is None):
                temp.left = Node(data)
            else:
                f.append(temp.left) 
                

        
            
                        

        

    def inorder(self, node):
        # implementar
        pass

    def preorder(self, node):
        # implementar
        pass

    def postorder(self, node):
        # implementar
        pass

    def level_order(self):
        # implementar
        pass

    def is_perfect(self):
        # Retorna true se a árvore for perfeita
        pass

    def is_complete(self):
        # Retorna true se a árvore for completa
        pass

    def is_regular(self):
        # Retorna true se todos os nós tiverem 0 ou 2 filhos
        pass

    def is_balanced(self):
        # Retorna true se for balanceada
        pass

    def is_unbalanced(self):
        # Retorna true se não for balanceada
        pass



