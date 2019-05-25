t = int(input())
list=[] #[총 시간, 시작시간, 끝나는 시간]
answer=0
for i in range(1,t+1):
    time = [int(str) for str in input().strip().split()]
    time.insert(0,time[1]-time[0])
    list.append(time)
list.sort()
time=[] #[{시작시간-끝나는시간},...]
for l in list:
    print("l: ",l," time: ",time)
    s1 = set(range(l[1],l[2]))
    print("s1: ",s1)
    if time:
        for t in time:
            if s1 & t:
                continue
            else:
                answer+=1
                time.append(s1)
                break
    else:
        answer+=1
        time.append(s1)
print(answer)
