import math

def minimun_cost_connecting_edges(input_file_path, output_file_path):
    with open(input_file_path, 'r') as infile:                                          
        rows = [l.replace('(', '').replace(')', '').split(',') for l in infile.readlines()]
        vertices = [(float(x), float(y)) for x, y in zip(*[iter(rows[0])] * 2)]
        edges = [(float(x), float(y)) for x, y in zip(*[iter(rows[1])] * 2)]
        graph = create_adjacency_matrix(vertices, edges)
        minimun_cost = minimun_graph_weight(graph)
    

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
        print("weight of path: ", weight_of_path[i], " current min: ", current_min, " visited: ", visited[i])
        if weight_of_path[i] < current_min and visited[i] == False:
            current_min = weight_of_path[i]                                      #check if next edges weight is less then the current 
            visited[i] = True                                                    #If it is it as the new min weight path and set it so it has been visited (don't want to repeat visiting vertices)
            current_vertices = i
    return current_vertices

def minimun_graph_weight(graph):
    num_vertices = len(graph)
    weight_of_path = [1000000000000] * num_vertices                              #used to store the the different weigth options
    current_path = [10000000000] * num_vertices                                #stores the current path with the shortest weight
    visited = [False] * num_vertices                                            #stores if a vertices has already been visited/ added to current path
    weight_of_path[0] = 0                                                       #intalizing with zero because the 0 -> 0 will have zero weight
    current_path = -1                                                           #first vertice in the tree us the start node -1


    for i in range(num_vertices):
        min_path = min_edge_weight(graph, weight_of_path, visited)
        visited[i] = True 
        print("min path: ", type(min_path), min_path)
        print("current path type: ", type(current_path), current_path)
        for j in range(num_vertices):
            if int(graph[i][j]) < min_path and visited[j] == False:
                weight_of_path[j] = graph[i][j]
                current_path[j] = min_path


    return num_vertices


    
def main():
    minimun_cost_connecting_edges("Sample_Input.txt", "Sample_Output.txt")

if __name__ == "__main__":
    main()
    
