import math, random
def fastPowering(g,a,p): #(g**a) % p
    def denToBin(x):
        result = [];
        while (x>0):
            result.append(x%2);
            x = x//2;
        return result;
    #print(denToBin(67))

    g=g%p;
    nA=denToBin(a);
    exponent = 0
    first=math
    gtmp = g
    ans = 1;
    for i in nA:
        if (i == 1):
            ans = (ans*gtmp)%p;
        exponent += 1;
        gtmp = (gtmp**2) % p;
    return ans

def inverseModulo(pX,pY):
    #Finding modulo inverse of pX (mod pY)
    x = pX+0;
    y=pY+0;
    prevx=[];
    prevy=[];
    counter = 0;
    dividends=[];
    b=0;
    while (x != 0 and y != 0 and counter < 100):
        prevx.append(x);
        prevy.append(y);
        if (x>y):
            b = x//y;
            x = x%y;
        else:
            b = y//x;
            y = y%x;
        dividends.append(b);
        counter += 1;
    
    hcf = max(x,y);
    if (hcf != 1):
        #return hcf
        return -1;
    else:
        dividends.pop();
        c=1
        d=-dividends[-1];
        if (prevy[-1] != 1):
            prevx, prevy = prevy, prevx; #we want prevy's last element to be 1.
        prevy.pop();
        replacement = True;
        result=0;
        for i in range(len(prevx)-2, -1, -1):
            if (replacement and i>0):
                c = c - d*dividends[i-1];
            elif (i>0):
                d = d - c*dividends[i-1];
            elif (i == 0):
                result = prevy[i]*c+prevx[i]*d;
            replacement = not replacement;
      
        if (prevy[0] == pY):
            if (result == 1 and d<0):
                d += pY;
            return d;
      
        elif (prevx[0] == pY):
            if (result == 1 and c<0):
                c += pY;
            return c;
        else:
            return -1
            #return (prevx[0], pY-1);
