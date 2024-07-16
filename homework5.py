#1

# 각 학점 구간의 학생 수를 저장할 딕셔너리
grade_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}

# 10명의 성적을 입력 받음
scores = []
for i in range(10):
    score = int(input(f"학생 {i+1}의 성적을 입력하세요: "))
    scores.append(score)

# 각 점수를 학점 구간에 따라 분류
for score in scores:
    if score >= 90:
        grade_counts['A'] += 1
    elif score >= 80:
        grade_counts['B'] += 1
    elif score >= 70:
        grade_counts['C'] += 1
    elif score >= 60:
        grade_counts['D'] += 1
    else:
        grade_counts['F'] += 1

# 결과 출력
for grade, count in grade_counts.items():
    print(f"{grade}학점: {count}명")


#2

books = [
    {"도서명": "파이썬정복", "저자": "김상형", "가격": 22000},
    {"도서명": "점프 투 파이썬", "저자": "박응용", "가격": 18800},
    {"도서명": "파이썬코딩의 기술", "저자": "블렛슬라킨", "가격": 32000},
    {"도서명": "모두의 파이썬", "저자": "이승찬", "가격": 12000},
]

# 최저 가격을 찾기
min_price = float('inf')
min_price_author = ""
for book in books:
    if book["가격"] < min_price:
        min_price = book["가격"]
        min_price_author = book["저자"]
print(f"최저 가격의 책 저자: {min_price_author}")


#3

# 1. 클럽A에는 [축구, 야구, 농구] 종목이 있으며 배구와 골프가 신설되었다. 신설된 배구와 골프를 클럽A에 삽입하여라.
club_A = {"축구", "야구", "농구"}
new_sports_A = {"배구", "골프"}
club_A.update(new_sports_A)
print(f"1. 클럽A의 종목: {club_A}")

# 2. 클럽B에는 [축구, 핸드볼, 야구, 테니스, 족구] 종목이 있으며 핸드볼의 종목을 삭제하여라.
club_B = {"축구", "핸드볼", "야구", "테니스", "족구"}
club_B.discard("핸드볼")
print(f"2. 클럽B의 종목: {club_B}")

# 3. 클럽A에만 있는 종목을 출력하여라.
unique_to_A = club_A - club_B
print(f"3. 클럽A에만 있는 종목: {unique_to_A}")

# 4. 클럽B에만 있는 종목을 출력하여라.
unique_to_B = club_B - club_A
print(f"4. 클럽B에만 있는 종목: {unique_to_B}")

# 5. 클럽A와 클럽B의 모든 종목을 출력하여라.
all_sports = club_A | club_B
print(f"5. 클럽A와 클럽B의 모든 종목: {all_sports}")

# 6. 클럽A와 클럽B에 공통적으로 속하지 않은 종목을 출력하여라.
non_common_sports = club_A ^ club_B
print(f"6. 클럽A와 클럽B에 공통적으로 속하지 않은 종목: {non_common_sports}")
