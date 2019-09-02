def maxCrossingSum(arr,l,m,h,mod):
    #include elements on left to mid
    sm=0
    left_sum=-10000
    lmod_sum=0
    for i in range(m,l-1,-1):
        sm=sm+arr[i]
        if lmod_sum<sm%mod:
            lmod_sum=sm%mod
        if (sm>left_sum):
            left_sum=sm
    #include elements on right of mid
    sm=0
    right_sum=-10000
    rmod_sum=0
    for i in range(m+1,h+1):
        sm=sm+arr[i]
        if rmod_sum<sm%mod:
            rmod_sum=sm%mod
        if(sm>right_sum):
            right_sum=sm
    return lmod_sum+rmod_sum

def maxSubArraySum(arr,l,h,mod):
    if l==h:
        return arr[l]
    m=(l+h)//2
    return max(maxSubArraySum(arr,l,m,mod),
               maxSubArraySum(arr,m+1,h,mod),
               maxCrossingSum(arr,l,m,h,mod))

arr=[3,3,9,9,5]
mod=7
n=len(arr)
max_sum=maxSubArraySum(arr,0,n-1,mod)
print(max_sum)
