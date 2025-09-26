import random
game_name = "PyQuest"
print(f"Welcome to {game_name}!")
print("===================")

# Ask for the character's name
name = input("Before we begin, what is your character's name?\n")

# Print the name
print(f"Great {name}! Let's begin the adventure!")

# Player's initial stats
player = {
    "name": name,
    "health": 100,
    "coin": 0
}

# List of possible events
events = ["find a coin", "meet a monster", "do nothing"]

# Choose a random event
event = random.choice(events)
print(f"While exploring, you {event}!")

if event == "find a coin":
    player["coin"] += 1
    print(f"{name} found a coin, {name} now has {player["coin"]} coins.")
elif event == "meet a monster":
    player["health"] -= 10
    print(f"{name} got hurt during the combat with monster, health is now {player["health"]}.")