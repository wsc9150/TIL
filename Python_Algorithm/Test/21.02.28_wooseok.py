def solution1(new_id):
    answer = ''

    # 1단계
    new_id = new_id.lower()

    # 2단계
    temp_id = ''
    for i in new_id:
        if i.isalpha() or i.isdigit() or i in ['-', '_', '.']:
            temp_id += i

    new_id = temp_id

    # 3단계
    temp_id = ''
    isFlag = False

    for i in new_id :
        if i == '.' :
            isFlag = True
        else :
            if isFlag :
                temp_id += '.'
                isFlag = False
            temp_id += i

    new_id = temp_id

    if new_id :
        # 4단계
        if new_id[0] == '.':
            new_id = new_id[1:]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    else :
        # 5단계
        new_id = 'a'

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]

        if new_id[-1] == '.':
            new_id = new_id[:-1]
    # 7단계
    elif len(new_id) <= 2:
        s = new_id[-1]
        new_id += s * (3 - len(new_id))

    answer = new_id

    return answer


new_id = "...!@BaT#*..y.abcdefghijklm"
# print(solution1(new_id))


import itertools


def solution2(orders, course):
    answer = []

    menu_list = []

    for order in orders:
        menu_list.extend(order)

    menu_list = list(set(menu_list))
    menu_list.sort()

    for i in course:
        part = list(map(''.join, itertools.combinations(menu_list, i)))
        count_list = []

        for p in part:
            count = 0

            for order in orders:

                for k in p :
                    if k not in order :
                        break
                else :
                    count += 1

            count_list.append(count)

        _max = max(count_list)

        if _max <= 1 :
            continue
        else :
            for j in range(len(count_list)) :
                if count_list[j] == _max :
                    answer.append(part[j])

    answer.sort()

    return answer


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
print(solution2(orders, course))
