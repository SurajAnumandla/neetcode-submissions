class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges:
            return []
        n = len(edges)
        parent = list(range(n+1))

        def find(x):
            while parent[x]!=x:
                x = parent[x]
            return x
        res = None
        for a,b in edges:
            fa = find(a)
            fb = find(b)

            if fa==fb:
                res = [a,b]
            parent[fa]=fb
        return res