
def factorise(n):
    p = q = 0
    for i in range(2,n):

        if n % i == 0:

            for j in range(2,i):
                
                if i % j == 0: break
                else: 
                    p = i
                    q = int(n / p)
                    for k in range(2,q):
                        if q % k == 0: p = 0; break
                    
                    break;
            if p == i: break;

    if p == 0 : print("This number has no prime factors!"); exit();
    else: return p, q

p = 0
q = 0
d = 0
cryptogram = []

n = int(input("Input 'n': "))
e = int(input("Input 'e', the part of the public key: "))

p, q = factorise(n)

print("\nInput cryptogram (finish with 'Enter'): ")
while(True):
    
    try:
        inputValue = input()
        if(inputValue == ''): break
        number = int(inputValue)
        cryptogram.append(number)
        
    except ValueError:
        print("That is not a number! Input again!")
        continue

print("\nPrime factors of number {} are {} and {}.\n".format(n, p, q))

z = (p-1) * (q-1)

for i in range(1,z):
    if i == e: pass
    if (i*e) % z == 1:
        d = i
        break

print("Public key is ({},{}).".format(n,e))
print("Private key is ({},{}).".format(n,d))

message = []

for c in cryptogram:
    m = pow(c,d) % n
    message.append(chr(m+54))

print("\nCryptogram: {}".format(cryptogram))
print("\nDecrypted message is: {}\n".format(message))
