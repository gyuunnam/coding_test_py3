def checktr(time,li):
    c=0
    start=time
    end=time+1000
    for i in li:
        if i[1] >= start and i[0] < end:
            c += 1
    return c

def solution(lines):
    li=[]
    r=1
    for line in lines:
        year,time,sec=line.split()
        time=time.split(':')
        sec=float(sec.replace('s',''))*1000
        end=(int(time[0])*3600 + int(time[1])*60 + float(time[2]))*1000
        start=end-sec+1
        li.append([start,end])
    for i in li:
        r=max(r,checktr(i[0],li),checktr(i[1],li))
    return r