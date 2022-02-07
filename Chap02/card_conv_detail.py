def convert_str(x:int, r:int) -> str:
    """ 10진수인 정수 x를 r진수로 변환한 문자열을 반환하며 그 과정을 출력 """

    conv_str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rt_str = ''
    #length = len(str(x))
    
    print(f'{r}진수로 변환을 시작합니다.')
    print(f'{r} | {x:4}')
    print(f'     -------')
    while x > 0:
        print(f'{r} | {x//r:4} ... {conv_str[x % r]}')
        print(f'  +------')
        rt_str += conv_str[x % r]
        x = x // r
    
    return rt_str[::-1]

if __name__ == '__main__':
    """ 10진수를 n진수로 변환 """

    while True:
        x = int(input('음이 아닌 10진수 정수를 입력하시오 : '))
        if x > 0:
            break
    
    while True:
        n = int(input('변환하고싶은 진수로 2와 32사이의 값을 입력하시오 : '))
        if n >=2 and n <=32:
            break
    
    print(f'{x}를 {n}진수로 변환한 값은 {convert_str(x, n)}입니다.')