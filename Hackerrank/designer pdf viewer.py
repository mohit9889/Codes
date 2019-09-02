n=list(map(int, input().split()))
s=input()
length=len(s)
height=-1
for i in range(length):
    if n[ord(s[i])-ord('a')]>height:
        height=n[ord(s[i])-ord('a')]
print(length*height)
