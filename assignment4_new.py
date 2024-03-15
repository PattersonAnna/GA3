from collections import defaultdict

neg = '~'

# directed graph class
#  adapted from:
#  src: https://www.geeksforgeeks.org/generate-graph-using-dictionary-python/
class dir_graph:
    def __init__(self):
        # create an empty directed graph, represented by a dictionary
        #  The dictionary consists of keys and corresponding lists
        #  Key = node u , List = nodes, v, such that (u,v) is an edge
        self.graph = defaultdict(set)
        self.nodes = set()

    # Function that adds an edge (u,v) to the graph
    #  It finds the dictionary entry for node u and appends node v to its list
    # performance: O(1)
    def addEdge(self, u, v):
        self.graph[u].add(v)
        self.nodes.add(u)
        self.nodes.add(v)

    # Function that outputs the edges of all nodes in the graph
    #  prints all (u,v) in the set of edges of the graoh
    # performance: O(m+n) m = #edges , n = #nodes
    def print(self):
        edges = []
        # for each node in graph
        for node in self.graph:
            # for each neighbour node of a single node
            for neighbour in self.graph[node]:
                # if edge exists then append
                edges.append((node, neighbour))
        return edges

# 2-CNF class
#  Class storing a boolean formula in Conjunctive Normal Form of literals
#  where the size of clauses is at most 2
#  -NOTATION-
#    The CNF is represented as a list of lists
#    e.g [[x, y], [k, z]] == (x or y) and (k or z)
#    i.e Conjunction of inner lists , where the inner lists are disjunctions
#    of literals
#    Negation is represented with ~ .  ~x == negation of literal x
# class two_cnf:
class two_cnf:
    def __init__(self):
        self.con = []

    # adds a clause to the CNF
    # performance O(1)
    def add_clause(self, clause):
        if len(clause) <= 2:
            self.con.append(clause)
        else:
            print("error: clause contains > 2 literals")

    # returns a set of all the variables in the CNF formula
    def get_variables(self):
        vars = set()
        for clause in self.con:
            for literal in clause:
                vars.add(literal)
        return vars

    def print(self):
        print(self.con)

#Our Code
class Light:
    def __init__(self, light_num, on_or_off, switch_nums):
        self.light_num = light_num
        self.on_or_off = on_or_off
        self.switch_nums = switch_nums

# helper function that applies the double negation rule to a formula
#   the function removes all occurrences ~~ from the formula
def double_neg(formula):
    return formula.replace((neg+neg), '')

# Function that performs Depth First Search on a directed graph
# O(|V|+|E|)
def DFS(dir_graph, visited, stack, scc):
    for node in dir_graph.nodes:
        if node not in visited:
            explore(dir_graph, visited, node, stack, scc)

# DFS helper function that 'explores' as far as possible from a node
def explore(dir_graph, visited, node, stack, scc):
    if node not in visited:
        visited.append(node)
        for neighbour in dir_graph.graph[node]:
            explore(dir_graph, visited, neighbour, stack, scc)
        stack.append(node)
        scc.append(node)
    return visited

# Function that generates the transpose of a given directed graph
# Performance O(|V|+|E|)
def transpose_graph(d_graph):
    t_graph = dir_graph()
    # for each node in graph
    for node in d_graph.graph:
        # for each neighbour node of a single node
        for neighbour in d_graph.graph[node]:
            t_graph.addEdge(neighbour, node)
    return t_graph

# Function that finds all the strongly connected components in a given graph
# Implementation of Kosaraju’s algorithm
# Performance O(|V|+|E|) for a directed graph G=(V,E)
# IN : directed graph, G
# OUT: list of lists containing the strongly connected components of G
def strongly_connected_components(dir_graph):
    stack = []
    sccs = []
    DFS(dir_graph, [], stack, [])
    t_g = transpose_graph(dir_graph)
    visited = []
    while stack:
        node = stack.pop()
        if node not in visited:
            scc = []
            scc.append(node)
            explore(t_g, visited, node, [], scc)
            sccs.append(scc)
    return sccs

