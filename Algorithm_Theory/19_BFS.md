# BFS (Breadth-First Search)

- BFS는 **너비 우선 탐색**이라고도 부르며, 그래프에서 **가까운 노드부터 우선적으로 탐색하는 알고리즘**입니다.
- BFS는 **큐 자료구조**를 이용하며, 구체적인 동작 과정은 다음과 같습니다.
  1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 합니다.
  2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리합니다.
  3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복합니다.

### BFS 소스코드 예제 (Python)

```python
from collections import deque

# BFS 메소드 정의
def bfs(graph, start, visited) :
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    
    # 현재 노드를 방문 처리
    visited[start] = True
    
    # 큐가 빌 때까지 반복
    while queue :
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        
        print(v, end = ' ')
        
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True
                
# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
```

### BFS 소스코드 예제 (C++)

```c++
#include <bits/stdc++.h>

using namespace std;

bool visited[9];
vector<int> graph[9];

void bfs(int start) {
    queue<int> q;
    q.push(start);
    visited[start] = true;
    
    while (!q.empty()) {
        int x = q.front();
        q.pop();
        
        for (int i = 0; i < graph[x].size(); i++) {
            int y = graph[x][i];
            if (!visited[y]) {
                q.push(y);
                visited[y] = true;
            }
        }
    }
}

int main(void) {
    // 그래프 연결된 내용 생략
    // bfs(1)
    
    return 0;
}
```

### BFS 소스코드 예제(Java)

```java
import java.util.*;

public class Main {
    
    public static boolean[] visited = new boolean[9];
    public static ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();
    
    // BFS 함수 정의
    public static void bfs(int start) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(start);
        
        // 현재 노드를 방문 처리
        visited[start] = true;
        
        // 큐가 빌 때까지 반복
        while (!q.isEmpty()) {
            // 큐에서 하나의 원소를 뽑아 출력
            int x = q.poll();
            System.out.print(x + " ");
            
            for (int i = 0; i < graph.get(x).size(); i++) {
                int y = graph.get(x).get(i);
                
                if (!visited[y]) {
                    q.offer(y);
                    visited[y] = true;
                }
            }
        }
    }
    // 메인함수 생략
}
```

