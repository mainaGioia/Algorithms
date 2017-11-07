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
