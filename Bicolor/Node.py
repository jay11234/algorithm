class Node:

    def __init__(self, node_id):
        self.node_id = node_id
        self.adj_list = list()
        self._color = None

    def set_color_to_black(self):
        self._color = "black"

    def set_color_to_white(self):
        self._color = "white"

    def get_color(self):
        return self._color

    def add_neighbor(self, node):
        self.adj_list.append(node)
        self.sort_adj_list()

    def sort_adj_list(self):
        self.adj_list = sorted(self.adj_list, key=lambda x: x.node_id)

