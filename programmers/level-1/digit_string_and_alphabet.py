#https://programmers.co.kr/learn/courses/30/lessons/81301
def solution(s):
    answer = ""
    nums={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    alpha=""
    for num in s:
        if num.isalpha():
            alpha+=num
            if alpha in nums.keys():
                answer+=str(nums[alpha])
                alpha=""
        else:
            answer+=str(num)
    return int(answer)