num = int(input('직각이등변삼각형의 한 변의 길이를 입력하시오 : '))

for i in range(num):
    for j in range(num - i):
        print(' ', end = '')
    print('*' * (i + 1))
