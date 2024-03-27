# Referensi :
    # 1. https://www.pythonpool.com/rsa-encryption-python/
    # 2. https://www.askpython.com/python/examples/rsa-algorithm-in-python

# Steps
    # 0. misalkan pesan : m = 89
    # 1. ambil dua angka prima 
        # p1 = 7, p2 =11
    # 2. hitung n = p1*p2
        # n = 7*11 = 77
    # 3. ambil e dengan 1 < e < phi(n)
        # phi(n) = (p1-1) * (p2-1) = 6*10 = 60
        # misal : e = 3
    # 4. enkripsi : c = m^e (mod n)
        # c = 89^3 (mod 77) = 166

import math
 
# step 1
p = 3
q = 7
 
# step 2
n = p*q
print("n =", n)
 
# step 3
phi = (p-1)*(q-1)
 
# step 4
e = 2
while(e<phi):
    if (math.gcd(e, phi) == 1):
        break
    else:
        e += 1
 
print("e =", e)
# step 5
k = 2
d = ((k*phi)+1)/e
print("d =", d)
print(f'Public key: {e, n}')
print(f'Private key: {d, n}')
 
# plain text
msg = 11
print(f'Original message:{msg}')
 
# encryption
C = pow(msg, e)
C = math.fmod(C, n)
print(f'Encrypted message: {C}')
 
# decryption
M = pow(C, d)
M = math.fmod(M, n)
 
print(f'Decrypted message: {M}')      