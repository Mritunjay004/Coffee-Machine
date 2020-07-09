water = 400
milk = 540
beans = 120
cups = 9
money = 550

def rem():
    
    print(f"""The coffee machine has:
{water} of water
{milk} of milk
{beans} of coffee beans
{cups} of disposable cups
${money} of money""")
def buy():
    global water, milk, beans, cups, money
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    coffee = input()
    if coffee == "1":
        if 250 <= water and 16 <= beans and 4 <= money:
            print("I have enough resources, making you a coffee!")
            water -= 250
            beans -= 16
            cups -= 1
            money += 4
        else:
            print("Sorry, not enough water!")
    elif coffee == "2":
        if 350 <= water and 75 <= milk and 20 <= beans and 7 <= money:
            print("I have enough resources, making you a coffee!")
            water -= 350
            milk -= 75
            beans -= 20
            cups -= 1
            money += 7 
        else:
            print("Sorry, not enough water!")
            
    else:
        if coffee == "3":
            if 200 <= water and 100 <= milk and 12 <= beans and 6 <= money:
                print("I have enough resources, making you a coffee!")
                water -= 200
                milk -= 100
                beans -= 12
                cups -= 1
                money += 6
            else:
                print("Sorry, not enough water!")
def fill():
    global water, milk, beans, cups, money
    print("Write how many ml of water do you want to add:")
    waterr = int(input())
    print("Write how many ml of milk do you want to add:")
    milkk = int(input())
    print("Write how many grams of coffee beans do you want to add:")
    beanss = int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    cupss = int(input())
    water += waterr
    milk += milkk
    beans += beanss
    cups += cupss

        
def take():
    global water, milk, beans, cups, money
    print("I gave you $", money)
    money = 0 
while True:
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    if action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        rem()
    else:
        break
            
