print("세 정수의 최댓값을 구합니다.")
a = int(input("정수 a의 값을 입력하시오 : "))
b = int(input("정수 b의 값을 입력하시오 : "))
c = int(input("정수 c의 값을 입력하시오 : "))

max_value = a
if b > max_value:
    max_value=b
if c > max_value:
    max_value=c

print(f"MAX VALUE IS {max_value}.")
