#1
a = input("학과를 입력하세요:")
b = input("학번을 입력하세요:")
c = input("이름을 입력하세요:")
d = input("거주지를 입력하세요:")
print(a,b,c,d)
print('%s %s %s %s' %(a,b,c,d) )
print("{0},{1},{2},{3}".format(a,b,c,d))
print(f"{a},{b},{c},{d}")

#2
a = input("첫번째 정수를 입력하세요")
b = input("두번째 정수를 입력하세요")

a=int(a)
b=int(b)

print("{0}+{1}={2}".format(a,b,a+b))
print(f"{a}-{b}={a-b}")
