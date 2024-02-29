import math
#from collections import namedtuple
#Point = namedtuple('Point', ['x', 'y'])


def minimun_cost_connecting_edges(input_file_path, output_file_path):
    with open(input_file_path, 'r') as infile:
        rows = [l.replace('(', '').replace(')', '').split(',') for l in infile.readlines()]
        vertices = [(int(x), int(y)) for x, y in zip(*[iter(rows[0])] * 2)]
        edges = [(int(x), int(y)) for x, y in zip(*[iter(rows[1])] * 2)]
        print(vertices[1])

        #vertices = [Point(int(x), int(y)) for x, y in zip(*[iter(rows[0])] * 2)] 
        #edges = [Point(int(x), int(y)) for x, y in zip(*[iter(rows[1])] * 2)] 


def manhatan_distance(vertice_start, vertice_end):

    #total_weigth = 
        


def main():
    minimun_cost_connecting_edges("Sample_Input.txt", "Sample_Output.txt")


if __name__ == "__main__":
    main()
