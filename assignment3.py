import math

def minimun_cost_connecting_edges(input_file_path, output_file_path):
    with open(input_file_path, 'r') as infile:                                          
        rows = [l.replace('(', '').replace(')', '').split(',') for l in infile.readlines()]
        vertices = [(float(x), float(y)) for x, y in zip(*[iter(rows[0])] * 2)]
        edges = [(float(x), float(y)) for x, y in zip(*[iter(rows[1])] * 2)]
        graph = create_adjacency_matrix(vertices, edges)
        minimun_cost = minimun_graph_weight(graph)
        total_weight = correct_weight(minimun_cost)
    with open(output_file_path, 'w') as outfile:
        outfile.write(f'{int(total_weight)}\n')
    

def manhatan_distance(vertice_start, vertice_end):
    x_value_start, y_value_start = vertice_start
    x_value_end, y_value_end = vertice_end
    total_weigth = abs(x_value_start - x_value_end) + abs(y_value_start - y_value_end)
    return total_weigth

def create_adjacency_matrix(vertices, edges):
    num_vertices = len(vertices)
    adjacency_matrix = [[0.0] * num_vertices for _ in range(num_vertices)]
    for i in range(num_vertices):
        for j in range(num_vertices):
            adjacency_matrix[i][j] = manhatan_distance(vertices[i], vertices[j])
    for edge in edges:
        edge_start, edge_end = edge
        adjacency_matrix[int(edge_start-1)][int(edge_end-1)] = 0.1
        adjacency_matrix[int(edge_end-1)][int(edge_start-1)] = 0.1

    return adjacency_matrix

def min_edge_weight(graph, weight_of_path, visited):
    num_vertices = len(graph)
    current_min = 10000000000000
    for i in range(num_vertices):
        if weight_of_path[i] < current_min and visited[i] == False:
            current_min = weight_of_path[i]                                      #check if next edges weight is less then the current 
            current_vertices = i
    return current_vertices

def minimun_graph_weight(graph):
    num_vertices = len(graph)
    weight_of_path = [1000000000000] * num_vertices                              #used to store the the different weigth options
    visited = [False] * num_vertices                                            #stores if a vertices has already been visited/ added to current path
    weight_of_path[0] = 0                                                       #intalizing with zero because the 0 -> 0 will have zero weight

    for i in range(num_vertices):
        min_weight = min_edge_weight(graph, weight_of_path, visited)
        visited[i] = True 
        for j in range(num_vertices):
            if graph[i][j] > 0 and visited[j] == False and weight_of_path[j] > int(graph[i][j]):
                weight_of_path[j] = graph[i][j]

    return weight_of_path

def correct_weight(minimun_cost):
    total = len(minimun_cost)
    sum = 0
    for i in range(total):
        if minimun_cost[i] == 0.1:
            minimun_cost[i] = 0
    for i in range(total):
        sum += minimun_cost[i]

    return sum

    
def main():
    minimun_cost_connecting_edges("Sample_Input.txt", "Sample_Output.txt")

if __name__ == "__main__":
    main()
    
