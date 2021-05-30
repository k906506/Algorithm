def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def union_parent(parents, x, y):
    x = find_parent(parents, x)
    y = find_parent(parents, y)

    if x == y: # 사이클이 발생한 경우
        return 1

    # 값이 작을수록 더 낮은 레벨의 노드
    if x > y:
        parents[x] = y # x의 부모 노드를 y로 바꿔준다.
    else:
        parents[y] = x # y의 부모 노드를 x로 바꿔준다.

    return 0 # 정상적으로 합쳐진 경우

def main():
    n, m = map(int, input().split())

    nodes = [[] for _ in range(n+1)] # 1 ~ n까지의 노드 정보를 저장할 리스트
    parents = [i for i in range(n+1)] # 부모노드를 저장할 리스트 -> 초기값은 자기 자신

    for _ in range(m):
        src, dst = map(int, input().split())
        nodes[src].append(dst)

    cycleCheck = False
    for i in range(1, n+1):
        for j in nodes[i]:
            if union_parent(parents, i, j) == 1:
                cycleCheck = True
                break

    if cycleCheck:
        print("사이클이 발생했습니다!")
    else:
        print(parents[1:])

if __name__ == "__main__":
    main()
