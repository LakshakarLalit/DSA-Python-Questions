# Enter alphabet and check whether it is vowel or consonant

ch = input("Enter a character: ")

if len(ch) == 1 and ch.isalpha():
    ch = ch.lower()
    if ch in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Not an alphabet")