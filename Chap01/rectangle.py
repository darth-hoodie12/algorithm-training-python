#정수 넓이를 입력 받았을 때 정수로된 직사각형의 변들을 출력하는 프로그램

area = int(input('직사각형의 넓이를 입력하시오 : '))

for i in range(1, area + 1):
    if i * i > area:
        break
    elif area % i == 0:
        print(f'{i} x {area // i}')
