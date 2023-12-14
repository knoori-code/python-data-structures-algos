class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])        

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
    

new_graph = Graph()

new_graph.add_vertex('A')
new_graph.add_vertex('B')
new_graph.add_vertex('C')
new_graph.add_vertex('D')

new_graph.add_edge('A', 'B')
new_graph.add_edge('A', 'C')
new_graph.add_edge('A', 'D')

new_graph.add_edge('B', 'D')
new_graph.add_edge('C', 'D')

new_graph.print_graph()
print('\n')

new_graph.remove_vertex('D')

new_graph.print_graph()