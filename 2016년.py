#2016년
#Level 2
#2016년 1월 1일은 금요일입니다. 2016년 A월 B일은 무슨 요일일까요? 두 수 A,B를 입력받아 A월 B일이 무슨 요일인지 출력하는 getDayName 함수를 완성하세요. 요일의 이름은 일요일부터 토요일까지 각각
#SUN,MON,TUE,WED,THU,FRI,SAT
#를 출력해주면 됩니다. 예를 들어 A=5, B=24가 입력된다면 5월 24일은 화요일이므로 TUE를 반환하면 됩니다.

def getDayName(a,b):
    answer = 0
    countOfDay = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    dayName = {0:'THU', 1:'FRI', 2:'SAT', 3:'SUN', 4:'MON', 5:'TUE', 6:'WED'}
    i=1
    for i in range(1,a):
        answer += countOfDay[i]
    answer += b
    return dayName[answer%7]

#아래 코드는 테스트를 위한 출력 코드입니다.
print(getDayName(1,1))
print(getDayName(5,24))
