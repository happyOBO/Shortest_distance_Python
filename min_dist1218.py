# -*- coding: utf-8 -*- 
import Queue

# 시작점에 대한 모든 노드의 최단거리 값 계산
def weight(strt_pos, dst_pos):
    dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    # x축 길이
    N = 3
    # y축 길이
    M = 5
    # 시작 좌표
    (strt_x,strt_y) = strt_pos
    # 목적지 좌표
    (dst_x,dst_y) = dst_pos
    # 맵에서 갈수 있는 곳은 1 못가는 곳은 0으로 표시
    arr = [[1,1,0,1,1],[1,1,1,1,1],[1,1,0,1,1]]
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
def MakeOrder(strt_pos, dst_pos,check):
    dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    # x축 길이
    N = 3
    # y축 길이
    M = 5
    # 시작 좌표
    (strt_x,strt_y) = strt_pos
    # 목적지 좌표
    (dst_x,dst_y) = dst_pos
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

def AddDirect_complicated(NEWSList):
    s = [('N','N'),('E','E'),('W','W'),('S','S')]
    l = [('N','W'),('E','N'),('W','S'),('S','E')]
    r = [('N','E'),('E','S'),('W','N'),('S','W')]
    t = [('N','S'),('E','W'),('W','E'),('S','N')]
    i = 0
    DirectList = []
    while(i < len(NEWSList) - 1):
        NEWStuple = (NEWSList[i],NEWSList[i+1])
        
        if (NEWStuple in s):
            DirectList.append(4) # straight
        if(NEWStuple in l):
            DirectList.append(3) # left
        if(NEWStuple in r):
            DirectList.append(2) # right
        if(NEWStuple in t):
            DirectList.append(5) # turn
        i +=1
    return DirectList

def AddNEWS(strtNEWS,OrderList):
    NEWS = [strtNEWS]
    i = 0
    while(i < len(OrderList)-1):
        x = OrderList[i][0]
        y = OrderList[i][1]
        sign_series = (OrderList[i+1][0] - x , OrderList[i+1][1] - y )
        if ((x,y) == (1,2)):
            pass
        elif (sign_series == (1,0)):
            NEWS.append('N')    
        elif (sign_series == (0,-1)):
            NEWS.append('E')
        elif (sign_series == (0,1)):
            NEWS.append('W')     
        elif (sign_series == (-1,0)):
            NEWS.append('S')
        else :
            print("Exception error_5")
        i += 1
    return NEWS

# 함수화
def navigator(strtNEWS, strt_pos, dst_pos):
    check = weight(strt_pos, dst_pos)
    for i in range(3):
        for j in range(5):
            print check[i][j] ,
        print '\n',
    OrderList = MakeOrder(strt_pos, dst_pos,check)
    NEWSList = AddNEWS(strtNEWS,OrderList)
    DirectList = AddDirect_complicated(NEWSList)

    # 중간 다리 제거
    if( (1,2) in OrderList ):
        OrderList.remove((1,2))
    return OrderList,DirectList,NEWSList

Order,Direct,NEWS = navigator('N',(2,4),(2,0))

print("Order List")
print(Order)
print("Action List")
print(Direct)
print("NEWS List")
print(NEWS)