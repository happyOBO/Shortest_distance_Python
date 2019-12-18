# -*- coding: utf-8 -*- 
import Queue
# x축 길이
N = 3
# y축 길이
M = 5
# 시작 좌표
strt_x = 2
strt_y = 1
# 목적지 좌표
dst_x = 1
dst_y = 4
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
Dual_Cross = [(1,0),(1,4)]
Trip_Cross = [(1,1),(1,3)]
left_sign = [(0,-1,-1,0),(0,1,1,0),(-1,0,0,1),(1,0,0,-1)]
right_sign = [(0,-1,1,0),(0,1,-1,0),(-1,0,0,-1),(1,0,0,1)]
# 시작점에 대한 모든 노드의 최단거리 값 계산
def weight():
    # 맵에서 갈수 있는 곳은 1 못가는 곳은 0으로 표시
    arr = [[1,1,0,1,1],[1,1,1,1,1],[0,1,0,1,1]]
    q = Queue.Queue()
    # 맵 최단거리 값 누적 표시하는 check 생성
    check = [[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]]
    # 시작 초기화
    check[strt_x][strt_y] = 1
    q.put((strt_x,strt_y))
    # bfs 시작
    while (q.qsize() != 0):
        x = q.queue[0][0]
        y = q.queue[0][1]
        q.get()
        for i in range(4):
            xx = x + dir[i][0]
            yy = y + dir[i][1]
            if (xx < 0 or xx >= N or yy < 0 or yy >= M):
                continue
            # 못가는 곳이거나 이미 지나쳤던 곳이면 push 하지 않는다.
            if (arr[xx][yy] == 0 or check[xx][yy] != -1):
                continue

            # 옆 노드에서 조건에 맞는 상하 좌우 노드는 거리가 1 증가하면 갈수 있다.
            check[xx][yy] = check[x][y] + 1 
            # push
            q.put((xx, yy))
    return check

# 지정 목적지에 대한 순서리스트 만들기
def MakeOrder(check):
    # 초기화
    stack = []
    order = []
    check[strt_x][strt_y] = 1
    stack.append((strt_x,strt_y))
    # False로 초기화
    do_nothing = False
    while (len(stack) != 0):
        x = stack[-1][0]
        y = stack[-1][1]
        p = stack.pop()
        if(do_nothing):
            boundary_answer = check[p[0]][p[1]]
            boundary = order.pop()
            while(check[boundary[0]][boundary[1]] > boundary_answer):
                boundary = order.pop()
        order.append(p)

        # 아무것도 하지 않았을 때(dfs를 통해 계속 푸쉬했는데 결국 정답 길이 아니었다) True로 표시
        do_nothing = True
        # dfs 시작
        for i in range(4):
            xx = x + dir[i][0]
            yy = y + dir[i][1]
            if (xx < 0 or xx >= N or yy < 0 or yy >= M):
                continue
            if (check[xx][yy] == -1):
                continue
            # 지날수 있는 다음 노드 일 때
            if(check[xx][yy] == check[x][y] + 1 ):
                # 목적지와 같은 최단거리 가중치를 가지고 있는데 목적지가 아닐때 -- 정답길이 아니었다
                if(check[xx][yy] == check[dst_x][dst_y] and xx != dst_x and yy != dst_y):
                    continue
                # 정답길이었을때
                if((xx,yy) == (dst_x,dst_y)):
                    order.append((xx,yy))
                    return order
                stack.append((xx,yy))
                # 다음 노드를 추가했으므로 변수를 False 로 할당
                do_nothing = False
    return order


def AddDirectSimple(OrderList):
    DirectList = []
    for i in range(len(OrderList)):
        if( i < len(OrderList) -1):
            if(OrderList[i][0] == OrderList[i+1][0]):
                DirectList.append(OrderList[i])
                DirectList.append('right')
            else:
                DirectList.append(OrderList[i])
                DirectList.append('left')
    DirectList.append(OrderList[-1])
    return DirectList


def AddDirect(OrderList):
    DirectList = []
    i = 0
    while(i < len(OrderList)):
        if( i == 0 or i == len(OrderList) -1 or OrderList[i] == (1,2)):
            DirectList.append(OrderList[i])
        elif(OrderList[i] in Trip_Cross):
            if( 0 < i < len(OrderList) -1):
                if(OrderList[i - 1][0] == OrderList[i + 1][0] or OrderList[i - 1][1] == OrderList[i + 1][1]):
                    DirectList.append(OrderList[i])
                    DirectList.append('straight')
                else:
                    # print("Cross sign : ",OrderList[i-1] + OrderList[i+1])
                    x = OrderList[i][0]
                    y = OrderList[i][1]
                    sign_series = (OrderList[i-1][0] - x , OrderList[i-1][1] - y , OrderList[i+1][0] - x , OrderList[i+1][1] - y )
                    if(sign_series in left_sign):
                        DirectList.append(OrderList[i])
                        DirectList.append('left')
                    elif(sign_series in right_sign):
                        DirectList.append(OrderList[i])
                        DirectList.append('right')
                    else:
                        print("Exception error_1")
            else:
                print("Exception error_2")

        elif(OrderList[i] in Dual_Cross):
            x = OrderList[i][0]
            y = OrderList[i][1]
            sign_series = (OrderList[i-1][0] - x , OrderList[i-1][1] - y , OrderList[i+1][0] - x , OrderList[i+1][1] - y )
            if(0 < i < len(OrderList) -1):
                if(sign_series in left_sign):
                    DirectList.append(OrderList[i])
                    DirectList.append('left')
                elif(sign_series in right_sign):
                    DirectList.append(OrderList[i])
                    DirectList.append('right')
                else:
                    print("Exception error_3")
            else:
                print("Exception error_4")
        else:
            DirectList.append(OrderList[i])
            DirectList.append('right')
        i += 1
    return DirectList

check = weight()
OrderList = MakeOrder(check)
print("최단거리 맵")
for i in range(N):
    for j in range(M):
        print(check[i][j])
    print()
print("순서 리스트 ")
print(OrderList)
print("순서 및 방향 리스트")
print(AddDirect(OrderList))
