print("Welcome to the pet tungsten cube simulator you will take care of this tungsten cube and make sure it stays alive and happy")
name = input("What would you like to name your cube?\n")
health = 10

happy = 10

hunger = 10

while health > 0:
    action = (input("What would you like to do?\n1. Feed the cube \n2. Play with the cube \n3. Nothing \n4. Leave\n"))
    
    if action == "1":
        print(f"You decide to feed {name}")
        hunger += 1
        health += 1
        print (f"{name}'s condition - Health: {health} Happiness: {happy} Hunger: {hunger}")
    
    elif action == "2":
        print(f"You decide to play with {name}")
        happy += 3
        hunger -= 3
        print (f"{name}'s condition - Health: {health} Happiness: {happy} Hunger: {hunger}")
    
    elif action == "3":
        print(f"You don't do anything with {name}:(")
        happy -= 5 
        hunger -= 3
        print (f"{name}'s condition - Health: {health} Happiness: {happy} Hunger: {hunger}") 
    
    elif action == "4":
        print(f"You monster, you abandon {name}")
        quit()
    
    if health == 0:
        print(f"{name} died, you are a terrible owner :(")
        quit()
    
    if hunger < 0:
        hunger = 0
        print(f"{name} starved to death :(")

    if hunger == 0:
        health -= 5
        print(f"{name} starved to death :(")

    
    
    if happy < 0:
        hunger = 0
        print(f"{name} died of sadness :(")
        
    if happy == 0:
        health -= 5
        print(f"{name} died of sadness :(")