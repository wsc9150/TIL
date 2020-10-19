# binary search
# 이진 검색
# 정렬되어 있는 배열에서 사용 가능
# 배열의 가운데 원소를 찾아 비교
# 검색하는 원소가 값이 더 작으면 앞쪽 범위, 더 크면 뒤쪽 범위에서 다시 가운데 원소를 찾아 비교
# 비교할 때마다 검색 범위가 반씩 줄어들게 된다. -> 선형 검색보다 빠른 검색 가능


def bin_search(a, key) :
    pl = 0              # 검색 범위의 맨 앞 원소 인덱스
    pr = len(a) - 1     # 검색 범위의 맨 끝 원소 인덱스

    while True :
        pc = (pl + pr) // 2     # 중앙 원소의 인덱스
        if a[pc] == key :
            return pc
        elif a[pc] < key :
            pl = pc + 1         # 검색 범위를 뒤쪽 절반으로 감소
        else :
            pr = pc - 1         # 검색 범위를 앞쪽 절반으로 감소

        if pl > pr :
            break

    return -1


if __name__ == '__main__' :
    x = [1, 2, 3, 5, 7, 8, 9]
    k = int(input('검색할 값을 입력하세요. : '))

    idx = bin_search(x, k)

    if idx == -1 :
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else :
        print(f'검색값은 x[{idx}]에 있습니다.')
