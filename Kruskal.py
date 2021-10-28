class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = []
 
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
 
 
    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])
 
    def apply_union(self, parent, rank, x, y):
        xr = self.search(parent, x)
        yr = self.search(parent, y)
        if rank[xr] < rank[yr]:
            parent[xr] = yr
        elif rank[xr] > rank[yr]:
            parent[yr] = xr
        else:
            parent[yr] = xr
            rank[xr] += 1

    def triangle_matrix(self, matrix):
        pass
  
    def kruskal(self, vertex, matrix):
        
        
        result = []
        i, e = 0, 0
        
        #Сортирую рёбра в порядке возрастания их веса
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        
        #Выбераю край, имеющий минимальный вес, и
        #добавляю его к самому большому. Если ребро создает
        #цикл - идём к следующему
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.search(parent, u)
            y = self.search(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
                
        #переворачиваю результат, чтобы забить его в нижний треугольник матрицы
        for k in range(len(result)):
            result.append([result[k][1], result[k][0], result[k][2]])
        #print(result)

        #Нулевая матрица вывода
        arr = []
        for i in range(vertex):
            arr.append([0]*vertex)
            
        #Создание матрицы весов
        for k in result:
            arr[k[0]][k[1]] = k[2]

        #Вывод матрицы весов
        #print()
        print(f"   1  2  3  4  5")
        count = 1
        sum_ostov = 0
        for i in arr:
            print(count, i)
            count += 1
            for j in i:
                sum_ostov += j
        print(f"\nВеличина минимального остова: {int(sum_ostov/2)}")


matrix = [
    #  1   2   3   4   5 
    [  0,  0,  0,  1,  3],# 1
    [  0,  0,  3,  5,  4],# 2
    [  0,  3,  0,  0,  4],# 3
    [  1,  5,  0,  0,  2],# 4
    [  3,  4,  4,  2,  0],# 5
    ]


vertex = len(matrix)

g = Graph(vertex)

graph = []
triangle_index = 0
for i in range(vertex):
    for j in range(triangle_index, vertex):
        if matrix[i][j] != 0:
            graph.append( [i+1, j+1, matrix[i][j]] )
    triangle_index += 1


#print(graph)

for u, v, w in graph:
    g.add_edge(u-1, v-1, w)
    

g.kruskal(vertex, matrix)
