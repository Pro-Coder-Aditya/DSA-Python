graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = [] # list for visited nodes
queue = []

def BreadthFirstSearch(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:            # creating queue to visit each node
        m = queue.pop(0)    # m -> current node
        print(m, end= " -> ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("Following is the BreadthFirstSearch")
BreadthFirstSearch(visited, graph, "5")
