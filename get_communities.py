def get_communities(adj_list):
    total_nodes = len(adj_list)
    CS = {new_list: [] for new_list in range(total_nodes)}

    # Step 1: Initialize all nodes as unclassified
    label = {}
    for i in range(total_nodes):
        if i == 0:
            label[i] = -1
        else:
            label[i] = 0
    
    

    # Step 6: Repeat 2-6 until unclassified node set doesn't change


    def unclassafied_set(label):
        u_set = []
        for l in label:
            if label[l] == 0:
                u_set.append(l)
        return u_set


    while True:
        # print(label)
        community = []
        uus = unclassafied_set(label)
        

        # Step 2: Select the unclassified node v with largest degree and create community C labeled with l for it
        def max_unclassified_degree():
            mx = 0
            for l in label.values():
                if l != -1:
                    mx = max(l, mx)
            return mx 
        ll = max_unclassified_degree() + 1
        def max_degree_vertex_unclassified():
            mx = 0
            v = 0
            for l in label:
                if label[l] == 0:
                    length = len(adj_list[l])
                    if mx < length:
                        mx = length
                        v = l  
            return v
        v = max_degree_vertex_unclassified()
        community.append(v)

        # Step 3: Examine node v's unclassified neighbours to identify other seeds for the community C:
        
        def common_neighbour(u, v):
            cnt = 0
            for nu in adj_list[u]:
                for nv in adj_list[v]:
                    if nu == nv:
                        cnt = cnt + 1
            return cnt

        # For unclassified neighbours of v
        seed = {}
        for u in adj_list[v]:
            if label[u] == 0:
                cn = common_neighbour(u, v)
                val = max(common_neighbour(u,v)/len(adj_list[u]), common_neighbour(u,v)/len(adj_list[v]))
                seed[u] = val
        for s in seed:
            if seed[s]:
                label[s] = ll
                community.append(s)
        
        # For classified neighbours of v
        for u in adj_list[v]:
            if common_neighbour(u, v) >= len(adj_list[u])/2 or common_neighbour(u, v) >= len(adj_list[v])/2:
                label[u] = ll 
                if u not in community:
                    community.append(u)

        # Step 4: Expand community C by inserting nodes most of whose neighbours have been classified in C:

        def common_nodes(u, v):
            cnt = 0
            for node_u in u:
                for node_v in v:
                    if node_u == node_v:
                        cnt = cnt + 1
            return cnt

        while True:
            last_community_size = len(community)
            for w in community:
                for u in adj_list[w]:
                    if label[u] == 0:
                        if common_nodes(adj_list[u],community) >= len(adj_list[u])/2:
                            label[u] = ll 
                            if u not in community:
                                community.append(u)
            if last_community_size == len(community):
                break
        
        # Step 5: Insert community to CS
        if len(community) > 1:
            CS[ll] = community
            label[v] = ll


        if unclassafied_set(label) == uus:
            break
    

    # Step 7: Assign some of the unclassified nodes to the corresponding communities. For each of the neighbours if the number of its neighbors that have been classified in a certain community exceeds number of unclassified neighbors it is assigned to the community

    def most_frequent_classified_neighbor_label(u):
        dct = {}
        for neighbor in adj_list[u]:
            if label[neighbor] != 0:
                dct[label[neighbor]] = dct[label[neighbor]] + 1
        ans = 0
        for d in dct:
            if dct[d] > mx:
                mx = dct[d]
                ans = d 
        return ans


    unclassified = unclassafied_set(label)
    for u in unclassified:
        ll = most_frequent_classified_neighbor_label(u)
        if ll != 0:
            label[u] = ll
            CS[ll].append(u)



    # Step 8: Deal with very few unclassified nodes in the graph 

    unclassified = unclassafied_set(label)
    for u_node in unclassified:
        ll = ll + 1
        label[u] = ll
        new_community = []
        new_community.append(u)
        CS[ll] = new_community

        
    # Step 9: Return Community Structure
    return CS