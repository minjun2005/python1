# 점수 입력 받기
records = []
for i in range(6):
    score = float(input(f"심판 {i+1}의 점수를 입력하세요: "))
    records.append(score)

# 총점 계산
max_score = max(records)
min_score = min(records)
total_score = sum(records) - max_score - min_score
# 결과 출력
print(f"총점 (최고점과 최저점을 제외한 점수의 합): {total_score}")