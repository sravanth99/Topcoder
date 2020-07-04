class AutoLoan:
    def interestRate(self,price, monthlyPayment, loanTerm):
        lo = 1e-14
        hi = 100
        prev_lo = 0
        prev_hi = 0
        while(hi/lo>1+1e-14):
            #print(lo,hi)
            annual_interest = (hi+lo)/2
            t = 0
            cur = price
            while(True):
                net = cur + ((annual_interest/100)/12)*cur
                cur = net - monthlyPayment
                t +=1
                #print(t,cur)
                if t<loanTerm:
                    if round(monthlyPayment - (cur + ((annual_interest/100)/12)*cur),13)>0:
                        prev_lo = lo
                        lo = annual_interest
                        break
                elif t>= loanTerm:
                    if round(monthlyPayment - (cur + ((annual_interest/100)/12)*cur),13)>0:
                        prev_hi = hi
                        hi = annual_interest
                        break   
                    if cur>=price:
                        prev_hi = hi
                        hi = annual_interest
                        break               #print(t,'---',cur)
        #print(annual_interest,lo,hi)
        #print('this is it!')
        return lo