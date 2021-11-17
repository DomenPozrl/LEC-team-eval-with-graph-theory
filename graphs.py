import networkx as nx
from process_data import process_data
import matplotlib.pyplot as plt

def construct_graph(data, show_fig=False):
    nodes = list(set([x for x, _, _ in data]))
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    
    edges = []
    
    for t1, t2, win in data:
        if win == t1:
            edges.append((t2, t1))
        else:
            edges.append((t1, t2))
    G.add_edges_from(edges)

    if show_fig:
        nx.draw(G, with_labels = True) 
        plt.show()

    return G

def page_rank_centrality(graph, alpha=0.1):
    results = nx.pagerank(graph, alpha=0.1)
    final_results = []
    for key in results:
        final_results.append((key, results[key]))

    sortirano = list(reversed(sorted(final_results, key=lambda x: x[1])))
    
    return {team: score for team, score in sortirano}

def degree_centrality(graph):
    results = nx.in_degree_centrality(graph)
    final_results = []
    for key in results:
        final_results.append((key, results[key]))

    sortirano = list(reversed(sorted(final_results, key=lambda x: x[1])))
    
    return {team: score for team, score in sortirano}


if __name__ == "__main__":
    train, test = process_data("data.txt")
    
    G = construct_graph(train)
    pgr = page_rank_centrality(G)
    deg = degree_centrality(G)

    pgr_c = 0
    deg_c = 0
    for t1, t2, winner in test:
        if winner == t1:
            if pgr[t1] > pgr[t2]:
                pgr_c += 1
        else:
            if pgr[t2] > pgr[t1]:
                pgr_c += 1
        
        if winner == t1:
            if deg[t1] > deg[t2]:
                deg_c += 1
        else:
            if deg[t2] > deg[t1]:
                deg_c += 1

    print(f"PageRank accuracy: {pgr_c/len(test)}, correct predictions: {pgr_c}")
    print(f"Degree centrality accuracy: {deg_c/len(test)}, correct predictions: {deg_c}")
        


