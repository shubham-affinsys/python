

"""
Algorithm:
    RSA key generation
        choose two large prime numbers p and q
        calculate n = p*q
        select public key e such that it is not a factor of (p-1)*(q-1)
        select private key d such that floww eq is true (d*e)mod(p-1)(q-1)=1 or d is inverse of E in modulo (p-1)*(q-1)

    RSA Digital Signature Scheme:
        in RSA d is private
        e and n are public
        Alice creates  her digital signature using S=M^d mod n where M is message
        Alice sends MEssage M and Signature S to Bob
        Bob computes M1=S^e mod n
        if M1=M then Bob accepts the data sent by Alice

Time Complexity: O(log(min(m, n))

The security of the RSA system is mainly reliant on the computational difficulties of factoring big composite numbers. If p and q are large primes, factoring n becomes computationally expensive and time-consuming, even on powerful computers. This prevents an attacker from identifying the private key from the public key, ensuring the security of the RSA system.
"""




#using pycryptodome
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# RSA key gen
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

print("Public key: ",public_key.decode())
print("Private key: ",private_key.decode())


# RSA Digital Signature Scheme

#Alice create her digital signature using gher private key
message = b"Tis is my msg"
hash = SHA256.new(message)
signature = pkcs1_15.new(key).sign(hash)

print("Signature: ",signature.hex())

#Alice sends the message and Signature to BOb
#Bob computes hash of the message and verifies the signature using Alice's public key

try:
    pkcs1_15.new(key.publickey()).verify(hash,signature)
    print("The signature is valid")
except (ValueError,TypeError):
    print("The signature is not valid")





#using simple math and functions
"""
def euclid(m, n):
    if n == 0:
        return m
    else:
        r = m % n
        return euclid(n, r)

def exteuclid(a, b):
    r1, r2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1

    while r2 > 0:
        q = r1 // r2
        r1, r2 = r2, r1 - q * r2
        s1, s2 = s2, s1 - q * s2
        t1, t2 = t2, t1 - q * t2

    if t1 < 0:
        t1 = t1 % a
    return r1, t1

p = 823
q = 953
n = p * q
phi_n = (p - 1) * (q - 1)  #Calculate Euler's Totient function

# Generate encryption key in range 1 < e < phi_n
key = []
for i in range(2, phi_n):
    if euclid(phi_n, i) == 1: #coprime
        key.append(i)

# Select encryption key e from the list
e = key[0]

# Obtain the inverse of the encryption key in Z_phi_n
r, d = exteuclid(phi_n, e)
if r == 1:
    print("Decryption key is:", d)
else:
    print("Multiplicative inverse for the given encryption key does not exist. Choose a different encryption key")

# Enter message to be sent
M = 19070

# Signature is created by Alice
S = pow(M, d, n)

# Alice sends M and S both to Bob
# Bob generates message M1 using signature S, Alice's public key e, and product n
M1 = pow(S, e, n)

# If M == M1 only then Bob accepts the message sent by Alice
if M == M1:
    print("Message accepted")
else:
    print("Message rejected")



"""