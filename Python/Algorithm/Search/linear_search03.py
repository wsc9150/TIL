# 실수 검색


def seq_search(a, key) :
    for i in range(len(a)) :
        if a[i] == key :
            return i

    return -1


if __name__ == '__main__' :
    x = [12.7, 3.14, 6.4, 7.2]
    k = float(input('검색할 값을 입력하세요. : '))

    idx = seq_search(x, k)

    if idx == -1 :
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else :
        print(f'검색값은 x[{idx}]에 있습니다.')
