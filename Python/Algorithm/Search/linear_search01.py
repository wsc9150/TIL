# linear search
# 선형 검색
# 직선 모양으로 늘어선 배열에서 검색하는 경우
# 원하는 키값을 가진 원소를 찾을 때 까지 맨 앞부터 스캔하여 순서대로 검색하는 알고리즘
#  = 순차 검색 (sequential search)


def seq_search(a, key) :
    i = 0

    while True :
        if i == len(a) :    # 검색값을 찾지 못하고 배열의 맨 끝 인덱스를 지나간 경우
            return -1

        if a[i] == key :
            return i

        i += 1


if __name__ == '__main__' :
    x = [6, 4, 3, 2, 1, 2, 8]
    k = int(input('검색할 값을 입력하세요. : '))

    idx = seq_search(x, k)

    if idx == -1 :
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else :
        print(f'검색값은 x[{idx}]에 있습니다.')
