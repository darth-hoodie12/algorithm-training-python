from max import max_of

print('입력받은 숫자들의 최대값을 출력합니다.')
print('-q 을 입력하시면 종료됩니다.')

val = []
index = 0

while True:
    numbers = input('입력하시오 : ')
    if(numbers == '-q'):
        break
    val.append(int(numbers))

print(f'{len(val)}개 입력하셨습니다.')
print(f'최대값은 {max_of(val)}입니다.')