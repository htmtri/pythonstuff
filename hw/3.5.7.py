exception_l = [".",",","!","?",""," "]

def word_count(a_str):
    prev = False
    if a_str[0] == " ":
        count = 0
    else:
        count = 1
    for char in a_str:
        if char == " ":
            prev = True
        else:
            if prev:
                count +=1
            prev = False    
    return count

def letter_count(a_str):
    count = 0
    for char in a_str:
        if not(char in exception_l):
            count +=1
    return count
        
def average_word_length(my_string):
    try:
        a = word_count(my_string)
        b = letter_count(my_string)
        if a == 0:
            return "No words"
        elif b == 0:
            return "No words"
        else:
            return b/a
    except:
        return "Not a string"

#print(word_count("   What   big spaces  you    have!"))
#print(average_word_length("Hi"))
#print(average_word_length("Hi, Lucy"))
print(average_word_length("   What   big spaces  you    have!"))
#print(average_word_length(True))
#print(average_word_length("?!?!?! ... !"))
        