import heapq

def dijkstra(start, node_dict, node):
    INF = float('inf')
    distance = {}
    queue = []

    for element in node: # 모든 정점과의 거리를 INF로 초기화
        distance[element] = INF
    
    distance[start] = 0 # 시작 정점의 거리는 0
    
    heapq.heappush(queue, [start, 0]) # 힙에 [현재 노드, 거리] 형태로 push

    while queue:
        current_node = heapq.heappop(queue) # 힙에서 원소를 pop [현재 노드, 거리]
        for element in node_dict[current_node[0]]: # 현재 노드와 연결된 다른 노드들을 탐색
            if (distance[element[0]] > distance[current_node[0]] + element[1]): # 연결된 다른 노드의 distance와 현재 노드의 distance + 연결된 다른 노드의 거리를 비교
                distance[element[0]] = distance[current_node[0]] + element[1] # 더 작은 값으로 변경
                heapq.heappush(queue, [element[0], distance[element[0]]]) # 힙에 연결된 다른 노드와 distance를 push

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
        node_dict[dst].append([srt, distance]) # 무방향 그래프 (방향 그래프일 경우 해당 코드 불필요)
    
    start = input() # 시작 정점
    print(dijkstra(start, node_dict, node))

if __name__ == "__main__":
    main()
