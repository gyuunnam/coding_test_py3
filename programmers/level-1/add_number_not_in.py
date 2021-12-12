#https://programmers.co.kr/learn/courses/30/lessons/86051?language=python3
def solution(numbers):
    answer = 0
    temp=set(numbers)
    for i in range(10):
        if i not in temp:
            answer+=i
    return answer