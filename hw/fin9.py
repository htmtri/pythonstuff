import operator
class Poke:
    def __init__(self,ID,name,type1,type2,HP,Atk,Def,SpecAtk,SpecDef,Speed,Gen,Legend,Mega):
        self.ID = ID
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.HP = HP
        self.Atk = Atk
        self.Def = Def
        self.SpecAtk = SpecAtk
        self.SpecDef = SpecDef
        self.Speed = Speed
        self.Gen = Gen
        self.Legend = Legend
        self.Mega = Mega
    def sumstat(self):
        result = int(self.HP) + int(self.Atk) + int(self.Def) + int(self.SpecAtk) + int(self.SpecDef) + int(self.Speed)
        return result    
pokedex = open('samplepoke.csv','r')
poke_l = []
for lines in pokedex.readlines():
    poke_l.append(lines.strip())
poke_l = poke_l[1:]
pokemon_l = []
for items in poke_l:
    temp = items.split(',')
    Pokemon = Poke(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],
    temp[6],temp[7],temp[8],temp[9],temp[10],temp[11],temp[12])
    pokemon_l.append(Pokemon)

#count = 0
#for items in pokemon_l:
#    if items.type2 == '':
#        count += 1 

#type_list = {}
#for items in pokemon_l:
#    if not items.type1 in type_list: 
#        type_list[items.type1] = [0,0]
#    if not items.type2 in type_list:
#        type_list[items.type2] = [0,0]
#    type_list[items.type1][0] += 1
#    type_list[items.type1][1] += int(items.Speed)
#    type_list[items.type2][0] += 1
#    type_list[items.type2][1] += int(items.Speed)
#type_list.pop('')
#avg_sp =  {}
#for items in type_list:
#    avg_sp[items] = type_list[items][1]/type_list[items][0]
#print(max(avg_sp.items(),key=operator.itemgetter(1))[0]) 

#for items in pokemon_l:
#    if not(items.Mega == 'TRUE') or not(items.Legend == 'TRUE'):
#        if int(items.Def) == 230:
#            print(items.name)

#stat = {}
#for items in pokemon_l:
#    if not items.Gen in stat:
#        stat[items.Gen] = [0,0]
#    stat[items.Gen][0] += 1
#    stat[items.Gen][1] += items.sumstat()
#stat = {}
#for items in pokemon_l:
#    if not items.ID in stat:
#        stat[items.ID] = 0
#    stat[items.ID] += 1  
#print(stat)      
#avg_sum = {'Mega': 0, 'nonMega': 0}
#count1 = 0
#count2 = 0
#for items in stat:
#    if stat[items][0] > 1:
#        avg_sum['Mega'] += stat[items][1]
#        count1 += stat[items][0]
#    else:
#        avg_sum['nonMega'] += stat[items][1]
#        count2 += 1
#print(avg_sum, count1,count2)  
#print(max(avg_sum.items(),key=operator.itemgetter(1))[0])    

for items in pokemon_l:
    
print(mega_ID)        
Normal = {}
Mega = {}
for items in pokemon_l:
    if items.ID in mega_ID:
        if items.Mega == 'FALSE':
            Normal[items.ID] = items.sumstat()
        if items.Mega == 'TRUE':
            if not items.ID in Mega:
                Mega[items.ID] = [0,0]
            Mega[items.ID][0] += 1
            Mega[items.ID][1] += items.sumstat()
print(len(Normal))  
print(len(Mega))          