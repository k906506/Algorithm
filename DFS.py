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
        
    visit = []
    dfs(node, start, visit)
    print(*visit)
        
def dfs(node, start, visit):
    if start not in visit:    # 방문하지 않는 정점인 경우에
        visit.append(start)   # 해당 정점을 방문 처리하고
        for vertice in node[start]:    # 해당 정점과 연결된 다른 정점을 탐색
            dfs(node, vertice, visit)
    
if __name__ == "__main__":
    main()
