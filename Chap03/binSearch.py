# Binary Search
## NOT WORK

from typing import Any, Sequence

def bin_search(seq: Sequence, key: Any) -> int:
    """ 이진 검색 방법으로 seq의 원소값 중 key와 같은 값이 있는 index를 반환 """
    #pl pc pr
    pl = 0
    pr = len(seq) - 1
    
    while True:
        pc = (pl + pr) // 2

        if (key == seq[pc]):
            return pc
        elif (key < seq[pc]):
            pr = pc - 1
        else:
            pl = pc + 1
        
        if pr < pl:
            break

        return -1

def bubble_sort(seq: Sequence) -> Sequence:
    length = len(seq)
    tmp = 0

    for i in range(length):
        for j in range(length):
            if(i != j and seq[i] < seq[j]):
                tmp = seq[j]
                seq[j] = seq[i]
                seq[i] = tmp

    return seq

if __name__ == '__main__':
    num = int(input('원소 수를 입력하시오 : '))
    seq = []

    for i in range(num):
        tmp = float(input(f'원소 값을 입력하시오 입력횟수는 {num - i}번 남았습니다. : '))
        seq.append(tmp)

    seq = bubble_sort(seq)
    print(f'{seq}')

    key = float(input('찾고 싶은 값을 입력하시오 : '))

    idx = bin_search(seq, key)

    if idx == -1:
        print(f'입력하신 {key}은/는 없는 값입니다.')
    else:
        print(f'입력하신 {key}은/는 {idx + 1}번째에 있습니다.')