import math
import random

P=5
Q=7
n = P*Q
Φn = (P-1)*(Q-1)

def generate_e():
    e = random.randrange(1,Φn)
    return e

def generate_d():
    k = random.randint(1,100)
    d = (k*Φn +1) / e
    d = math.floor(d)
    return d

def encrypt(msg):
    e_text = []
    for i in range(len(msg)):
        e_text.append(ord(msg[i]))
    return "".join(str(i) for i in e_text), e_text
    # Encrypted Data c = (89 ** e) % n


def decrypt():
    global e_text
    d_text = ""
    for i in e_text:
        d_text += chr(i)
    return d_text
    # Decrypted Data = (c ** d) % n

e = generate_e()
d = generate_d()

msg = input("Enter the String : ")

encrypt_text, e_text = encrypt(msg)
decrypt_text = decrypt()

print("Public_Key : "+str(n)+", "+str(e))
print("Private_Key : "+str(d))
print("The Encrypted text is : "+encrypt_text)
print("The Decrypted text is : "+decrypt_text)