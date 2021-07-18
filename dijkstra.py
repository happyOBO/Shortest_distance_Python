
global_map = [[ 0,  2,  5,  1,  float('inf'),  float('inf')],
              [ 2,  0,  3,  2,  float('inf'),  float('inf')],
              [ 5,  3,  0,  3,  1,  5],
              [ 1,  2,  3,  0,  1,   float('inf')],
              [ float('inf'),  float('inf'),   1, 1,  0,  2],
              [ float('inf'),  float('inf'),  5,  float('inf'),  2,  0]]

class dijkstra:
    def __init__(self,size, start):
        # 노드의 개수
        self.size = size
        # 해당 인덱스의 노드를 이전에 방문했는지
        self.visited = [False for i in range(size)]
        # 지금까지 탐색했을 때 해당 start에서 해당 노드까지의 최단 거리
        self.distance = [float('inf') for i in range(size)]
        # 해당 인덱스의 노드의 부모 노드
        self.parent = [-1 for i in range(size)]
        self.start = start


    def get_small_index(self):
        min = float('inf')
        index = 0
        for i in range(self.size):
            if(self.distance[i] < min and not self.visited[i]):
                min = self.distance[i]
                index = i

        return index


    def calc_dijkstra(self):
        self.parent[self.start] = self.start
        for i in range(self.size):
            self.distance[i] = global_map[self.start][i]
            self.parent[i] = self.start

        # 자기 자신 방문
        self.visited[self.start] = True

        for i in range(self.size - 2):
            current = self.get_small_index()
            self.visited[current] = True
            for j in range(self.size):
                if(not self.visited[j]):
                    next_dist = self.distance[current] + global_map[current][j] 
                    
                    # 지금까지 탐색했던 노드의 최단 거리보다, 탐색한 거리가 더 작을 때
                    if(next_dist < self.distance[j]):
                        self.distance[j] = next_dist
                        self.parent[j] = current
    
    # 해당 노드의 부모 노드를 찾아서 역순으로 path 추적
    def find_path(self, end):
        current = end
        cost = 0
        path = []

        current = end
        path.append(current)
        cost += self.distance[current]

        while(self.start != current):
            current = self.parent[current]
            path.append(current)
            cost += self.distance[current]

        path.reverse()

        return cost , path



if __name__ == '__main__':
    dijkstra_path = dijkstra(6, 0)
    dijkstra_path.calc_dijkstra()
    
    for i in range(6):
        print(dijkstra_path.parent[i])


    print()

    for i in range(6):
        print(dijkstra_path.distance[i])

    cost , path = dijkstra_path.find_path(5)
    
    print("cost : ", cost)


    for i in range(len(path)):
        print(path[i])