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
        if self.root == None:
            self.root = Node(data)

            self.tree.create_node(data, data)
            self.filaMostragem.append(data)
            self.filaMostragem.append(data)
            self.filaNodes.append(self.root)
            self.filaNodes.append(self.root)

            return

        node = Node(data)
        pai = self.filaNodes.popleft()

        if pai.left == None:
            pai.left = node
        else:
            pai.right = node

        self.filaMostragem.append(data)
        self.filaMostragem.append(data)
        self.tree.create_node(data, data, parent=self.filaMostragem.popleft())
        self.filaNodes.append(node)
        self.filaNodes.append(node)

    def inorder(self, Node):
        if Node.left is not None:
            self.inorder(Node.left)
        print(Node.data)
        if Node.right is not None:
            self.inorder(Node.right)

    def preorder(self, Node):
        print(Node.data)
        if Node.left is not None:
            self.preorder(Node.left)
        if Node.right is not None:
            self.preorder(Node.right)


    def postorder(self, Node):
        if Node.left is not None:
            self.postorder(Node.left)
        if Node.right is not None:
            self.postorder(Node.right)
        print(Node.data)

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

    def mostrarArvore(self):
        print('\n')
        self.inorder(self.root)
        print('\n')
        self.preorder(self.root)
        print('\n')
        self.postorder(self.root)
        print('\n')
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
