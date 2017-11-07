def minCost(matrix, m, n):
     sol = [[0 for i in range(0,m)] for i in range(n)]
     sol[0][0] = matrix[0][0]
     for i in range(1, m):
             sol[i][0] = sol[i-1][0] + matrix[i][0]
     for i in range(1, n):
             sol[0][i] = sol[0][i-1] + matrix[0][i]
     print(sol)
     for i in range(1,m):
             for j in range(1,n):
                     sol[i][j] = min(sol[i-1][j], sol[i][j-1], sol[i-1][j-1])+matrix[i][j]
     print(sol)
     print(sol[m-1][n-1])



cost = [[1, 2, 3],
         [4, 8, 2],
         [1, 5, 3]]

minCost(cost, 3,3)


class Graph:

    def __init__(self, rows, cols, g):
        self.ROW = rows,
        self.COL = cols,
        self.graph = g
        self.visited = [[False for i in range(self.COL)] for i in range(self.ROW)]

    def isSafe(self,i,j):
        return (i>=0 and i<self.ROW and j>=0 and j<self.COL and not self.visited[i][j] and graph[i][j])

    def DFS(self, i, j):
        indices_i = [-1,-1,-1,0,0,1,1,1]
        indices_j = [-1,0,1,-1,1,-1,0,1]
        print("visited of "+str(i)+" "+str(j)+": "+str(self.visited[i][j]))
        #visit all the cells around
        self.visited[i][j] = True
        for n in range(8):
            if self.isSafe(n+indices_i, n+indices_j):
                self.DFS(n+indices_i, n+indices_j)

    def findIslands(self):
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                if self.isSafe(i,j):
                    self.DFS(i,j)
                    count +=1
        return count



graph = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]]


row = len(graph)
col = len(graph[0])
 
g= Graph(row, col, graph)

print "Number of islands is :"
print g.findIslands()
