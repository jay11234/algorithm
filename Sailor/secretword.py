from __future__ import print_function
from vertex import Vertex
import sys
import enchant


def print_anagram(prefix, word):
    if len(word) == 1:
        dict = enchant.Dict("en_US")
        output = prefix+''.join(word)
        if dict.check(output):
            print(output)

    else: ## 8 words              fdsafdsa+     r *8
        for a in range(len(word)):
            new_pre = prefix + word[a]
            rest = word[:a]+word[a+1:]
            print_anagram(new_pre, rest)

    ## abcd
    ## newpre= a
    ## rest =bcd
    ## rainb, ow
    ## 8*8 .....8
    ## ra+inbow
    ## inbow
    ## arinbo w
class ShortestPath:

    @staticmethod
    def find_the_shortest_path(vertex_list):

        group_number = 0
        queue = list()
        for xxx in range(0, len(vertex_list)):
            read = vertex_list[xxx]
            if read.status != 1:
                queue = [vertex_list[xxx]]
                group_number = group_number + 1
            while len(queue) > 0:
                current = queue.pop(0)
                current.group = group_number
                if current.is_undiscovered():
                    vertex_list[current.vertex_id].set_discovered()
                    for neighbor in vertex_list[current.vertex_id].adj_list:
                        if neighbor.is_undiscovered:
                            neighbor.set_discovered()
                            queue.append(neighbor)
                            neighbor.group = group_number


        # according to the group number make a list to count
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        word_list = list()
        count = 0
        for i in range(1, group_number+1):
            for xx in vertex_list:
                if xx.group == i:
                    count = count+1

            if count != 0:
                word_list.append(alphabet[count-1])
            count = 0

        ## print anagram
        word = ''.join(word_list)
        prefix =''
        print_anagram(prefix, word)








if __name__ == '__main__':

    from_vertex = None
    to_vertex = None
    vertex_list = list()

    read_line = sys.stdin.readline()
    vertex_number = int(read_line)
    for x in range(0, vertex_number):
        vertex = Vertex(x)
        vertex_list.append(vertex)

    edge_number = sys.stdin.readline()
    edge_number = edge_number.rstrip('\n')

    while edge_number != '':
        edge_number = edge_number.split(' ')
        from_vertex = int(edge_number[0])
        to_vertex = int(edge_number[1])
        vertex_list[from_vertex].add_neighbor(vertex_list[to_vertex])
        vertex_list[to_vertex].add_neighbor(vertex_list[from_vertex])
        edge_number = sys.stdin.readline()
        edge_number = edge_number.rstrip('\n')
        #edge_number = re.split("\s+", edge_number)


    shortest_path = ShortestPath()
    shortest_path.find_the_shortest_path(vertex_list)


