import heapq

def dijkstra(start, node_dict, node):
    INF = float('inf')
    distance = {}
    visit = {}
    queue = []

    for element in node: # 모든 정점과의 거리를 INF로 초기화
        distance[element] = INF
    
    distance[start] = 0 # 시작 정점의 거리는 0
    
    for element in node: # 방문 노드를 확인하기 위한 visit 변수 초기화
        visit[element] = False

    heapq.heappush(queue, [0, start]) # 힙에 [거리, 현재 노드] 형태로 push

    while queue:
        current_node = heapq.heappop(queue) # 힙에서 원소를 pop [거리, 현재 노드] 형태

        if (visit[current_node[1]] == True): # 이미 방문한 노드인 경우 탐색 X
            continue

        for element in node_dict[current_node[1]]: # 현재 노드와 연결된 다른 노드들을 탐색
            if (distance[element[0]] > distance[current_node[1]] + element[1]): # 연결된 다른 노드의 distance와 현재 노드의 distance + 연결된 다른 노드의 거리를 비교
                distance[element[0]] = distance[current_node[1]] + element[1] # 더 작은 값으로 변경
                heapq.heappush(queue, [distance[element[0]], element[0]]) # 힙에 distance와 연결된 다른 노드를 push
        
        visit[current_node[1]] = True # 방문 노드 표시

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
    print(dijkstra(start, node_dict, node))

if __name__ == "__main__":
    main()
