# imports
from rich import print
import random

# colors used
# red
# bright_cyan
# light_green

# base set up
left = ["left", "Left", "L", "l"]
right = ["right", "Right", "R", "r"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]
inside = ["I", "i", "Inside", "inside"]
outside = ["O", "o", "Outside", "outside"]


class Player:
    inventory = []
    health = 100
    attack = 30

    def add_attack(self):
        if self.attack == 30:
            self.attack += 10
            print(f'Attack power increased to: {self.attack}')
        else:
            print('You already picked up the astroblaster')
    
    def add_health(self):
        if self.health == 100:
            self.health += 30
            print(f'Health increased to: {self.health}')
        else:
            print('You already picked up the food')

def start():
    answer = input('Want to play?(yes/no)')
    if answer.lower() in yes:
        print('Welcome!')
        intro()
    else:
        print('See ya')


############################################  INTRODUCTION   ######################################################
increased_player_attack = False
increased_player_health = False

player = Player()

def intro():
    print('[red]💥💥CRASHING NOISES💥💥[/red]')
    print('You wake up still strapped into your seat and slowly open your eyes. You take in the mangled mess of a spaceship around you. You reach down and struggle to unbuckle yourself. Everything in your body aches from the intense impact.')
    print('You were able to eject your seat from the ship and somehow survived. You slowly rise to your feet and see a vast, dry desert all around you. There are bits and pieces of your ship wedged in the mounds of sand.')
    print(f'[bright_cyan]Health: {player.health}[/bright_cyan]')
    print(f'[bright_cyan]Attack power: {player.attack}[/bright_cyan]')
    print(f'[bright_cyan]Inventory: {player.inventory}[/bright_cyan]')
    choice1 = input(
        'Go left to the damaged spaceship or go right to explore?(L/R)')
    if choice1.lower() in left:
        print('You stagger towards the chunk of ship that was the main cabin. Lights are still flashing and bits of metal shine in the hot sunlight. You scan the wreckage to see if there is anything salvageable.')
        print('Your eyes land on a chrome blue bit of metal sticking out of the sand. You dig around it and realize its your astroblaster! It\'s seen better days, but still seems functional')

        print('[light_green]✨ASTRO BLASTER✨[/light_green] added to inventory')
        player.inventory.append('astro blaster')
        print(f'[bright_cyan]Inventory: {player.inventory}[/bright_cyan]')

        player.add_attack()
        increased_player_attack == True

# function to add health to player when astro blaster is discovered, need to find spot for it

        ship()
    else:
        explore()

############################################  SHIP   ##########################################################


def ship():
    choice2 = input(
        'Continue to dig through the ship rubble or head back outside?(Inside/Outside)')
    if choice2.lower() in inside:
        print('You decide to rummage through the rubble to see if you can find anything else that may be useful. You look around and spot large chucks of what used to be the shell of your high tech spaceship. You walk over and begin digging in the hot sand. Sweat is building on your forehead and your fingers start to go numb.')
        # add method for flashlight or battery drop
        explore()
    else:
        print('You take one last, long look at what remains of your spaceship. The sand is starting to feel hot through your space boots and you need to get out of this heat.')
        explore()

############################################  EXPLORE   ##########################################################


def explore():
    print('You take a deep breath and scan yourself for injuries. You seem to be physically ok, but your memory is still foggy. To your left you see a mountain range about 1 mile away, to your right you see a cave about 2 miles away. The moutain might have running water, but the cave will sheild you from the unbearable heat.')
    choice3 = input(
        'Head left towards the mountain or go right into the cave?(L/R)')
    if choice3.lower() in left:
        print('Your mouth is extremely dry and you feel your stomach rumble. You decide to take a chance and head towards the mountain range, in hopes of finding clean water and maybe some food.')
        mountain()
    else:
        print('Sweat rolls down your back and your skin is already burning. You decide to seek shade in the cave.')
        cave()

############################################  MOUNTAIN   ##########################################################


