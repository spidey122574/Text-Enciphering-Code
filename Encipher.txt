import pyperclip, sys, random #pyperclip allows the user to call the clipboard through their programs
#pyperclip is not mine in any way, shape, or form!  I found it online
import CStrip #This calls a program I created to customize the cypher strip for the program
import Message #This calls another program I created to accept a custom message
import Mode # calls the program to set the mode of this program


myMode = Mode.myMode
myKey = CStrip.cStrip
myMessage = Message.myMessage
translated = ""
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    pass

def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if myMode == 'decrypt':
        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.
        charsA, charsB = charsB, charsA

    # Loop through each symbol in message:
    for symbol in message:
        if symbol.upper() in charsA:
            # Encrypt/decrypt the symbol:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # Symbol is not in LETTERS; just add it
            translated += symbol

    return translated

def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')

#***Mode Switch***    
if myMode == 'encrypt':
    translated = encryptMessage(myKey, myMessage)
elif myMode == 'decrypt':
    translated = decryptMessage(myKey, myMessage)

print('Using key %s' % (myKey))
print('The %sed message is:' % (myMode))
print(translated)
pyperclip.copy(translated)
print()
print('This message has been copied to the clipboard.')

    
if __name__ == '__main__':
    main()
