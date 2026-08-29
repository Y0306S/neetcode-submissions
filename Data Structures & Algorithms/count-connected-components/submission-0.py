class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for i in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        visited = set()
        res = 0
        def dfs(node):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        for i in range(n):
            if i not in visited:
                dfs(i)
                res+=1
        return res
