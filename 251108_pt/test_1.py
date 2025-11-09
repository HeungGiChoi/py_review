## 예제 1.
all_students = {
    "student_1": {
        "국어": 83,
        "영어": 92,
        "수학": 88
    },
    "student_2": {
        "국어": 90,
        "영어": 79,
        "수학": 86
    },
    "student_3": {
        "국어": 88,
        "영어": 86,
        "수학": 94
    }
}
while True:
    subject = input('평균값을 알고싶은 과목은?: ')
    if subject == "종료":
        print('평균값 구하기 프로그램을 종료합니다.')
        break
    avg_score = [score[subject] for score in all_students.values()]        
    print(f'{len(avg_score)}명의 {subject} 과목 평균은 {sum(avg_score) / len(avg_score):.2f}점 입니다.')
