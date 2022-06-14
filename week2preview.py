 # super hero class:

# from operator import truediv
# from random import randint

# class Superhero:
#     def __init__(self, name, superpower, weakness, health, power):
#         self.name = name
#         self.superpower = superpower
#         self.weaness = weakness
#         self.health = health
#         self.power = power

#     def __repr__(self):
#         return f"< Superhero | name:{self.name} | health:{self.health} | power:{self.power}>"

#     def take_damage(self, amount_of_damage):
#         self.health -= amount_of_damage

#     def punch_enemy(self, enemy):
#         print(f"{self.name} tries to punch {enemy.name}.")
        
#         if randint(0, 100) >= 50:
#             enemy.take_damage(self.power)
#             print(f"ouch! {enemy.name} took damage of {self.power}, and now has the heath of {enemy.health}.")
        
#             if enemy.is_dead():
#                 print(f"{enemy.name} has died of his her wounds....rip.... f in the chat.")
#             else:
#                 print(f"{enemy.name} is still alive and still in the fight.")

#     def is_dead(self):
#         if self.health <= 0:
#             return True
#         else:
#             return False

# superman = Superhero("Superman", "Everything", "Kryptonite", 1000, 1000)

# batman = Superhero("Batman", "rich", "orphan", 100, 350)

# batman.punch_enemy(superman)

# superman.punch_enemy(superman)





from random import randint

class Superhero:
    def __init__(self, name, superpower, weakness, health, power):
        self.name = name
        self.superpower = superpower
        self.weakness = weakness
        self.health = health
        self.power = power

    def __repr__(self):
        return f"< Superhero | name: {self.name} | health: {self.health} | power: {self.power} >"

    def take_damage(self, amount_of_damage):
        self.health -= amount_of_damage

    def punch_enemy(self, enemy):
        print(f"{self.name} tries to punch {enemy.name}.")
        
        if randint(0, 100) >= 50:
            
            enemy.take_damage(self.power)
            print(f"Ouch! {enemy.name} took damage of {self.power} damage, and NOW has the health of {enemy.health}.")
            
            if enemy.is_dead():
                print(f"{enemy.name} has died of his/her wounds.... RIP.... f in the chat.")
            else:
                print(f"{enemy.name} is still alive and in the fight!")
        
        else:
            print(f"{self.name}'s punch attack failed!!!!")

    def is_dead(self):
        if self.health <= 0:
            return True
        else:
            return False



    

superman = Superhero("Superman", "Everything", "Kryptonite", 1000, 1000)

batman = Superhero("Batman", "Rich and Smart", "Parents are dead", 100, 350)

batman.punch_enemy(superman)

superman.punch_enemy(batman)
superman.punch_enemy(batman)