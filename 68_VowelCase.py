# Vowel and Consonant using case

ch = input("Enter an alphabet: ").lower()

match ch:
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print("Vowel")
    case _ if ch.isalpha() and len(ch) == 1:
        print("Consonant")
    case _:
        print("Invalid input")