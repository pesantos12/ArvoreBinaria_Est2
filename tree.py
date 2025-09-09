import tkinter as tk
from tkinter import messagebox
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
    
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def exists(self, value):
        if not self.root:
            return False
        q = deque([self.root])
        while q:
            node = q.popleft()
            if node.data == value:
                return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False

    def insert_level_order(self, data):
        if self.exists(data):
            raise ValueError(f"Valor {data} já existe na árvore")

        if self.root is None:
            self.root = Node(data)
            return
        
        f = deque([self.root])
        
        while f:
            temp = f.popleft()
            
            if temp.left is None:
                temp.left = Node(data)
                break
            else:
                f.append(temp.left)

            if temp.right is None:
                temp.right = Node(data)
                break
            else:
                f.append(temp.right)


    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.data] + self.inorder(node.right)

    def preorder(self, node):
        if node is None:
            return []
        return [node.data] + self.preorder(node.left) + self.preorder(node.right)

    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.data]

    def level_order(self):
        if not self.root:
            return []
        q = deque([self.root])
        res = []
        while q:
            node = q.popleft()
            res.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res


    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def is_perfect(self):
        h = self.height(self.root)
        return self.count_nodes(self.root) == (2**h - 1)

    def is_complete(self):
        if not self.root:
            return True
        q = deque([self.root])
        end = False
        while q:
            node = q.popleft()
            if node:
                if end:
                    return False
                q.append(node.left)
                q.append(node.right)
            else:
                end = True
        return True

    def is_regular(self):
        def check(node):
            if node is None:
                return True
            if (node.left is None) ^ (node.right is None):
                return False
            return check(node.left) and check(node.right)
        return check(self.root)

    def is_balanced(self):
        def check(node):
            if node is None:
                return 0, True
            hl, bl = check(node.left)
            hr, br = check(node.right)
            return 1 + max(hl, hr), bl and br and abs(hl - hr) <= 1
        return check(self.root)[1]

    def is_unbalanced(self):
        return not self.is_balanced()


class Interface:  
    def __init__(self, root):
        self.arvore_binaria = BinaryTree()
        self.root = root
        self.root.title("Árvore Binária")

        self.entrada = tk.Entry(root)
        self.entrada.pack()

        self.botao_inserir = tk.Button(root, text="Inserir", command=self.adicionar_valor)
        self.botao_inserir.pack()

        self.status_label = tk.Label(root, text="Árvore: nenhuma")
        self.status_label.pack()

        self.texto_percursos = tk.Text(root, height=10, width=40)
        self.texto_percursos.pack()

        self.botao_inorder = tk.Button(root, text="Mostrar Inorder", command=lambda: self.mostrar_percurso("inorder"))
        self.botao_inorder.pack()

        self.botao_preorder = tk.Button(root, text="Mostrar Preorder", command=lambda: self.mostrar_percurso("preorder"))
        self.botao_preorder.pack()

        self.botao_postorder = tk.Button(root, text="Mostrar Postorder", command=lambda: self.mostrar_percurso("postorder"))
        self.botao_postorder.pack()

        self.botao_levelorder = tk.Button(root, text="Mostrar Level Order", command=lambda: self.mostrar_percurso("level"))
        self.botao_levelorder.pack()

        self.botao_desenhar = tk.Button(root, text="Desenhar Árvore", command=self.desenhar_arvore)
        self.botao_desenhar.pack()

    def atualizar_status(self):
        status = []
        if self.arvore_binaria.is_perfect():
            status.append("Perfeita")
        if self.arvore_binaria.is_complete():
            status.append("Completa")
        if self.arvore_binaria.is_regular():
            status.append("Regular")
        if self.arvore_binaria.is_balanced():
            status.append("Balanceada")
        if self.arvore_binaria.is_unbalanced():
            status.append("Desbalanceada")

        self.status_label.config(text="Árvore: " + ", ".join(status) if status else "Árvore: vazia")

    def adicionar_valor(self):
        try:
            valor = int(self.entrada.get())
            self.arvore_binaria.insert_level_order(valor)
            self.atualizar_status()
            self.desenhar_arvore()  
        except ValueError:
            messagebox.showerror("Erro", "Insira um valor válido")

    def mostrar_percurso(self, tipo):
        if tipo == "inorder":
            valores = self.arvore_binaria.inorder(self.arvore_binaria.root)
        elif tipo == "preorder":
            valores = self.arvore_binaria.preorder(self.arvore_binaria.root)
        elif tipo == "postorder":
            valores = self.arvore_binaria.postorder(self.arvore_binaria.root)
        else:
            valores = self.arvore_binaria.level_order()

        self.texto_percursos.delete(1.0, tk.END)
        self.texto_percursos.insert(tk.END, f"{tipo}: {valores}\n")

    def desenhar_arvore(self):
        if not self.arvore_binaria.root:
            return

        plt.close('all')
        G = nx.DiGraph()

        def add_edges(node, x=0, y=0, layer=1):
            if node is None:
                return
            G.add_node(node.data, pos=(x, y))
            if node.left:
                G.add_edge(node.data, node.left.data)
                add_edges(node.left, x - 1 / layer, y - 1, layer + 1)
            if node.right:
                G.add_edge(node.data, node.right.data)
                add_edges(node.right, x + 1 / layer, y - 1, layer + 1)

        add_edges(self.arvore_binaria.root)
        pos = nx.get_node_attributes(G, 'pos')

        plt.figure(figsize=(8, 5))
        nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=10, font_weight="bold")
        plt.show()


if __name__ == "__main__":
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()
