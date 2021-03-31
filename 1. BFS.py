def main():
    node = {}   # 그래프를 저장할 dict형 변수
    n, m, start = map(int, input().split())     # 정점의 개수, 간선의 개수, 시작 정점
    
    for i in range(n):
        node[i+1] = []
    
    for i in range(m):
        srt, dst = map(int, input().split())    # 시작 정점과 도착 정점
        node[srt].append(dst)   # 무방향 그래프이므로 양방향으로 저장
        node[dst].append(srt)
    
    for i in range(n):  # 오름차순으로 정렬 (위에서 3번 과정에 해당)
        node[i+1].sort()

    print(*bfs(node, start))
        
def bfs(node, start):
    visit = []
    queue = []
    
    queue.append(start)
    
    while queue:    # Queue에 원소가 없을 때까지 반복
        element = queue.pop(0)      # pop(0)를 이용하여 리스트를 Queue처럼 사용
        if element not in visit:    # 방문하지 않았을 경우 방문 리스트에 추가
            visit.append(element)
            queue.extend(node[element])     # 해당 정점과 연결된 다른 정점들을 Queue에 추가
    
    return visit
    
if __name__ == "__main__":
    main()
