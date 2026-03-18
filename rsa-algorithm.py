#from functionDeposit.py import inverseModulo, fastPowering;
import random
import functionDeposit as x; #Local file, the el Gamal file has lots of necessary algorithms stored
print(x.inverseModulo(241,(2**127 - 2)*(2**107 - 2)));
print(x.inverseModulo(19,(2**127 - 2)*(2**107 - 2)));

tableFormat = '{:^45}|{:^45}|{:^45}';

def rsa():
    message = input("Enter the message: (ascii characters)") #a string; more characters allowed in RSA than elGamal
    print(tableFormat.format('Computer A', 'comm. channel', 'Computer B'));
    print('-'*141);

    #Generate key
    p = 2**127 - 1;
    q = 2**107 - 1;
    #arbitrary primes. Should ideally be randomly generated but that scale is quite difficult to get to on an ordinary laptop.
    
    print(tableFormat.format('','',f'Generate key for message receival'));
    
    print(tableFormat.format('','',f'Primes p and q selected:'));
    print(tableFormat.format('','',f'p={p}'));
    print(tableFormat.format('','',f'q={q}'));

    pminusoneqminusone = (p-1)*(q-1) #Sorry about the name of this variable lol

    d = -1
    while (d == -1):
        e = random.randint(1, 2**200);

        d = x.inverseModulo(e, pminusoneqminusone)

        #if (d == -1):
         #   print("d = -1 is invalid. Retry");
            
    print(tableFormat.format('','',f'Choose a (public) random number e '));
    print(tableFormat.format('',f'e={str(e)[:40]}...',''));
    print(tableFormat.format('',f'...{str(e)[40:]}',''));
    print(tableFormat.format('','',f'd is the modulo inverse of e (mod (p-1)(q-1))'));
    print(tableFormat.format('','',f'd={str(d)[:40]}...'));
    print(tableFormat.format('','',f'...{str(d)[40:]}'));


    n = p*q;
    print(tableFormat.format('', f'N=p*q', ''));
    print(tableFormat.format('', f'= {str(n)[:40]}...', ''));
    print(tableFormat.format('', f'...{str(n)[40:]}', ''));


    messageNum = 0;
    for char in range(len(message)):
        messageNum += ord(message[char])*(128**char);
    print(tableFormat.format(f'Encode `{message}` in ascii', '', ''));
    if messageNum > 10**41:
        print(tableFormat.format(f'm={str(messageNum)[:40]}...', '', ''));
        print(tableFormat.format(f'...{str(messageNum)[:40]}', '', ''));
    else:
        print(tableFormat.format(f'm={str(messageNum)}', '', ''));
        
    
    print(tableFormat.format('Now encode for computer B with public keys', '', ''))
    
    print(tableFormat.format('c=m^e (mod N), make c public','', ''));
    c = x.fastPowering(messageNum,e,n);
    print(tableFormat.format('',f'c={str(c)[:38]}...', ''));
    print(tableFormat.format('',f'...{str(c)[38:]}', ''));

    
    print(tableFormat.format(f'','', 'To decode message, m\' = c^d (mod N)'));
    nM = x.fastPowering(c, d, n);
    if nM > 10**41:
        print(tableFormat.format(f'','', f'm\'={str(nM)[:40]}...'));
        print(tableFormat.format(f'','', f'...{str(nM)[40:]}'));
    else:
        print(tableFormat.format(f'','', f'{str(nM)}'));
    print(tableFormat.format(f'','', f'Convert message from ascii to get: '));

    ogMessage = '';
    while (nM>0):
        ogMessage += chr(nM%128);
        nM = nM//128;
    
    print(tableFormat.format(f'','', f'`{ogMessage}`'));
    
rsa();
