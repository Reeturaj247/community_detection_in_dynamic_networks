import networkx as nx
from convertGraph import AdjToNx
def modularity(graph, communities):
    comm = [set(c) for c in communities]
    return nx.community.modularity(graph, comm)


def conductance(graph, communities):
    conductances = []
    for community in communities:
        internal_edges = 0
        external_edges = 0
        for node in community:
            for neighbor in graph[node]:
                if neighbor in community:
                    internal_edges += 1
                else:
                    external_edges += 1
        if external_edges + 2*internal_edges == 0:
            conductance = 1.0
        else:
            conductance = external_edges / (external_edges + 2*internal_edges)
        conductances.append(conductance)
    return sum(conductances)/len(conductances)


def expansion(graph, communities):
    expansions = []
    for community in communities:
        internal_edges = 0
        external_edges = 0
        for node in community:
            for neighbor in graph[node]:
                if neighbor in community:
                    internal_edges += 1
                else:
                    external_edges += 1
        expansio = external_edges/len(community)
        expansions.append(expansio)
    return sum(expansions)/len(expansions)


def external_density(graph, communities):
    external_densities = []
    for community in communities:
        internal_edges = 0
        external_edges = 0
        for node in community:
            for neighbor in graph[node]:
                if neighbor in community:
                    internal_edges += 1
                else:
                    external_edges += 1
        k = len(community)
        if k == 1:
            print("Can't be calculated")
            return 0
        external_density = external_edges / (k * (k-1) / 2)
        external_densities.append(external_density)
    return sum(external_densities)/len(external_densities)

def calculate_measures_real(graph, communities):

    # modularity_g = modularity(graph, communities)
    # print("Modularity of The graph is: " + str(modularity_g))
    conductance_g = conductance(graph, communities)
    print("Conductance of the graph is: " + str(conductance_g))
    expansion_g = expansion(graph, communities)
    print("Expansion of the graph is: " + str(expansion_g))
    external_density_g = external_density(graph, communities)
    print("External Density of the graph is: " + str(external_density_g))