# sentinel method
# 보초법
# 검색하고자 하는 키값을 배열의 맨 끝에 저장
# 이때 저장하는 값을 보초(sentinel)라고 한다.

import copy


def seq_search(seq, key) :
    a = copy.deepcopy(seq) # 배열 복제
    a.append(key)

    i = 0

    while True :
        # 검색값을 찾지 못했을 경우의 판단을 하지 않아도 된다.
        # 배열의 마지막에 검색값을 넣어줬기 때문에 반드시 찾게 된다.
        # if i == len(a) :
        #     return -1

        if a[i] == key :
            break

        i += 1

    # 못찾았을 경우의 판단을 if 하나로 단축 -> 종료조건 검사 비용을 반으로 줄이는 효과
    return -1 if i == len(seq) else i


if __name__ == '__main__' :
    x = [6, 4, 3, 2, 1, 2, 8]
    k = int(input('검색할 값을 입력하세요. : '))

    idx = seq_search(x, k)

    if idx == -1 :
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else :
        print(f'검색값은 x[{idx}]에 있습니다.')
