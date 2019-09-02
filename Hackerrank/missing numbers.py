n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
a_arr=[0]*100
b_arr=[0]*100
minn=min(b)
for i in a:
    a_arr[i-minn]+=1
for i in b:
    b_arr[i-minn]+=1
for i in range(100):
    if a_arr[i]!=b_arr[i]:
        print(i+minn, end=" ")
