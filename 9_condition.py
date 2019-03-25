'''조건문 예시
돈이 있으면 택시를 타고 돈이 없으면 걸어간다.

조건문 기본구조
if 조건문:
    실행할 문장1
elif 조건문:
    실행할 문장2
else:
    실행할 문장3
'''

money = True

if money:
    print("택시타자")

else:
    print("걸어가자")

# 택시타자

'''문제)
어떤 학생의 성적은 70점이다.
시험 합격의 기준은 60점이다.
60점이 넘으면 “합격입니다.”
60점 보다 낮으면 “불합격입니다.”
를 출력하세요.
'''

grade = 70

if grade >= 60:
    print("합격입니다.")

else:
    print("불합격입니다.")

# 불합격입니다.

'''문제)
어떤 학생의 성적은 60점이다.
성적이 70점이 이상일 경우 ‘A’를
성적이 50점 이상 70점 미만일 경우 ‘B’를
그 아래일 경우 ‘C’를 출력하세요.
'''

grade = 60

if grade >= 70:
    print('A')

elif grade >= 50:
    print('B')

else:
    print('C')

# B


'''문제)
한 학생은 시험에 합격했고
다른 학생은 시험에 불합격했다.
두 학생 모두 합격한 경우
“두 학생 모두 합격입니다.”를
둘 중 한 학생만 합격한 경우
“한 학생만 합격입니다.”를
두 학생 모두 불합격인 경우
“두 학생 모두 불합격입니다.”를 출력하세요.
'''

std1, std2 = True, False

if std1 and std2:
    print("두 학생 모두 합격입니다.")

elif std1 of std2:
    print("한 학생만 합격입니다.")

else:
    print("두 학생 모두 불합격입니다.")

# 한 학생만 합격입니다.
