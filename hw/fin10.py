#One of the early common methods for encrypting text was the
#Playfair cipher. You can read more about the Playfair cipher
#here: https://en.wikipedia.org/wiki/Playfair_cipher
#
#The Playfair cipher starts with a 5x5 matrix of letters,
#such as this one:
#
# D A V I O
# Y N E R B
# C F G H K
# L M P Q S
# T U W X Z
#
#To fit the 26-letter alphabet into 25 letters, I and J are
#merged into one letter. When decrypting the message, it's
#relatively easy to tell from context whether a letter is
#meant to be an i or a j.
#
#To encrypt a message, we first remove all non-letters and
#convert the entire message to the same case. Then, we break
#the message into pairs. For example, imagine we wanted to
#encrypt the message "PS. Hello, worlds". First, we could
#convert it to PSHELLOWORLDS, and then break it into letter
#pairs: PS HE LL OW OR LD S. If there is an odd number of
#characters, we add X to the end.
#
#Then, for each pair of letters, we locate both letters in
#the cipher square. There are four possible orientations
#for the pair of letters: they could be in different rows
#and columns (the "rectangle" case), they could be in the
#same row but different columns (the "row" case), they could
#be in the same column but different rows (the "column"
#case), or they could be the same letter (the "same" case).
#
#Looking at the message PS HE LL OW OR LD SX:
#
# - PS is the Row case: P and S are in the same row.
# - HE is the Rectangle case: H and E are in different rows
#   and columns of the square.
# - LD is the Column case: L and D are in the same column.
# - LL is the Same case as it's two of the same letter.
#
#For the Same case, we replace the second letter in the pair
#with X, and then proceed as normal. When decrypting, it
#would be easy to see the our result was not intended to be
#PS HELXO WORLDSX, and we would thus assume the X is meant to
#repeat the previous letter, becoming PS HELLO WORLDSX.
#
#What we do for each of the other three cases is different:
#
# - For the Rectangle case, we replace each letter with
#   the letter in the same row, but the other letter's
#   column. For example, we would replace HE with GR:
#   G is in the same row as H but the same column as E,
#   and R is in the same row as E but the same column as
#   H. For another example, CS would become KL: K is in
#   C's row but S's column, and L is in C's column but S's
#   row.
# - For the Row case, we pick the letter to the right of
#   each letter, wrapping around the end of the row if we
#   need to. PS becomes QL: Q is to the right of P, and L
#   is to the right of S if we wrap around the end of the
#   row.
# - For the Column case, we pick the letter below each
#   letter, wrapping around if necessary. LD becomes TY:
#   T is below L and Y is below D.
#
#We would then return the resultant encrypted message.
#
#Decrypting a message is essentially the same process.
#You would use the exact same cipher and process, except
#for the Row and Column cases, you would shift left and up
#instead of right and down.
#
#Write two methods: encrypt and decrypt. encrypt should
#take as input a string, and return an encrypted version
#of it according to the rules above.
#
#To encrypt the string, you would:
#
# - Convert the string to uppercase.
# - Replace all Js with Is.
# - Remove all non-letter characters.
# - Add an X to the end if the length if odd.
# - Break the string into character pairs.
# - Replace the second letter of any same-character
#   pair with X (e.g. LL -> LX).
# - Encrypt it.
#
#decrypt should, in turn, take as input a string and
#return the unencrypted version, just undoing the last
#step. You don't need to worry about Js and Is, duplicate
#letters, or odd numbers of characters in decrypt.
#
#For example:
#
# encrypt("PS. Hello, world") -> "QLGRQTVZIBTYQZ"
# decrypt("QLGRQTVZIBTYQZ") -> "PSHELXOWORLDSX"
#
#HINT: You might find it easier if you implement some
#helper functions, like a find_letter function that
#returns the row and column of a letter in the cipher.
#
#HINT 2: Once you've written encrypt, decrypt should
#be trivial: try to think of how you can modify encrypt
#to serve as decrypt.
#
#To make this easier, we've gone ahead and created the
#cipher as a 2D tuple for you:
CIPHER = (("D", "A", "V", "I", "O"),
          ("Y", "N", "E", "R", "B"),
          ("C", "F", "G", "H", "K"),
          ("L", "M", "P", "Q", "S"),
          ("T", "U", "W", "X", "Z"))
