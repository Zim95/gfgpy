'''
https://practice.geeksforgeeks.org/problems/print-adjacency-list/0
'''


class Graph:
    
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = dict([(i, []) for i in range(vertices)])
    
    def add_edge(self, vertex_a, vertex_b):
        self.adjacency_list[vertex_a].append(str(vertex_b))
        self.adjacency_list[vertex_b].append(str(vertex_a))

    def print_graph(self):
        for vertex, connections in self.adjacency_list.items():
            if (connections):
                print('{}-> {}'.format(str(vertex), '-> '.join(connections)))
            else:
                print('{}'.format(str(vertex)))


if __name__ == "__main__":
    test_cases = int(input())

    for _ in range(test_cases):
        vertices, edges = map(int, input().split(' '))
        graph = Graph(vertices)        
        for _ in range(edges):
            vertex_a, vertex_b = map(int, input().split(' '))
            graph.add_edge(vertex_a, vertex_b)
        graph.print_graph()
            
            