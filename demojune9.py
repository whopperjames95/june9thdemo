for loop:
slang = ['knackered', 'pip pip', 'squidgy', 'smashing']

menu = []

for word in slang:
    menu.append(word + ' Spam')

print(menu)

menu_prices = {}
price = .50
for item in menu:
    menu_prices[item] = price
    price = price + 1

print(menu_prices)


for name, price in menu_prices.items():
    print(name, ': $', format (price, '.2f'), sep='')



orders = []
order = input("what would you like to order? (Q to Quit)")

while (True):
    if order == 'Cheeky spam':
        print('Sorry, we run out of that')
        continue
    if order.upper() == 'Q':
        break

    order = input("Anything else? (Q to Quit)")

print(orders)



#guessing game while loops:

import random

num = random.randint(1, 10)

guess = int(input('Guess a number between 1 and 10'))
# Add while loop here
while (guess != num):
    guess = int(input('Guess again'))

print('You win!') 



import random

num = random.randint(1,10)
times = 1

guess = int(input('Guess a number between 1 and 10'))

while guess != num:
    guess = int(input('Guess again'))
    times = times +1

    if times == 3:
        break
if (guess == num):
    print('you win')
else:
    print('You lose. The number was ', num)
        

print('You win!')




functions:
start a function:     def average(prices(prices is a parameter)):
return avg

total = 0
prices = [29, 21, 55, 10]
for price in prices:
    total = total + price

avg = total/len(prices)
print(avg)


numbers = [1, 2, 3, 4, 5]
my_average = average(numbers)

print(average)

def average(prices):
    total = 0

    for price in prices:
        total = total + price
    avg = total/len(prices)
    return avg

prices = [2.5,3,4.5,5]

result = average(prices)

print(result)




# another example of list and for loop:

import random

def lotto_numbers():
    lotto_nums = []
    for i in range(5):
        lotto_nums.append(random.randint(1, 53))

    return lotto_nums


numbers = lotto_numbers()
print(numbers)







# best practice: 

def average(numbers):
    total = 0
    for num in list:
        total = total + num

    avg = total/len(numbers)
    return avg

def main():
    prices = [1,2,3,4]

    result = average(prices)
    print(order_goal)
    print(result)

main()
order_goal = 25




def get_order(menu):


def print_menu(menu):


def main():
    menu = {'Knackered spam': .50, 'fish': 2.50,}
    print_menu(menu)
    order = get_order(menu)
    print('You ordered:', order)

main()






import random

def guessing_game():
    num = random.randint(1, 10)

    guess = int(input('Guess a number between 1 and 10'))
    times = 1

    while guess != num:
        guess = int(input('Guess again'))
        times += 1
        if times == 3:
            break

    if guess == num:
        print('You win!')
    else:
        print('You lose! The number was', num)
    

def lotto_numbers():
    lotto_nums = []
    for i in range(5):
        lotto_nums.append(random.randint(1, 53)) 
    
    return lotto_nums
  
def main():
    answer = input('Do you want to get lottery numbers (1) or play the game (2) or quit (Q)?')
    if (answer == '1'):
        numbers = lotto_numbers()
        print(numbers)
    elif (answer == '2'):
            guessing_game()
    else:
            print('Toodles!')
    
main()



#files:

performances = {'Ventriloquism':       '9:00am', 
                'Snake Charmer':       '12:00pm', 
                'Amazing Acrobatics':  '2:00pm', 
                'Enchanted Elephants': '5:00pm'}

schedule_file = open('schedule.txt', 'w')
for key, val in performances.items():
    schedule_file.write(key + ' - ' + val + '\n')
    
schedule_file.close()



def read_dollar_menu():

    dollar_spam = open('dollar_menu.txt', "r")

    dollar_menu = []
    for line in dollar_spam:
        line = line.strip()
        dollar_menu.append(line)

    print(dollar_spam.read())




    performances = {}

schedule_file = open('schedule.txt', 'r')

for line in schedule_file:
    (show, time) = line.split(' - ')
    performances[show] = time.strip()
    #.strip deletes the random n characters on showtimes
    print(show, time)
    performances[show] = time

schedule_file.close()

print(performances)





performances = {}

try:
    schedule_file = open('schedule.txt', 'r')
except FileNotFoundError as err:
    print(err)

for line in schedule_file:
    (show, time) = line.split(' - ')
    performances[show] = time

schedule_file.close()
print(performances)







import requests
  
url = "http://api.openweathermap.org/data/2.5/weather?q=London&units=imperial&appid=67da29cb91129f1a68c1c06c1be92daa"
request = requests.get(url)

weather_json = request.json()

main_weather = weather_json['main']

temp = main_weather['temp']

print("The Circus's current temperature is ", temp)



# creating a module for weather: 
import weather

def main():
    weather.current_weather()

main()




import requests

def current_weather():
    url = "http://api.openweathermap.org/data/2.5/weather?q=London&units=imperial&appid=67da29cb91129f1a68c1c06c1be92daa"
    r = requests.get(url)

    weather_json = r.json()
    print(weather_json)

    min = weather_json['main']['temp_min']
    max = weather_json['main']['temp_max']

    print("The circus' forecast is", min , "as the low and", max, "as the high")