import re
def divide_chunks(l, n):
    for i in range(0, len(l), n): 
        yield l[i:i + n]
def checkCase(a_str):    
    result = {}
    for i in range(len(CIPHER)):
        if a_str[0] in CIPHER[i]:
            result[a_str[0]] = [i,CIPHER[i].index(a_str[0])]    
        if a_str[1] in CIPHER[i]:
            result[a_str[1]] = [i,CIPHER[i].index(a_str[1])]
    if result[a_str[0]][0] == result[a_str[1]][0]: 
        return ['Row',result]
    elif result[a_str[0]][1] == result[a_str[1]][1]:
        return ['Column',result]  
    else:
        return ['Rec',result]

def RowEN(a_str,a_dict):
    new = ''
    for item in a_str:
        try:
            new += CIPHER[a_dict[item][0]][a_dict[item][1]+1]
        except IndexError:    
            new += CIPHER[a_dict[item][0]][0]
    return new
def ColEN(a_str,a_dict):
    new = ''  
    for item in a_str:
        try:
            new += CIPHER[a_dict[item][0]+1][a_dict[item][1]]
        except IndexError:    
            new += CIPHER[0][a_dict[item][1]]
    return new
def RecEN(a_str,a_dict):
    new = ''
    new += CIPHER[a_dict[a_str[0]][0]][a_dict[a_str[1]][1]]
    new += CIPHER[a_dict[a_str[1]][0]][a_dict[a_str[0]][1]]
    return new    

def encrypt(a_str):
    a_str=re.sub('[^A-Za-z]', '', a_str)
    a_str=a_str.upper()
    a_str=re.sub('','',a_str)
    if len(a_str)%2 == 1:
        a_str = a_str + 'X'
    chunks = list(divide_chunks(a_str,2))
    new = ''
    for items in chunks:
        if items[0] == items[1]:
            items = items[0]+'X'
        temp = checkCase(items)
        if temp[0] == 'Row':
            new += RowEN(items,temp[1])
        elif temp[0] == 'Column':
            new += ColEN(items,temp[1])
        elif temp[0] == 'Rec':
            new += RecEN(items,temp[1])
    return new    

def RowDE(a_str,a_dict):
    new = ''
    for item in a_str:
        try:
            new += CIPHER[a_dict[item][0]][a_dict[item][1]-1]
        except IndexError:    
            new += CIPHER[a_dict[item][0]][-1]
    return new
def ColDE(a_str,a_dict):
    new = ''  
    for item in a_str:
        try:
            new += CIPHER[a_dict[item][0]-1][a_dict[item][1]]
        except IndexError:    
            new += CIPHER[-1][a_dict[item][1]]
    return new
def RecDE(a_str,a_dict):
    new = ''
    new += CIPHER[a_dict[a_str[0]][0]][a_dict[a_str[1]][1]]
    new += CIPHER[a_dict[a_str[1]][0]][a_dict[a_str[0]][1]]
    return new  

def decrypt(a_str):
    chunks = list(divide_chunks(a_str,2))
    new = ''
    for items in chunks:
        temp = checkCase(items)
        if temp[0] == 'Row':
            new += RowDE(items,temp[1])
        elif temp[0] == 'Column':
            new += ColDE(items,temp[1])
        elif temp[0] == 'Rec':
            new += RecDE(items,temp[1])
    return new 
#If your function works correctly, this will originally
#print: QLGRQTVZIBTYQZ, then PSHELXOWORLDSX
#print(encrypt("PS. Hello, worlds"))
print(decrypt("QLGRQTVZIBTYQZ"))