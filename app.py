# data types
my_integer = 17764356786479898
my_float= 3.54 * 4.64

my_string= "this is a string"

my_boolean = True
my_other_boolean = False

my_none_type = None

#conditionals
# if my_integer >= 13:
#     print("It's a big number!")
# elif my_integer >= 7:
#     print("this is a medium number!")
# else:
#     print("this is a small number!")    


# functions
def is_awesome(name, boolean):
    if boolean:
        return f"{name} is super awesome!"
    else:
        return f"{name} is totally not awesome!"

# print(is_awesome("James Goff", True))
# print(is_awesome("Jared Goff", False))

def my_blank_function():
    pass

my_name = input("What is your name?  ")
print(f"Hey there {my_name}.")



# print


print("my thing")

# executing code
is_awesome("captain america", True)
print(is_awesome("thanos", False))



#basic data structure

#lists
movies_lists = ["infinity war", "endgame", 1984]
movies_lists.append("Dr. strange and multiverse")

# print(movies_lists)



#tuples
movies_tuples = ("infinity war", "endgame", 1984)
movies_tuples = ("marry poppins", "parent trap")
# print(movies_tuples)

#sets

movies_set = {"infity war", "endgame", 1984}
movies_set.add("black panther")
movies_set.add("infinity war")
print(movies_set)

#dictionaries
my_dictionary = {
    "title": "thor ragnar",
    "director": "taika",
    "is_good": True,
}