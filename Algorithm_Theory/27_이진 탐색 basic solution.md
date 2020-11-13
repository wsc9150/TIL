# 이진 탐색 기초 문제 풀이

### 떡볶이 떡 만들기

- 오늘 동빈이는 여행 가신 부모님을 대신해서 떡집 일을 하기로 했습니다. 오늘은 떡볶이 떡을 만드는 날입니다. 동빈이네 떡볶이 떡은 재밌게도 떡볶이 떡의 길이가 일정하지 않습니다. 대신에 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰줍니다.
- 절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단합니다. 높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않습니다.
- 예를 들어 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면 자른 뒤 떡의 높이는 15, 14, 10, 15cm가 될 것입니다. 잘린 떡의 길이는 차례대로 4, 0, 0, 2cm입니다. 손님은 6cm만큼의 길이를 가져갑니다. 
- 손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하세요.

### 답안 예시 (Python)

```python
# 떡의 개수(N)와 요청한 떡의 길이(M)을 입력
n, m = map(int, input().split())

# 각 떡의 개별 높이 정보를 입력
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행 (반복적)
result = 0

while (start <= end) :
    total = 0
    mid = (start + end) // 2
    
    for x in array :
        # 잘랐을 때의 떡의 양 계산
        if x > mid :
            total += x - mid
    
    # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
    if total < m :
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
    else :
        # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        result = mid
        start = mid + 1

# 정답 출력
print(result)
```

### 답안 예시 (C++)

```c++
#include <bits/stdc++.h>

using namespace std;

// 떡의 개수(N)와 요청한 떡의 길이(M)
int n, m;

// 각 떡의 개별 높이 정보
vector<int> arr;

int main(void) {
    cin >> n >> m;
    
    for (int i = 0; i < n; i ++) {
        int x;
        cin >> x;
        arr.push_back(x)
    }
    
    // 이진 탐색을 위한 시작점과 끝점 설정
    int start = 0;
    int end = 1e9;
    
    // 이진 탐색 수행 (반복적)
    int result = 0;
    while (start <= end) {
        long long int total = 0;
        int mid = (start + end) / 2;
        
        for (int i = 0; i < n; i++) {
            // 잘랐을 때의 떡의 양 계산
            if (arr[i] > mid)
                total += arr[i] - mid;
        }
        
        // 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
        if (total < m)
            end = mid - 1;
        // 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
        else {
            // 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
            result = mid;
            start = mid + 1;
        }
    }
    
    cout << result << '\n';
}
```

### 답안 예시 (Java)

```java
public class Main {
    
    public static void main(String[] args) {
        // 이진 탐색을 위한 시작점과 끝점 설정
        int start = 0;
        int end = (int) 1e9;
        
        // 이진 탐색 수행 (반복적)
        int result = 0;
        
        while (start <= end) {
            long total = 0;
            int mid = (start + end) / 2;
            
            for (int i = 0; i < n; i++) {
                // 잘랐을 때의 떡의 양 계산
                if (arr[i] > mid)
                    total += arr[i] - mid
            }
            
            // 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
            if (total < m)
                end = mid - 1;
            // 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
            else {
                // 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
                result = mid;
                start = mid + 1;
            }
        }
        
        System.out.println(result);
    }
}
```

---

### 정렬된 배열에서 특정 수의 개수 구하기

- N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다. 이때 이 <u>수열에서 x가 등장하는 횟수를 계산</u>하세요. 예를 들어 수열 {1, 1, 2, 2, 2, 2, 3}이 있을 때 x = 2라면, 현재 수열에서 값이 2인 원소가 4개이므로 4를 출력합니다.
- 단, 이 문제는 시간 복잡도 **O(logN)**으로 알고리즘을 설계하지 않으면 **시간 초과** 판정을 받습니다. 

### 답안 예시 (Python)

```python
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_rnage(array, left_value, right_value) :
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

# 데이터의 개수 N, 찾고자 하는 값 x 입력
n, x = map(int, input().split())

# 전체 데이터 입력
array = list(map(int, input().split()))

# 값이 [x, x] 범위에 있는 데이터의 개수 계산
count = count_by_range(array, x, x)

# 값이 x인 원소가 존재하지 않는다면
if count == 0 :
    print(-1)
# 값이 x인 원소가 존재한다면
else :
    print(count)
```

### 답안 예시 (C++)

```c++
#include <bits/stdc++.h>

using namespace std;

// 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
int countByRange(vector<int>& v. int leftValue, int rightValue) {
    vector<int>::iterator rightIndex = upper_bound(v.begin(), v.end(), rightValue);
    vector<int>::iterator leftIndex = lower_bound(v.begin(), v.end(), leftValue);
    return rightIndex - leftIndex;
}

int n, x;
vector<int> v;

int main() {
    // 데이터의 개수 N, 찾고자 하는 값 x 입력
    cin >> n >> x;
    
    // 전체 데이터 입력
    for (int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        v.push_back(temp);
    }
    
    count = countByRange(v, x, x);
    
    // 값이 x인 원소가 존재하지 않는다면
	if (count == 0)
    	cout << -1 << '\n'
	// 값이 x인 원소가 존재한다면
	else :
    	cout << count << '\n';
    
    return 0;
}
```

