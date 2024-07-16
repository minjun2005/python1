name=input("이름을 입력하세요:") 
age=input("생년월일을 입력하세요:")    
age= int(age[:4])
age2 = 2024-age + 1
print(name,"님은", age2,"세입니다.")
