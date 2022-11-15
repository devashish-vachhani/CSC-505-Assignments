import heapq as heap

class Dijkstra:

    def Dijkstra_alg(self, n, e, mat, s):
        adj_list = {}
        for i in range(1, n+1, 1):
            adj_list[i] = set()
        for i in range(e):
            adj_list[mat[i][0]].add((mat[i][1], mat[i][2]))
            adj_list[mat[i][1]].add((mat[i][0], mat[i][2]))
            
        Q = []
        heap.heapify(Q)
        d = [1e9] * n
        d[s-1] = 0
        usp = [1] * n

        for i in range(1, n+1, 1):
            heap.heappush(Q, (d[i-1], i))
            
        while len(Q) != 0:
            du, u = heap.heappop(Q)
            for el in adj_list[u]:
                v = el[0]
                wt = el[1]
                if du + wt < d[v-1]:
                    d[v-1] = du + wt
                    heap.heappush(Q, (d[v-1], v))
                    usp[v-1] = 1
                elif du + wt == d[v-1]:
                    usp[v-1] = 0

        answer = []
        for i in range(1, n+1, 1):
            answer.append([d[i-1], usp[i-1]])
        return answer

