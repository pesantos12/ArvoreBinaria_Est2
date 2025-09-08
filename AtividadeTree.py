from treelib import Tree
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.tree = Tree()
        self.filaMostragem = deque()
        self.filaNodes = deque()
        self.root = None

    def insert_level_order(self, data):
        No = Node(data)

        if self.root is None:
            self.root = No
            self.tree.create_node(data, data) 
            return

        fila = deque([self.root])
        
        while True:
            pai = fila.popleft()

            if pai.left is None:
                pai.left = No
                self.tree.create_node(data, data, parent=pai.data)
                break
            else:
                fila.append(pai.left)

            if pai.right is None:
                pai.right = No
                self.tree.create_node(data, data, parent=pai.data) 
                break  
            else:
                fila.append(pai.right)

    def inorder(self, Node):
        if Node.left is not None:
            self.inorder(Node.left)
        print(Node.data, end=" ")
        if Node.right is not None:
            self.inorder(Node.right)

    def preorder(self, Node):
        print(Node.data, end=" ")
        if Node.left is not None:
            self.preorder(Node.left)
        if Node.right is not None:
            self.preorder(Node.right)


    def postorder(self, Node):
        if Node.left is not None:
            self.postorder(Node.left)
        if Node.right is not None:
            self.postorder(Node.right)
        print(Node.data, end=" ")

    def level_order(self):
        if self.root is None:
            return

        nodes_queue = deque([self.root])

        while len(nodes_queue) > 0:
            current_node = nodes_queue.popleft()

            print(current_node.data, end=" ")

            if current_node.left is not None:
                nodes_queue.append(current_node.left)
            
            if current_node.right is not None:
                nodes_queue.append(current_node.right)

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

    def mostrarArvore(self):
        print('\n')
        print("In-Order: ", end=" ")
        self.inorder(self.root)
        print("\nPré-Ordem: ", end=" ")
        self.preorder(self.root)
        print("\nPós-Ordem: ", end=" ")
        self.postorder(self.root)
        print("\nLevel-Order: ", end=" ")
        self.level_order()
        print("\n")
        self.tree.show()



if __name__ == '__main__':
    arvore = BinaryTree()
    arvore.insert_level_order(1)
    arvore.insert_level_order(2)
    arvore.insert_level_order(3)
    arvore.insert_level_order(4)
    arvore.insert_level_order(5)
    arvore.insert_level_order(6)

    arvore.mostrarArvore()




"""
    tree.create_node("n1", "n1", data=20)

    tree.create_node("n2", "n2", parent="n1", data=10)
    tree.create_node("n3", "n3", parent="n1", data=30)
    tree.create_node("n4", "n4", parent="n2", data=40)
    print(f"Tree size: {tree.size()}")           # Number of nodes
    print(f"Tree depth: {tree.depth()}")         # Maximum depth
    print(f"Root node: {tree.root}")             # Root identifier
    print(f"Is empty: {len(tree) == 0}")         # Empty check"""
