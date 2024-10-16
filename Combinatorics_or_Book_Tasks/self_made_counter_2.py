a=input().split()
ans=dict.fromkeys(a,0)
for i in a:
    ans[i]+=1
print(ans)