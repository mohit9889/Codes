def check(n, x, y, xx, yy, obs):
    a=n
    count=0
    while (x<=n and x>0 and y<=n and y>0) and ([x,y] not in obs):
        x+=xx
        y+=yy
        count+=1
    return count


def solve(n,k,x,y,obs):
    count=0
    count+=check(n, x+1, y, 1, 0, obs)
    count+=check(n, x-1, y, -1, 0, obs)
    count+=check(n, x, y-1, 0, -1, obs)
    count+=check(n, x, y+1, 0, 1, obs)
    count+=check(n, x+1, y-1, 1, -1, obs)
    count+=check(n, x+1, y+1, 1, 1, obs)
    count+=check(n, x-1, y-1, -1, -1, obs)
    count+=check(n, x-1, y+1, -1, 1, obs)
    print(count)

n,k=map(int, input().split())
q1,q2=map(int, input().split())
obs=[]
for i in range(k):
    obs.append(list(map(int, input().split())))
solve(n,k,q1,q2,obs)
