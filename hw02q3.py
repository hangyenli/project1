##this is homework02 question 3 in this problem we need Write a program that either encrypts or decrypts a string, depending on the choice that the user makes. ##


def encrypt(WORD1):
    WORD1=WORD1.replace(' a','%4%')
    WORD1=WORD1.replace('he','7!')
    WORD1=WORD1.replace('e','9(*9(')
    WORD1=WORD1.replace('y','*%$')
    WORD1=WORD1.replace('u','@@@')
    WORD1=WORD1.replace('an','-?')
    WORD1=WORD1.replace('th','!@+3')
    WORD1=WORD1.replace('o','7654')
    WORD1=WORD1.replace('9','2')
    return WORD1
def decrypt(WORD2):
    WORD2=WORD2.replace('%4%',' a')
    WORD2=WORD2.replace('7654','o')
    WORD2=WORD2.replace('7!','he')
    WORD2=WORD2.replace('2','9')
    WORD2=WORD2.replace('9(*9(','e')
    WORD2=WORD2.replace('*%$','y')
    WORD2=WORD2.replace('@@@','u')
    WORD2=WORD2.replace('-?','an')
    WORD2=WORD2.replace('!@+3','th')
    
    return WORD2

x=input("Enter 'E' for encrypt or 'D' for decrypt ==> ")
print(x)

if x=='d' or x=='D':
    a=input('Enter cipher text ==> ')
    print(a)
    print()
    print('Deciphered as ==>',decrypt(a))
    d=abs(len(a)-len(decrypt(a)))
    print('Difference in length ==>',d)
    
elif x=='e' or x=='E':
    a=input('Enter regular text ==> ')
    print(a)
    print()
    print('Encrypted as ==>',encrypt(a))
    d=abs(len(a)-len(encrypt(a)))
    print('Difference in length ==>',d)
    
else :
    print("I didn't understand ... exiting")
