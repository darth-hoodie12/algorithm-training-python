#  정수 2부터 1000까지 소수만 출력하는 함수

def print_prime():
    cnt = 0
    for i in range(2, 1001):
        for j in range(2, i):
            cnt += 1
            if (i % j == 0):
                break
        else:
            print(i)
    print(f'나눗셈은 총 {cnt}번 수행했습니다.')

if __name__ == '__main__':
    print_prime()