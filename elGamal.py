import math, random;
import functionDeposit as x;
tableFormat = '{:^45}|{:^45}|{:^45}';
def theElGamal():
    #document.getElementById("console").innerHTML = '';
    message = input("Enter the message (please English letter only because message can only encode english letters): ").lower(); #a string; like: "the tea in Nepal is vey hot"
    print(tableFormat.format('Computer A', 'comm. channel', 'Computer B'));
    print('-'*123);
    messageNum = 0;
    for char in range(len(message)):
        messageNum += '#abcdefghijklmnopqrstuvwxyz'.find(message[char])*(27**char);
    print(tableFormat.format(f'(encode {message})', '', ''));    
    #print(f'Cool - we\'re sending {message} (which is {messageNum} as a number).\n');
    print(tableFormat.format(f'm={messageNum}', '', ''))
    p = 2**127 - 1; #Arbitrary prime number. In an ideal crypto-system, prime number should be random; it's just that at this scale,
    #it would take lots of time to generate such a prime (and irrelevant to the project)
    g = random.randint(2,p-1); 
    a = random.randint(1, 2**125);
    if (messageNum>p):
        print(f'Message is too long. Try again.');
        return False
    
    #print(f'Public values are g: {g} and the prime: {p}\n');
    print(tableFormat.format('', f'g={g}', ''));
    print(tableFormat.format('', f'p={p}', ''));
    
    bigA = x.fastPowering(g,a,p);
    #print(f'g<sup>a</sup> (mod p) = {bigA}\n');
    print(tableFormat.format(f'','',f'a={a}'));
    print(tableFormat.format('', '', f'A=g^a (%p)'))
    print(tableFormat.format(f'', f'A={bigA}', f'A={bigA}'))
    k=random.randint(1, 2**125);
  
    c_1 = 1;
    c_2 = 1;
  
    c_1 = x.fastPowering(g, k, p); #g^k
    c_2 = messageNum * x.fastPowering(bigA, k, p) %p; #m*(A^k)
    c_2 = c_2%p;
    print(tableFormat.format(f'k={k} (% p)','',''));
    print(tableFormat.format(f'c1 = g^k (% p)','',''));
    print(tableFormat.format('c2 = m*A^k (% p)', '', ''))
    print(tableFormat.format(f'', f'A={bigA}', ''))
    print(tableFormat.format(f'', f'c1={c_1}', ''))
    print(tableFormat.format(f'', f'c2={c_2}', ''))
    #print(f'(c1, c2) = ({c_1}, {c_2})\n');
    
    nC_1 = x.fastPowering(c_1, a, p) #calculate A
    #print(f'A^k is calculated as {nC_1}\n');
    #now just a modulo inverse is required for the last step
    nC_2 = x.inverseModulo(nC_1, p);
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
