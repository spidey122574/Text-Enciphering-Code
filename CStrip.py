"""I am particularly proud of this program, it allows you to pick a codeword, then the program will
create a string of letters to be used as a reference to encipher your information."""



cWord = input('Cypher Word? ***ALL CAPS PLEASE***> ')
codeWord = list(cWord) #makes the codeword a list to be used
codeWord = list(dict.fromkeys(codeWord)) #removes the duplicate letters from the codeword
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS = list(dict.fromkeys(LETTERS))
codeWordset = set(codeWord)
LETTERSset = set(LETTERS)
alphaList = list(LETTERSset - codeWordset) #removes the codeword from the alphabet
alphaList.sort() #puts the remaining alphabet words into alphabetical order
cypherStrip = codeWord + alphaList #adds your codeword to the beginning of the alphabet
print(cypherStrip)   

cypherStripstr = cypherStrip #creates a string for the main program
cStrip = ""
for x in cypherStripstr:
    cStrip += x

print(cStrip)
