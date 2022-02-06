from typing import Any, Sequence

# 매개변수 seq의 자료형은 Sequence이며 임의의 자료형(Any)을 반환한다.
def max_of(seq: Sequence) -> Any:
    """시퀀스형 a 원소의 최대값을 반환"""
    maximum = seq[0]
    for i in range(len(seq)):
        if maximum < seq[i]:
            maximum = seq[i]
    
    return maximum

# __name__ 은 모듈 이름이며
# 스크립트 프로그램이 직접 실행될 때 __name__에는 '__main__'을 대입한다.
# 스크립트 프로그램이 import 되었을 때의 __name__은 원래의 모듈 이름이다.
    #이 파일을 예로 들자면 max.py 가 다른 프로그램에 import 되었을 경우
    #max라는 모듈의 __name__은 max가 된다.
if __name__ == '__main__':
    print('배열 X의 최대값을 구합니다.')
    num = int(input('배열의 크기를 입력하세요 : '))
    X = [None] * num

    for i in range(num):
        X[i] = int(input(f'X[{i}]의 값을 입력하세요 : '))
    
    print(f'배열 X의 최대값은 {max_of(X)}입니다.')