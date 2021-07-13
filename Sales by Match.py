#------------Sales by Match------------
def sockMerchant(n, ar):
    #----------------------------------
    num=[ar[0]]
    for i in range(len(ar)):
        if (ar[i] in num):
            continue
        else:
            num.append(ar[i])
    #----------------------------------
    sum=[]
    for i in range(len(num)):
        sum.append(0)
    for i in range(len(num)):
            for j in range(len(ar)):
                if (num[i]==ar[j]):
                    sum[i]+=1
    #----------------------------------
    res=0
    for i in range(len(sum)):
        if (sum[i]%2==0):
            res+=sum[i]/2
        else:
            if((sum[i]-1)%2==0 and sum[i]!=0):
                res+=(sum[i]-1)/2
    #----------------------------------
    return int(res)

if __name__ == '__main__':
    print("Sales by Match")
    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)
