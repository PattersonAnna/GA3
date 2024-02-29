import math
#from collections import namedtuple
#Point = namedtuple('Point', ['x', 'y'])


def minimun_cost_connecting_edges(input_file_path, output_file_path):
    with open(input_file_path, 'r') as infile:
        rows = [l.replace('(', '').replace(')', '').split(',') for l in infile.readlines()]
        vertices = [(int(x), int(y)) for x, y in zip(*[iter(rows[0])] * 2)]
        edges = [(int(x), int(y)) for x, y in zip(*[iter(rows[1])] * 2)]






        manhatan_distance(vertices[0], vertices[3])
        #vertices = [Point(int(x), int(y)) for x, y in zip(*[iter(rows[0])] * 2)] 
        #edges = [Point(int(x), int(y)) for x, y in zip(*[iter(rows[1])] * 2)] 


def manhatan_distance(vertice_start, vertice_end):
    x_value_start, y_value_start = vertice_start
    x_value_end, y_value_end = vertice_end
    total_weigth = abs(x_value_start - x_value_end) + abs(y_value_start - y_value_end)
    return total_weigth
        


def main():
    minimun_cost_connecting_edges("Sample_Input.txt", "Sample_Output.txt")


if __name__ == "__main__":
    main()
    
