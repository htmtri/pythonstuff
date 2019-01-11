clarity = "IF" 
color = "Z" 
preferred_cuts = ["Emerald", "Pear", "Heart", "Marquise"]
carat = 1.3
cut = "Marquise" 
budget = 1142

base_cost = 100

color_cost = 1 - 2*(ord(color) - ord("D"))/100
print(color_cost)

clarity_int = 1
if clarity == "F":
    clarity_int = 2**5
elif clarity == "IF":
    clarity_int = 2**4    
elif clarity == "VVS":
    clarity_int = 2**3  
elif clarity == "VS":
    clarity_int = 2**2  
elif clarity == "SI":
    clarity_int = 2          
print(clarity_int)

total_cost = base_cost*color_cost*clarity_int*carat

print(total_cost)

if cut in preferred_cuts and budget > total_cost:
    print("I'll take it!")
else:
    print("No thanks")    