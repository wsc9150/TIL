# 1. 가장 큰 수
import operator


def solution1(numbers):
    answer = ''
    str_numbers = []
    str_numbers_re = []
    dict = {}

    # 배열의 수들을 문자열로 변환하여 새로운 리스트에 저장
    for i in numbers:
        str_numbers.append(str(i))

    # 배열의 수들을 비교하기 위해 4자리만큼 반복하여 딕셔너리에 저장
    # 인덱스를 기억하기 위해
    for i in range(len(str_numbers)):
        str_numbers_re.append((str_numbers[i] * 4)[:4])
        dict[i] = str_numbers_re[i]

    # 값을 기준으로 내림차순 정렬
    dict = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)

    for i in range(len(dict)):
        answer += str_numbers[dict[i][0]]

    return str(int(answer))


numbers = [3, 30, 34, 5, 9]
# print(solution1(numbers))



# 2. H-index
def solution2(citations):
    answer = 0

    citations.sort(reverse=True)
    # print(citations)

    answer = len(citations)

    for i in range(len(citations)):
        if citations[i] <= i:
            answer = i
            break

    return answer


citations = [3, 0, 6, 1, 5]
# print(solution2(citations))



# 3. 입국심사
# 이분탐색의 포인트는
# 어떤 것을 이분탐색할 것인지
# 기준은 무엇으로 잡을지
def solution3(n, times):
    answer = 0

    start = 1
    end = max(times) * n            # 가장 비효율적인 시간으로 설정

    while start <= end:
        people = 0
        mid = (start + end) // 2    # 최적값을 찾아가기 위해 가운데의 값을 구한다.

        for i in times:
            people += mid // i      # 가운데 값 만큼의 시간 안에 각 심사관들이 얼마나 많은 사람을 검사할 수 있는지 구한다.

        if people >= n:             # 목표 검사 인원수보다 많으면 시간이 널널하다는 뜻이므로 시간을 줄여본다.
            answer = mid
            end = mid - 1
        else:                       # 목표 검사 인원수보다 적으면 시간이 부족하다는 뜻이므로 시간을 늘여본다.
            start = mid + 1

    return answer


n = 6
times = [7, 10]
print(solution3(n, times))
