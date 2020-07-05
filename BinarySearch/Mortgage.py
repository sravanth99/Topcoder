import math
def monthlyPayment(loan,interest,term):
    monthlyrate = (((interest)/(10))/12)/100
    #print(monthlyrate)
    lo = 1
    hi = loan*(1000)
    while(lo<=hi):
        ok = True
        mid = lo + (hi-lo)//2
        cur = loan - mid
        t = 1
        while cur>0:
            extra = math.ceil(cur*(monthlyrate))
            cur += extra
            cur -= mid
            t +=1
            if cur > loan:
                lo = mid+1
                ok = False
                break
        #print(lo,hi,mid)
        if ok:
            if t <= (12*term):
                hi = mid-1
            else:
                lo = mid+1
    return lo

####################
print(monthlyPayment(1000,50,1))
print(monthlyPayment(2000000000, 6000, 1))