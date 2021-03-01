INF = float('inf')

def bellManFord(n, m, node_dict, node, start):
    distance = {}
    
    for element in node:
        distance[element] = INF
    
    distance[start] = 0

    for _ in range(m-1): # 총 m-1번 반복
        for element in node_dict:
            for v, d in node_dict[element]:
                if distance[v] > distance[element] + d:
                    distance[v] = distance[element] + d
    
    for element in node_dict: # 가중치가 갱신되면 음의 사이클이 존재하는 경우
            for v, d in node_dict[element]:
                if distance[v] > distance[element] + d:
                    return -1
    
    return distance

def main():
    n, m = map(int, input().split()) # 정점, 간선
    node = list(input().split())
    node_dict = {}

    for i in range(n):
        node_dict[node[i]] = []

    for i in range(m):
        srt, dst, distance = input().split()
        distance = int(distance)
        node_dict[srt].append([dst, distance]) # ex) A, B, 10인 경우 A = [B, 10]과 같은 형태로 저장
    
    start = input() # 시작 정점

    result = bellManFord(n, m, node_dict, node, start)

    if result == -1:
        print("음의 사이클이 존재합니다!")
    else:
        for element in node:
            if result[element] != INF:
                print(result[element])
            else:
                print(-1)

if __name__ == "__main__":
    main()