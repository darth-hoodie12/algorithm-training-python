from typing import Sequence

def reverse_array(A:Sequence) -> Sequence:
    length = len(A)
    for i in range(length//2):
        A[i], A[length - i - 1] = A[length - i - 1], A[i]
    return A

if __name__ == '__main__':
    print('입력한 숫자를 배열로 만든 후 거꾸로 출력합니다.')
    print('\'-q\'를 입력하시면 입력을 끝내고 출력을 시작합니다.')
    seq = []
    while True:
        number = input('입력하시오 : ')
        if(number == '-q'):
            break
        seq.append(number)
    
    print(f'{reverse_array(seq)}')
