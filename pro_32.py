def sort_mat(m,n,mat):
    for list in mat:
        list.sort()
    for i in range(m-1):
        for j in range(n):
            if mat[i][j]>mat[i+1][j]:
                temp=mat[i][j]
                mat[i][j]=mat[i+1][j]
                mat[i+1][j]=temp
    print('\n'.join([' '.join([str(element) for element in list])for list in mat]))
m,n=map(int,input().split())
mat=list()
for i in range(m):
    mat.append(list(map(int,input().split())))
sort_mat(m,n,mat)
