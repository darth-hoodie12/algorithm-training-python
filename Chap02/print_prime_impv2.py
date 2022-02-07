#   정수 2부터 1000까지 소수만 출력하는 함수
#   print_prime_impv.py의 불필요한 나눗셈을 하는 문제를 개선한 버전

def print_prime():
    cnt_d = 0 # 나눗셈 횟수를 세는 변수
    cnt_p = 0 # 찾은 소수를 세는 변수
    prime = [None] * 2 # 찾은 소수를 저장하는 리스트
    
    #소수 2를 초기값으로 입력
    prime[cnt_p] = 2
    cnt_p += 1

    #소수 3를 초기값으로 입력
    prime[cnt_p] = 3
    cnt_p += 1

    for i in range(5, 1001, 2):
    # 짝수는 모두 2로 나누어 떨어지기 때문에 범위에서 제외
        n = 1
        while prime[n] * prime[n] <= i:
            cnt_d += 2
            if (i % prime[n] == 0):
                break
            n += 1
        else:
            cnt_p += 1
            cnt_d += 1
            prime.append(i)
    
    for i in range(cnt_p):
        print(f'{prime[i]}')
    print(f'나눗셈은 총 {cnt_d}번 수행했습니다.')

if __name__ == '__main__':
    print_prime()