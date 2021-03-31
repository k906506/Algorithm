INF = float('inf')

def main():
    n, m = map(int, input().split())
    distance = [[INF for _ in range(n+1)] for _ in range(n+1)]

    for i in range(m):
        src, dst, cost = map(int, input().split())
        if distance[src][dst] > cost: # 이미 간선 정보가 주어진 정점일 때
            distance[src][dst] = cost
    
    for i in range(1, n+1):
        distance[i][i] = 0

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if distance[i][k] + distance[k][j] < distance[i][j]: # 거쳐가는 길이 더 작은 길일때 갱신
                    distance[i][j] = distance[i][k] + distance[k][j]
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if distance[i][j] == INF: # 갈 수 없는 경우 0으로
                print(0, end = " ")
            else:
                print(distance[i][j], end = " ")
        print("")

if __name__ == "__main__":
    main()