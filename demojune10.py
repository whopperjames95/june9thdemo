# math and variables

# num = 60/3
# swallows = 1450
# swallows_total = swallows / num



# print (swallows_total)

# import math
# num_macaws = 4.8
# math.ceil(num_macaws)

# num_macaws_new = math.ceil(num_macaws)

# print(num_macaws_new)



#strings:

# name = 'monty python'
# description = 'sketch comedy group'
# year = 1969

# sentence = name + ' is a ' + description + ' formed in ' + str(year)
# print(sentence)

# famous_sketch1 = "\n\t Hell's Grannies"
# famous_sketch2 = '\n\t The Dead Parrot'

# print('Famous Work:', famous_sketch1, famous_sketch2)


# word1 = 'Good'
# end1 = word1[2:]

# word2 = 'Evening'
# end2 = word2[3:]
# print(end1, end2)

# word1 = 'good'
# half1 = len(word1)//2
# end1 = word1[half1:]

# word2 = 'evening'
# half2 = len(word2)//2
# end2 = word2[half2:]

# print(end1, end2)


# conditionals:


# rain_speed = 7
# if rain_speed < 5:
#     print("Just a Scotch mist")
# else:
#     print("It's a real Cow-quaker out there")


# example: if num_knights < 3 or day == "Monday":
#     print('Retreat')



# num_knights = int(input('Enter number of knights'))
# day = input('Enter day of the week')
# enemy = input('Enter type of enemy')

# if enemy == 'Killer bunny':
#     print('Holy hand grenade')
# else:
#     if num_knights < 3 or day == 'monday':
#         print('retreeeet')
#     if num_knights >= 10 and day == 'wednesday':
#         print('trojan rabbits')
#     else: 
#         print('truce')





# computer_choice = 'rock'
# user_choice = input("Enter rock, paper, or python:\n")

# if computer_choice == user_choice:
#     print('TIE')
# elif user_choice == 'rock' and computer_choice == 'python':
#     print('WIN')
# elif user_choice == 'paper' and computer_choice == 'rock':
#     print('WIN')
# elif user_choice == 'python' and computer_choice == 'paper':
#     print('WIN')
# elif user_choice == 'python' and computer_choice == 'rock':
#     print('WIN')
# else:
#     print('You lose :( Computer wins :D')