def mountain():
    print('You set off on your hike to the mountain range. The loose mounds of sand slow you down, but you are determined to find water. After what felt like a never ending trek, you finally make it to the base of the closest mountain. You scan your surroundings and spot a green patch of grass and trees. You head towards it and being to hear running water. FINALLY! You run to it and rapidly scoop handfuls of water to your mouth.')
    print('After you quench your thirst, you take in your surroundings. The river flows down from the mountain and curves away from you. The trees provide a little bit of shade, which is definetly better than standing out in the heat. You notice some small bushes around you and see small pops of red in them.')
    
    print('[bright_cyan]🍗FOOD🍗 added to inventory[/bright_cyan]')
    player.inventory.append('food')
    print(f'[bright_cyan]Inventory: {player.inventory}[/bright_cyan]')
    player.add_health()
    increased_player_health == True

    print('You pick the berries and gobble them down. You walk to a nearby ledge and peer off into the distance. You see the wreckage of your ship of in the distance and the entrance to the cave. You contemplate how draining the trek would be to the cave. You turn around and look up towards the peak of the mountain and see a steady pillar of smoke.')
    choice4 = input('Head left to the cave or travel right to the mountain peak?(L/R)')
    if choice4.lower() in left:
        cave()
    else:
        mountain_peak()

def mountain_peak():
    print('You gather your strength and start the trek to the peak of the mountain. The closer you get, you smell burning meat and perhaps spices? You continue hiking and begin to hear conversations and music. You finally make it to the top and see a very small village, comprised of maybe ten people.')
    print('You make some lound walking sounds and slowly approach, to ensure that you don\'t scare the villagers. The biggest villager turns and stares you down. You slowly raise your hands and take a knee in the dirt, to communicate that you are not a threat.')
    print('Another villager steps out from behind the large villager. She approaches you and says: "You look lost. Let us hear your story."')
    print('You detail your crash and how you\'ve been wandering around this unknown area, looking for a way to get home. She takes your hand and says: "I understand. We can send you home if you wish." You nod your head and begin to feel light and bubbly before you lose consciousness')
    sent_home()

############################################  CAVE   ##########################################################


def cave():
    print('You walk into the entrance of the cave and see an old, damaged flashlight on the ground.')
    print('[bright_cyan]✨FLASHLIGHT✨ added to inventory[/bright_cyan]')
    player.inventory.append('flashlight')
    print(f'[bright_cyan]Inventory: {player.inventory}[/bright_cyan]')
    print('You flick the switch and nothing happens. You bang the flashlight on your hand a few times and the flashlight slowly emits a warm beam of light. You scan the entrance of the cave with your newly found flashlight and only see sand, rocks, and a tunnel. The tunnel turns to the right after 30ft, so it\'s hard to see what the tunnel could lead to.')
    choice5 = input('Go down the tunnel or turn around?(Inside/Outside)')
    if choice5.lower() in inside:
        print('You slowly proceed down the tunnel and try to make the least amount of noise possible.')
        creature()
    else:
        print('You decide that the cave is too spooky and you quickly walk out of the cave. The mountain is at least closer to you now, so you decide it will be worthwhile to check it out. Your stomach grumbles again and you hope that you can possibly find some kind of food.')
        mountain()

############################################  CREATURE MEET   ###################################################


def creature():
    print('creature description')
    choice6 = input('approach creature or leave?(Inside/Outside)')
    if choice6.lower() in inside:
        print('player approaches the creature')
        approach()
    else:
        print('player leaves the cave')
        # add function for ending w/o fighting creature

############################################  APPROACH  ##########################################################


def approach():
    print('approach story')
    # random number for enemy health with varying probabilities
    enemyHealth = [75, 80, 85, 90, 100]
    enemy = random.choices(enemyHealth, weights=(10, 30, 20, 30, 10), k=1)
    print('[red]The enemy\'s heatlh is [/red]', enemy)
    if increased_player_health == True:
        print(f'[bright_cyan]Your health is {player.add_health}[/bright_cyan]')
    else:
        print(f'[bright_cyan]Your health is {player.health}[/bright_cyan]')
    if increased_player_attack == True:
        print(f'[bright_cyan]Your attack power is {player.add_attack}[/bright_cyan]')
    else:
        print(f'[bright_cyan]Your attack power is {player.attack}[/bright_cyan]')

def sent_home():
    print('home story')

# add functions for live and die endings

    # flip() the display to put your work on screen
    # pygame.display.flip()

    # clock.tick(60)  # limits FPS to 60


# pygame.quit()

start()

