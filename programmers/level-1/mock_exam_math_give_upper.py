def solution(array, commands):
    answer = []
    for com in commands:
        sub_arr=array[com[0]-1:com[1]]
        sub_arr.sort()
        answer.append(sub_arr[com[2]-1])
    return answer