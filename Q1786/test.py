def get_pi(str):
    pi=[0]*8
    j=0
    for i in range(1,len(str)):
        while j>0 and str[i]!=str[j]:
            j = pi[j-1]
        if str[i]==str[j] :
            j=j+1
            pi[i]=j
    return pi

def kmp(str,substr):
    answer=[]
    pi = get_pi(substr)
    j=0
    m = len(substr)
    for i in range(0,len(str)):
        while j>0 and str[i]!=substr[j]:
            j = pi[j-1]
        if str[i]==substr[j]:
            if j==m-1:
                answer.append(i-m+1)
                j = pi[j]
            else:
                j=j+1
    return answer


str = input()
substr = input()
answer = kmp(str,substr)
print(len(answer))
for i in range(len(answer)):
    print(answer[i]+1,end=' ')
