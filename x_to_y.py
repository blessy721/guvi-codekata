st1,st2=input().split()
answ=abs(len(st1)-len(st2))
def x_to_y(ans,s1,s2):
    for i in range(len(s1)):
        if len(s2)==1  and s2[i]==s1[i]:
            break
        if s1[i]!=s2[i]:
            ans+=1
    return ans
print(x_to_y(answ,st1,st2))
