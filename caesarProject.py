#encryption logic
def encrypt(word, shift):
    #turn the word into a list
    neWord = list(word)
    #the standard base 26 letters so the code knows what letters to place where. a = index 0 and z =25
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #empty list to store the encyrptoion
    nl = []
    #go throughs each letter in the word
    for i in neWord:
        if i not in letters:
            nl.append(i) #list method
        #if the shift goes past 25, subtract 26 to go back around
        elif letters.index(i) +shift >25:
            nl.append(letters[letters.index(i)+shift-26])
        #normal if shift doesnt go back around
        else:
            nl.append(letters[letters.index(i)+shift])
    #converts the list into a string
    final = ''.join(nl)
    return final

#decrytion logic
def decrypt(word, shift):
    neWord = list(word)
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    nl = []
    for i in neWord:
        if i not in letters:
            nl.append(i)
        #since this is decrypt, we have to subtract instead of add.
        #if the shift is less then 0, we wrap back around by adding 26
        elif letters.index(i)-shift <0:
            nl.append(letters[letters.index(i)-shift+26])
        #normal shift if you dont have to wrap back around
        else:
            nl.append(letters[letters.index(i)-shift])
    final = ''.join(nl)
    return final

print("Welcome to the Ceasar Cipher Terminal!")
word = input("Enter a word: ").lower() #string method
shift = int(input("Enter a shift value: "))

while True:
    try:
        enc = int(input("Wound you like to encrypt (1) or decrypt (2): "))
        break
    except ValueError:
        print("Please try again and enter a valid letter.")   

if enc == 1:
    ans = encrypt(word, shift)
    print(f"Your encrypted word is: {ans}")

elif enc == 2:
    ans = decrypt(word, shift)
    print(f"Your decrypted word is: {ans}")

else:
    print("You entered a wrong value. Please try again")
