from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    """ Sequence a에서 key값이 같은 원소의 인덱스(int) 반환 """
    length = len(a)

    for i in range(length):
        if a[i] == key:
            return i

    return -1

if __name__ == '__main__':
    num = int(input('원소 수를 입력하시오 : '))
    seq = []

    for i in range(num):
        tmp = float(input(f'원소 값을 입력하시오 입력횟수는 {num - i}번 남았습니다. : '))
        seq.append(tmp)
    
    key = float(input('찾고 싶은 값을 입력하시오 : '))

    idx = seq_search(seq, key)

    if idx == -1:
        print(f'입력하신 {key}은/는 없는 값입니다.')
    else:
        print(f'입력하신 {key}은/는 {idx + 1}번째에 있습니다.')