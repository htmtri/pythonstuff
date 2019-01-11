class Meat:
    def __init__(self, value=False):
        self.set_value(value)
            
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        if value in ["chicken", "pork", "steak", "tofu"]:
            self.value = value
        else:
            self.value = False

class Rice:
    def __init__(self, value=False):
        self.set_value(value)
            
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        if value in ["brown", "white"]:
            self.value = value
        else:
            self.value = False
            
class Beans:
    def __init__(self, value=False):
        self.set_value(value)
            
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        if value in ["black", "pinto"]:
            self.value = value
        else:
            self.value = False
            
class Burrito:
    def __init__(self,meat,to_go,rice,beans,extra_meat = False, guacamole = False,
    cheese = False, pico = False, corn = False):
        self.set_meat(meat)       
        self.set_to_go(to_go)
        self.set_rice(rice)       
        self.set_beans(beans)   
        self.extra_meat = extra_meat
        self.guacamole = guacamole
        self.cheese = cheese
        self.pico = pico
        self.corn = corn

    def get_meat(self):
        return self.meat.get_value()
    def get_to_go(self):
        return self.to_go        
    def get_rice(self):
        return self.rice.get_value()
    def get_beans(self):
        return self.beans.get_value()
    def get_extra_meat(self):
        return self.extra_meat
    def get_guacamole(self):
        return self.guacamole
    def get_cheese(self):
        return self.cheese
    def get_pico(self):
        return self.pico    
    def get_corn(self):
        return self.corn

    def set_meat(self,meat):
        self.meat = Meat(meat)   
    def set_to_go(self,to_go):
        if type(to_go) == bool:
            self.to_go = to_go
        else:
            self.to_go = False            
    def set_rice(self,rice):
        self.rice = Rice(rice)
    def set_beans(self,beans):
        self.beans = Beans(beans)
    def set_extra_meat(self,extra_meat):
        if type(extra_meat) == bool:
            self.extra_meat = extra_meat
        else:
            self.extra_meat = False
    def set_guacamole(self,guacamole):
        if type(guacamole) == bool:
            self.guacamole = guacamole
        else:
            self.guacamole = False
    def set_cheese(self,cheese):
        if type(cheese) == bool:
            self.cheese = cheese
        else:
            self.cheese = False
    def set_pico(self,pico):
        if type(pico) == bool:
            self.pico = pico
        else:
            self.pico = False    
    def set_corn(self,corn):
        if type(corn) == bool:
            self.corn = corn
        else:
            self.corn = False 

    def get_cost(self):
        cost = 5.0
        if self.get_meat() in ["chicken", "pork", "beef"]:
            cost += 1.0
        if self.get_meat() == "steak":
            cost += 1.5
        if self.get_extra_meat() and self.get_meat():
            cost += 1.0
        if self.get_guacamole():
            cost += 0.75
        return cost
        
#Write a function called total_cost. total_cost should take
#as input a list of instances of Burrito, and return the
#total cost of all those burritos together as a float.
#
#Hint 2: The exercise here is to write a function, not a
#method. That means this function should *not* be part of
#the Burrito class.
def total_cost(bu_l):
    result = 0
    for bur in bu_l:
        result += bur.get_cost()
    return result    

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs. Note that these lines
#will ONLY work if you copy/paste your Burrito, Meat,
#Beans, and Rice classes in.
#
#If your function works correctly, this will originally
#print: 27.0
burrito_1 = Burrito("tofu", True, "white", "black")
burrito_2 = Burrito("steak", True, "white", "pinto", extra_meat = True)
burrito_3 = Burrito("pork", True, "brown", "black", guacamole = True)
burrito_4 = Burrito("chicken", True, "brown", "pinto", extra_meat = True, guacamole = True)
burrito_list = [burrito_1, burrito_2, burrito_3, burrito_4]
print(total_cost(burrito_list))