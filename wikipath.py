import pandas as pd
import json
import matplotlib.pyplot as plt
import networkx as nx
import queue

def dijkstra(G, src, trg):
    path = []
    q = queue.Queue()
    
    nodes = list(G.nodes)
    
    sh_path = nx.shortest_path(G, source=src, target=trg, weight=None, method='dijkstra')
        
    visited = {}
    dist = dict.fromkeys(nodes, 1000000000) #init to inf
    pred = dict.fromkeys(nodes, -1)
    
    visited[src] = True #visit src
    path.append(src)
    
    dist[src] = 0
    q.put(src)
    
    while(not q.empty()):
        u = q.get()
        
        for adj_i in G.neighbors(u):
            
            if (adj_i not in visited):
                if (adj_i in sh_path):
                    path.append(adj_i)
                visited[adj_i] = True
                
                if u in sh_path or adj_i in sh_path:
                    path.append(adj_i)
                    
                dist[adj_i] = dist[adj_i] + 1
                pred[adj_i] = u
                q.put(adj_i)
                
                if (adj_i == trg):
                    return path
        
    return False

print("Booting up..")

infile = open("edges.json", "r")
edgyboy = json.load(infile)
infile.close()

G = nx.DiGraph(edgyboy)

rint("Welcome to the wikipedia speedrunner! Enter the source and destination articles and find out the least number of clicks needed to get there.\n")

while(1):
    p
    print("\n\nEnter e to exit")

    src = str(input("\nSource title: "))

    if (src == 'e'):
        exit()

    dest = str(input("\nDestination title: "))
    
    if (dest == 'e'):
        exit()

    try:
        sh_path = nx.shortest_path(G, source=src, target=dest, weight=None, method='dijkstra')
        
        print("Shortest path is : \n")
        for i in sh_path:
            print(i + "\n")
        
        print("\nGraphing...")
        
        x = dijkstra(G, "Autism", "Anarchism")
        
        subplot = G.subgraph(x)

        deg = subplot.degree
        
        new_subplot = [node[0] for node in deg if node[1] > 5 or node[0] in sh_path]

        new_subgraph = subplot.subgraph(new_subplot)
        
        color_map = []

        for node in new_subgraph.nodes():
            if node in sh_path:
                print(node)
                color_map.append('red')
            else:
                color_map.append('blue')
        
        nx.draw(new_subgraph, pos = nx.spring_layout(new_subgraph, k = 2), with_labels=True, font_size = 5, node_color = color_map, linewidths = 0.75)
        plt.savefig("graph.png", dpi = 3000)
        
        print("Graph saved to : ./graph.png")

    except Exception as e:
        print(e)
        
    
    

