graph = {"A":["D","C","B"],
   "B":["E"],
   "C":["G","F"],
   "D":["H"],
   "E":["I"],
   "F":["J"]}
def dfs_non_recursive(graph, source):
       seen = []
       stack = [source]
       while(len(stack) != 0):
           s = stack.pop()
           if s not in seen:
               seen.append(s)
           if s not in graph:
               continue
           for neighbor in graph[s]:
               stack.append(neighbor)
       return " ".join(seen)
DFS_seen = dfs_non_recursive(graph, "A")
print(DFS_seen)