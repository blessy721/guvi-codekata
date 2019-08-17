def longsub(string):
    st=0
    max_len=0
    start=0
    pos={}
    pos[string[0]]=0
    for i in range(1,len(string)):
        if string[i] not in pos:
            pos[string[i]]=i
        else:
            if pos[string[i]] >= st:
                currlen=i-st
                if max_len < currlen:
                    max_len=currlen
                    start=st
                st=pos[string[i]]+1
            pos[string[i]]=i
    if max_len < i-st:
        max_len=i-st
        start=st
    return string[start:start + max_len]

string=input()
print(len(longsub(string)))
