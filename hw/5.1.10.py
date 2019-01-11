#Copy your Burrito class from the last exercise. Now, add
#a method called "get_cost" to the Burrito class. It should
#accept zero arguments (except for "self", of course) and
#it will return a float. Here's how the cost should be
#computed:
#
# - The base cost of a burrito is $5.00
# - If the burrito's meat is "chicken", "pork" or "tofu", 
#   add $1.00 to the cost
# - If the burrito's meat is "steak", add $1.50 to the cost
# - If extra_meat is True and meat is not set to False, add
#   $1.00 to the cost
# - If guacamole is True, add $0.75 to the cost
#
#Make sure to return the result as a float even if the total
#is a round number (e.g. for burrito with no meat or
#guacamole, return 5.0 instead of 5).
valid_meat = ["chicken", "pork", "steak", "tofu", False]
valid_rice =  ["brown", "white", False]
valid_beans =  ["black", "pinto", False]
meat1 = ["chicken","pork","tofu"]
class Burrito:
    def __init__(self,meat,to_go,rice,beans,extra_meat = False, guacamole = False,
    cheese = False, pico = False, corn = False):
        if meat in valid_meat:
            self.meat = meat
        else:
            self.meat = False
        if type(to_go) == bool:        
            self.to_go = to_go
        else:
            self.to_go = False    
        if rice in valid_meat:
            self.rice = rice
        else:
            self.rice = False
        if beans in valid_beans:        
            self.beans = beans
        else:
            self.beans = False    
        self.extra_meat = extra_meat
        self.guacamole = guacamole
        self.cheese = cheese
        self.pico = pico
        self.corn = corn

    def get_meat(self):
        return self.meat
    def get_to_go(self):
        return self.to_go        
    def get_rice(self):
        return self.rice
    def get_beans(self):
        return self.beans
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
        if meat in valid_meat:
            self.meat = meat
        else:
            self.meat = False    
    def set_to_go(self,to_go):
        if type(to_go) == bool:
            self.to_go = to_go
        else:
            self.to_go = False            
    def set_rice(self,rice):
        if rice in valid_rice:
            self.rice = rice
        else:
            self.rice = False
    def set_beans(self,beans):
        if beans in valid_beans:
            self.beans = beans
        else:
            self.beans = False
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
        result = 5.00
        if self.meat in meat1:
            result += 1.00
        elif self.meat == "steak":
            result += 1.50
        if self.guacamole == True:
            result += 0.75
        if self.extra_meat == True and not self.meat == False:
            result += 1.00            
        return result


#Below are some lines of code that will test your class.
#You can change the value of the variable(s) to test your
#class with different inputs.
#
#If your function works correctly, this will originally
#print: 7.75
a_burrito = Burrito("pork", False, "white", "black", extra_meat = True, guacamole = True)
print(a_burrito.get_cost())