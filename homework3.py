#1

# 삼각형의 세 변의 값 입력
a = float(input("a를 입력하시오."))
b = float(input("b를 입력하시오."))
c = float(input("c를 입력하시오."))

#일반삼각형
if a > b and a > c and a < b + c:
  print("삼각형이 됩니다.")
elif b > a and b > c and b < a + c:
  print("삼각형이 됩니다.")
elif c > a and c > b and c < a + b:
  print("삼각형이 됩니다.")

#정삼각형
elif a == b and a == c:
  print("정삼각형이 됩니다.")

#이등변삼각형
elif a == b and a + b > c:  
  print("이등변삼각형이 됩니다.")  
elif a == c and a + c > b:
  print("이등변삼각형이 됩니다.")
elif b == c and b + c > a:
  print("이등변삼각형이 됩니다.")

#삼각형이 아님
else:
  print("삼각형이 아닙니다.")


#2

a = int(input("a값을 입력하시오."))
b = int(input("b값을 입력하시오."))
c = input("연산자를 선택하시오.")

if c == "+":
  print(a + b)
elif c == "-":
  print(a - b)
elif c == "*":
  print(a * b)
elif c == "/":
  if b == 0:
    print("0으로 나눌 수 없습니다.")
  else:
    print(a / b)
elif c == "%":
  if b == 0:
    print("0으로 나눌 수 없습니다.")
  else:
    print(a % b)
elif c == "**":
  print(a ** b)
elif c == "//":
  if b == 0:
    print("0으로 나눌 수 없습니다.")
  else:
    print(a // b)
else:
  print("잘못된 연산자입니다.")