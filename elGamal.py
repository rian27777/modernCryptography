import math, random;
tableFormat = '{:^45}|{:^45}|{:^45}';
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
            return -1;

def theElGamal():
    #document.getElementById("console").innerHTML = '';
    message = input("Enter the message: ").lower(); #a string; like: "the tea in Nepal is vey hot"
    print(tableFormat.format('Computer A', 'comm. channel', 'Computer B'));
    print('-'*123);
    messageNum = 0;
    for char in range(len(message)):
        messageNum += '#abcdefghijklmnopqrstuvwxyz'.find(message[char])*(27**char);
    print(tableFormat.format(f'(encode {message})', '', ''));    
    #print(f'Cool - we\'re sending {message} (which is {messageNum} as a number).\n');
    print(tableFormat.format(f'm={messageNum}', '', ''))
    p = 2**127 - 1; #2147483647;
    g = random.randint(2,p-1); 
    a = 6767;
    if (messageNum>p):
        print(f'Message is too long. Try again.');
        return False
    
    #print(f'Public values are g: {g} and the prime: {p}\n');
    print(tableFormat.format('', f'g={g}', ''));
    print(tableFormat.format('', f'p={p}', ''));
    
    bigA = fastPowering(g,a,p);
    #print(f'g<sup>a</sup> (mod p) = {bigA}\n');
    print(tableFormat.format(f'','',f'a={a}'));
    print(tableFormat.format('', '', f'A=g^a (%p)'))
    print(tableFormat.format(f'', f'A={bigA}', f'A={bigA}'))
    k=6127;
  
    c_1 = 1;
    c_2 = 1;
  
    c_1 = fastPowering(g, k, p); #g^k
    c_2 = messageNum * fastPowering(bigA, k, p) %p; #m*(A^k)
    c_2 = c_2%p;
    print(tableFormat.format(f'k={k} (% p)','',''));
    print(tableFormat.format(f'c1 = g^k (% p)','',''));
    print(tableFormat.format('c2 = m*A^k (% p)', '', ''))
    print(tableFormat.format(f'', f'A={bigA}', ''))
    print(tableFormat.format(f'', f'c1={c_1}', ''))
    print(tableFormat.format(f'', f'c2={c_2}', ''))
    #print(f'(c1, c2) = ({c_1}, {c_2})\n');
    
    nC_1 = fastPowering(c_1, a, p) #calculate A
    #print(f'A^k is calculated as {nC_1}\n');
    #now just a modulo inverse is required for the last step
    nC_2 = inverseModulo(nC_1, p);
    #print(f'Inverse modulo\'d to {nC_2}\n');
    uncovered = (nC_2*c_2) %p;
    print(tableFormat.format(f'', f'', 'code= (c1^a)^(-1) * c_2'));
    print(tableFormat.format(f'', f'', f'={uncovered}'))

    originalString = '';
    i=1;
    power=0;
    while (uncovered>0):
        originalString += '#abcdefghijklmnopqrstuvwxyz'[uncovered%27];
        uncovered = uncovered//27;

    print(tableFormat.format(f'', f'', f'={originalString}'))
    #print(f'Original message is {originalString}');


#print(inverseModulo(29, 41));
theElGamal();
