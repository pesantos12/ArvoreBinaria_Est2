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
        self.fila = deque()
        self.root = None


    def addNode(self):
        i = None
        while(i != ""):
            i = input("\nDigite o valor do nó a ser inserido (Deixe vazio para encerrar):")
            if i != "":
                if len(self.tree) == 0:
                    self.tree.create_node(i, i)
                    self.fila.append(i)
                    self.fila.append(i)
                else:
                    self.fila.append(i)
                    self.fila.append(i)
                    self.tree.create_node(i, i, parent=self.fila.popleft())
            else:
                break







    def insert_level_order(self, data): #inserção automática por nível
        # implementar
        pass

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

    def mostrarArvore(self):
        print('\n')
        self.tree.show()



if __name__ == '__main__':
    arvore = BinaryTree()
    arvore.addNode()
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
