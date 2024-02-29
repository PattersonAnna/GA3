import math
#from collections import namedtuple
#Point = namedtuple('Point', ['x', 'y'])


def minimun_cost_connecting_edges(input_file_path, output_file_path):
    with open(input_file_path, 'r') as infile:
        rows = [l.replace('(', '').replace(')', '').split(',') for l in infile.readlines()]
        vertices = [(int(x), int(y)) for x, y in zip(*[iter(rows[0])] * 2)]
        edges = [(int(x), int(y)) for x, y in zip(*[iter(rows[1])] * 2)]
        print(vertices)
        print(edges)
        x = create_adjacency_matrix(vertices, edges)
        for row in x:
            print(row)
       
        #vertices = [Point(int(x), int(y)) for x, y in zip(*[iter(rows[0])] * 2)] 
        #edges = [Point(int(x), int(y)) for x, y in zip(*[iter(rows[1])] * 2)] 


def manhatan_distance(vertice_start, vertice_end):
    x_value_start, y_value_start = vertice_start
    x_value_end, y_value_end = vertice_end
    total_weigth = abs(x_value_start - x_value_end) + abs(y_value_start - y_value_end)
    return total_weigth

def create_adjacency_matrix(vertices, edges):
    num_vertices = len(vertices)
    adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]
    for i in range(num_vertices):
        for j in range(num_vertices):
            adjacency_matrix[i][j] = manhatan_distance(vertices[i], vertices[j])
    for edge in edges:
        edge_start, edge_end = edge
        adjacency_matrix[edge_start-1][edge_end-1] = 0
        adjacency_matrix[edge_end-1][edge_start-1] = 0



    return adjacency_matrix


def main():
    minimun_cost_connecting_edges("Sample_Input.txt", "Sample_Output.txt")


if __name__ == "__main__":
    main()
    