# Function that finds a contradiction in a list of strong connected components
# if [a , b , ~a,  c, a] is a connected component then the function returns T
# since a -> ~a -> a exists
# sccs = Strongly Connected Components
#   It is a list of lists representing the connected components
def find_contradiction(sccs):
    for component in sccs:
        for literal in component:
            for other_literal in component[component.index(literal):]:
                if other_literal == double_neg(neg + literal):
                    return True
    return False

# Function that determines if a given 2-CNF is Satisfiable or not
def two_sat_solver(two_cnf_formula):
    # setup the edges of the graph
    # G = (V,E) , V = L U ~L where L = set of variables in 2-CNF
    # E =
    # {(~u,v),(~v,u) | for all clauses [u,v] } U {(~u,u) | for all clauses [u]}
    graph = dir_graph()
    for clause in two_cnf_formula.con:
        if len(clause) == 2:
            u = clause[0]
            v = clause[1]
            graph.addEdge(double_neg(neg+u), v)
            graph.addEdge(double_neg(neg+v), u)
        else:
            graph.addEdge(double_neg(neg+clause[0]), clause[0])
    if not find_contradiction(strongly_connected_components(graph)):
        return "yes"
    else:
        return "no"


#Our code
def can_turn_off_lights(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as infile:
            lines = [l.replace('***\n', 'problem').replace('\n', '').split(',') for l in infile.readlines()]

            # holds problem 1 info 
            problem1 = []
            problem1Lights = []
            problem1Connections = []

            #holds problem 2 info
            problem2 = []
            problem2lights = []
            problem2connections = []
            length = len(lines)

            #iterates through list, problem 1
            j = 0 
            x = 0
            x += 1
            j += 1
            problem1.append(lines[x])
            x += 1
            j += 1
            problem1Lights.append(lines[x])
            x += 1
            j += 1
            while lines[x][0] != 'problem':
                problem1Connections.append(lines[x])
                x += 1
                j += 1

            #iterates through list, problem 2
            j += 1
            problem2.append(lines[j])
            j += 1
            problem2lights.append(lines[j])
            j +=  1
            while j != length:
                problem2connections.append(lines[j])
                j += 1

        if int(problem1[0][0]) <= 1:
             with open(output_file_path, 'w') as outfile:
                 outfile.write(f'{"no"}\n')
                 outfile.write(f'{format_input(problem2, problem2lights, problem2connections)}\n')
                 return
        if int(problem2[0][0]) <= 1:
             with open(output_file_path, 'w') as outfile:
                 outfile.write(f'{"no"}\n')
                 return

    except Exception as exception:
        print(exception)
    with open(output_file_path, 'w') as outfile:
        outfile.write(f'{format_input(problem1, problem1Lights, problem1Connections)}\n')
        outfile.write(f'{format_input(problem2, problem2lights, problem2connections)}\n')
    pass

def format_input(problem1, problem1Lights, problem1Connections):
    light_map = []
    light_connection = []
    num_switches = int(problem1[0][0])
    num_light = int(problem1[0][1])
    for x in range(num_light):
        for i in range(num_switches):
            num_light_in_switch = len(problem1Connections[i])
            for j in range(num_light_in_switch):
                if int(problem1Connections[i][j]) == x+1:
                    light_connection.append(i+1)
                    
    for a in range(num_light):
        if a == 0:
            light_map.append(Light(a+1,int(problem1Lights[0][a]), [light_connection[a], light_connection[a+1]]))
        else:
            temp = a+1*a
            light_map.append(Light(a+1,int(problem1Lights[0][a]), [light_connection[temp], light_connection[temp+1]]))

    return create_clauses(light_map)

def create_clauses(light_map):
    formula = two_cnf()
    for light in light_map:
        if light.on_or_off == 1:
            formula.add_clause([str(light.switch_nums[0]), str(light.switch_nums[1])])
            formula.add_clause(['~'+ str(light.switch_nums[0]), '~'+str(light.switch_nums[1])])
        else:
            formula.add_clause([str(light.switch_nums[0]), "~" +  str(light.switch_nums[1])])
            formula.add_clause(["~" + str(light.switch_nums[0]), str(light.switch_nums[1])])

    return two_sat_solver(formula)

def main():
    can_turn_off_lights("Sample_Input.txt", "Sample_Output.txt")


if __name__ == "__main__":
    main()
