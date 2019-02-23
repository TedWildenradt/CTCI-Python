from collections import deque
def IsTrusted(node, trustGraph, pretrustedPeers, trustThreshold):

    if node in pretrustedPeers:
        return True
    
    queue = deque()
    queue.append((node,0))
    visited = set()
    visited.add(node)
    
    while queue:
        curr = queue.popleft()
        for i in range(len(trustGraph[curr[0]])):
            if trustGraph[curr[0]][i] > 0:
                if i in pretrustedPeers and (trustGraph[curr[0]][i] + curr[1] <= trustThreshold):
                    return True
                else:
                    if i not in visited:
                        visited.add(i)
                        queue.append((i,trustGraph[node][i] + curr[1]))
                    
    return False

IsTrusted(0,[[0,1,0],[1,0,1],[3,2,0]],[2,3],2)


'''
Your task is to check whether a given node within a trust graph is considered trusted or not, and return true of false accordingly.

A node is considered trusted if it has a trust distance of trustedDistance or less from any pre-trusted peer in the graph. Trust distance is calculated by finding a shortest path between two nodes, measured by summing up all of the edge weights specified in trustGraph. Pre-trusted peers are specified using an array of pre-trusted peer indices in prestrustedPeers.

Notes:

The trustGraph is represented by an NxN symmetric adjecency matrix where edge weights are represented by positive integers. The lack of an edge is represented with a 0 value.
The trust graph can contain cycles.
If node itself is listed in the pretrustedPeers array, then it is trusted.
Inputs and Outputs:

[execution time limit] 4 seconds (py3)

[input] integer node

The index of the node that you want to check whether it's trusted or not.

[input] array.array.integer trustGraph

The graph of trust relationships between nodes, represented as an adjacency matrix. This graph is symmetric and can contain loops. A value of 0 indicates no edge between nodes, and a positive value represents the trust edge weight.

[input] array.integer pretrustedPeers

List of pre-trusted peers

[input] integer trustThreshold

The max trust distance from a pre-trusted peer to be considered trusted.

[output] boolean

Whether node is considered trusted or not (ie whether it has a trust distance that is less than or equal to trustThreshold, from a node in pretrustedPeers.
'''