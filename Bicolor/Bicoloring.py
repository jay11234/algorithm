from Node import Node

class Bicoloring:

    @staticmethod
    def check_can_be_bicolored(incoming_list, edge_num):
        queue = list()

        for ver in incoming_list:
            ver.set_color_to_black()
            for ver2 in ver.adj_list:
                if ver2.get_color() == "white":
                    return "NOT BICOLORABLE."

        return "BICOLORABLE."

if __name__ == '__main__':
    adj_list = list()
    node_num = int(input())

    for x in range(0, node_num):
        node = Node(x)
        adj_list.append(node)

    edge_num = input()
    two_nodes = input()
    while two_nodes != "0":
        two_nodes = two_nodes.split(' ')
        a = int(two_nodes[0])
        b = int(two_nodes[1])
        adj_list[a].add_neighbor(adj_list[b])
        adj_list[b].add_neighbor(adj_list[a])
        two_nodes = input()

    bicoloring = Bicoloring()
    print(bicoloring.check_can_be_bicolored(adj_list, edge_num))
