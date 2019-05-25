import copy
global N, result
result=0

def queens(answer, n): # answer은 인덱스(col)에 대한 row 위치
    global result

    if len(answer)==n:
        result+=1
        '''
        for i in range(n):
            for j in range(n):
                if j==answer[i]:
                    print(1, end=' ')
                else:
                    print(0, end=' ')
            print()
        print()
        '''
        return

    temp = list(range(n)) # 현재 col에 대한 row 후보 배열
    for i in range(len(answer)): # 0 ~ 현재위치 col
        if answer[i] in temp:
            temp.remove(answer[i]) # temp에서 answer에 이미 있는 row 제거
        dist = len(answer)-i
        if answer[i] + dist in temp:
            temp.remove(answer[i]+dist)
        if answer[i] - dist in temp:
            temp.remove(answer[i]-dist)
    if len(temp)!=0:
        sol = copy.deepcopy(answer) #리스트의 값만 복사
        for i in temp:
            answer = copy.deepcopy(sol) #리스트의 값만 복사
            answer.append(i)
            queens(answer,n)
    else:
        return

N = int(input())
for i in range(N):
        queens([i],N)
print(result)
