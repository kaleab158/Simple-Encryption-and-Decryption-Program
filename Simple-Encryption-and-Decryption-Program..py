import string 
import random 
Chars ="  "  + string.ascii_letters + string.digits + string.punctuation
Chars = list(Chars)
key = Chars.copy()
random.shuffle(key)

#encription

def Encription():
 messege = input("Enter Your Messege To Encript =>  ")
 ciphertext = ""
 for letter in messege:
    index = Chars.index(letter)
    ciphertext += key[index]
 print(f"Your  Messege => {messege}")
 print(f"Encripted  Messege  / => {ciphertext}")
def Decription():
 
 # decription
 ciphertext = input("Enter Your decript messege to Read Normal Text  ")
 messege = ""
 for letter in ciphertext:
    index = key.index(letter)
    messege += Chars[index]

 print(f"Encript  Messege => {ciphertext}")
 print(f"Your Normal Messege => {messege}")

print("========= Welcome To Encription & Decription Program ========")
print("=========                                           ========")
print("=========     ADD Your Text / Messege Below         ========")
print("=========                                           ========")
print("=========                                           ========")
print("=============================================================")
Encription()
Decription()