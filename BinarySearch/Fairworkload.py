def FairWorkload(folders: list,workers:int)->int:
    n = len(A)
    lo = max(folders)
    hi = sum(folders)
    while (lo<hi):
        x = lo + ((hi-lo)//2)
        req = 1
        cur_folders = 0
        for i in range(n):
            if cur_folders+folders[i]<=x:
                cur_folders+=folders[i]
            else:
                req +=1
                cur_folders = folders[i]
        if req <= workers:
            hi = x
        else:
            lo = x+1
    return lo
if __name__ == '__main__':
    A = list(map(int,input().rstrip().split(' ')))
    N = int(input())
    print(FairWorkload(A,N))