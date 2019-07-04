sa,sb=input().split()
ans=abs(len(sa)-len(sb))
def x_to_y(ans,sa,sb):
    for i in range(len(sa)):
        if len(sb)==1  and sb[i]==sa[i]:
            break
        if sa[i]!=sb[i]:
            ans+=1
    return ans
print(x_to_y(ans,sa,sb))
