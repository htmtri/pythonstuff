import operator
names_file = open('../resource/lib/public/babynames.csv', 'r')
#name,count,gender
vowels = ['A','E','I','O','U','a','e','i','o','u']
name_raw = []
#ncount = 0
for lines in names_file.readlines():
    name_raw.append(lines.strip())
    #ncount += 1
 
name_dict = {}
name_same = [] #{}
for items in name_raw:
    temp = items.split(',')
    #if temp[2] == 'Girl' and temp[0][0] == 'Q':
    #if temp[0][0] in vowels and temp[0][-1] in vowels:
    if temp[0] in name_dict:
        #name_same[temp[0]] = [name_dict[temp[0]],int(temp[1])]
        name_same.append(temp[0])
        name_dict[temp[0]] -= int(temp[1])
    if temp[0] not in name_dict:
        name_dict[temp[0]] = int(temp[1])

                
#print(max(name_dict.items(),key=operator.itemgetter(1))[1])
#print(name_same)

name_diff = {}
for items in name_dict:
    if items in name_same:
        name_diff[items] = abs(name_dict[items])
        
print(min(name_diff.items(),key=operator.itemgetter(1))[0])