graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

seen = [] # List to keep track of seen nodes.
queue = []     #Initialize a queue

def bfs(seen, graph, node):
  seen.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in seen:
        seen.append(neighbour)
        queue.append(neighbour)

# Driver Code
bfs(seen, graph, 'A')