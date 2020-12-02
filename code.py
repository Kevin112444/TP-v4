from cmu_112_graphics import *
import os
import random


class MyApp(App):

################################################################################
# These are the different classes. The subclasses will be for every individual 
# unit in the game.
# The assets used for this game:
# Sprites for the Units - https://aekashics.itch.io/aekashics-librarium-librarium-static-batch-megapack
# Sprites for the bases(portals) - https://elthen.itch.io/2d-pixel-art-portal-sprites
# Picture for background - https://www.freelancer.is/contest/Need-Background-for-D-Platformer-Game-We-will-work-for-more-after-the-contest-1372733-byentry-22150937?w=f&ngsw-bypass=
################################################################################
        
    class Units(object):
        def __init__(self,health,attack,movespd,range,cost):
            self.health = health   # hp of the unit
            self.attack = attack   # the damage per attack
            self.moveSpeed = movespd   # how fast the unit moves
            self.range = range   # how far the unit can attack
            self.cost = cost   # how much the unit will cost
            self.state = 'walk'   # what the unit is doing
            self.spriteCounter = 0  # for animation purposes
        
        def __eq__(self, other):
            return (isinstance(other, A) and (self.x == other.x))
    
    class Base(Units):
        def __init__(self,absPos,relPos):
            self.health = 10000
            self.absPos = absPos   # absPos and relPos is used for scrolling
            self.relPos = relPos

# the different tuples represent which frame range is used    
    class Bat(Units):
        spritesheet = 0
        
        def __init__(self):
            super().__init__(10,1,10,0,10)
            
        def action(self):
            if self.state == 'walk':
                return (0,4)
            elif self.state == 'fight':
                return (30,42)

    class Owl(Units):
        spritesheet = 1
        def __init__(self): 
            super().__init__(10,1,15,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (0,9)
            elif self.state == 'fight':
                return (9,18)
                    
    class Peacock(Units):
        spritesheet = 2
        def __init__(self):
            super().__init__(10,1,10,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (27,36)
            elif self.state == 'fight':
                return (9,18)
                
    class Rat(Units):
        spritesheet = 3
        def __init__(self): 
            super().__init__(10,1,10,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (9,18)
            elif self.state == 'fight':
                return (0,9)

    class Anubis(Units):
        spritesheet = 4
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (42,48)
            elif self.state == 'fight':
                return (2,5)
    
    class Knight(Units):
        spritesheet = 5
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (0,5)
            elif self.state == 'fight':
                return (11,13)
    
    class Slime(Units):
        spritesheet = 6
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (9,14)
            elif self.state == 'fight':
                return (21,26)

    class Spore(Units):
        spritesheet = 7
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (27,36)
            elif self.state == 'fight':
                return (0,5)
    
    class EarthWorm(Units):
        spritesheet = 8
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (18,27)
            elif self.state == 'fight':
                return (3,5)
    
    class Golem(Units):
        spritesheet = 9
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (6,11)
            elif self.state == 'fight':
                return (18,26)
    
    class Phoenix(Units):
        spritesheet = 10
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (27,36)
            elif self.state == 'fight':
                return (9,18)
    
    class WereWolf(Units):
        spritesheet = 11
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (0,6)
            elif self.state == 'fight':
                return (12,14)
    
    class DoppelSlime(Units):
        spritesheet = 12
        def __init__(self): 
            super().__init__(10,1,1,0,10)
            
        def action(self):
            if self.state == 'walk':
                return (15,21)
            elif self.state == 'fight':
                return (9,18)
    
    class Slayer(Units):
        spritesheet = 13
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (27,35)
            elif self.state == 'fight':
                return (11,14)
    
    class Whale(Units):
        spritesheet = 14
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (36,45)
            elif self.state == 'fight':
                return (2,7)

    class Wyvern(Units):
        spritesheet = 15
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (0,8)
            elif self.state == 'fight':
                return (36,42)

    class Angel(Units):
        spritesheet = 16
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (27,36)
            elif self.state == 'fight':
                return (0,9)
    
    class Boss(Units):
        spritesheet = 17
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (27,36)
            elif self.state == 'fight':
                return (0,7)
    
    class Overmind(Units):
        spritesheet = 18
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (5,13)
            elif self.state == 'fight':
                return (4,7)
    
    class Spike(Units):
        spritesheet = 19
        def __init__(self): 
            super().__init__(10,1,1,0,10)
        
        def action(self):
            if self.state == 'walk':
                return (0,9)
            elif self.state == 'fight':
                return (9,15)

################################################################################
# These are the functions for the game functionality and for your side of
# the game
################################################################################      
    def appStarted(self):
        self.timerDelay = 10
        self.sheets = []
        self.background = self.loadImage('Assets/Backgrounds/background.png')
        self.age = 0   # current age
        self.enemyAge = 0
        self.alive = []   # all the ally units that are alive right now
        self.enemyAlive = []
        self.sprites = []   # contains all the frames of the units
        self.enemySprites = []
        self.enemySpriteCounters = []
        self.spriteCounters = []   # counters count the frame
        self.absSpriteLocation = []   # abs and rel locations used for scrolling purposes
        self.relSpriteLocation= []
        self.enemyAbsSpriteLocation = []
        self.enemyRelSpriteLocation = []
        self.icons = []   # image of the unit in the button
        self.iconLoader()   
        self.allyBase = self.Base(.05 * self.width, .05 * self.width)
        self.enemyBase = self.Base( 1.95 * self.width, 1.95 * self.width)
        self.baseSprites = []
        self.baseCounter = 0
        self.baseAnimate()
        self.money = 1000
        self.enemyMoney = 1000
        
    def keyPressed(self,event):
        # used for scrolling left and right
        # if a is pressed and your display window can still scroll left
        if event.key == 'a' and (self.allyBase.relPos < (.1  * self.width)):
            self.allyBase.relPos += self.width * .1
            self.enemyBase.relPos += self.width * .1
            for pos in range(len(self.relSpriteLocation)):
                self.relSpriteLocation[pos] += self.width * .1
            for pos in range(len(self.enemyRelSpriteLocation)):
                self.enemyRelSpriteLocation[pos] += self.width * .1
        # if d is pressed and your display window can still scroll right
        elif event.key == 'd' and (self.enemyBase.relPos > (.95 * self.width)):
            self.allyBase.relPos -= self.width * .1
            self.enemyBase.relPos -= self.width * .1
            for pos in range(len(self.relSpriteLocation)):
                self.relSpriteLocation[pos] -= self.width * .1
            for pos in range(len(self.enemyRelSpriteLocation)):
                self.enemyRelSpriteLocation[pos] -= self.width * .1

    # function for summoning a new unit                    
    def spawn(self,unit):
        self.alive.append(unit)
        self.spriteCounters.append(0)
        self.absSpriteLocation.append(self.allyBase.absPos)
        self.relSpriteLocation.append(self.allyBase.relPos)
        self.money -= unit.cost
        self.Animate()

    def enemySpawn(self,unit):
        self.enemyAlive.append(unit)
        self.enemySpriteCounters.append(0)
        self.enemyAbsSpriteLocation.append(self.enemyBase.absPos)
        self.enemyRelSpriteLocation.append(self.enemyBase.relPos)
        self.enemyMoney -= unit.cost
        self.enemyAnimate()  

    def mousePressed(self,event):
        # evolve button
        if (.75 * self.width <= event.x <= .85 * self.width) and (.05 * self.height <= event.y <= .15 * self.height): 
            self.age += 1
        if (.85 * self.height) <= event.y <= (.99 * self.height):
            #leftmost button
            if (.01 * self.width) <= event.x <= (.09 * self.width):
                if self.age == 0:
                    newBat = 'bat' + str(len(self.sprites))
                    newBat = self.Bat()
                    self.spawn(newBat)
                elif self.age == 1:
                    newAnubis = 'anubis'+ str(len(self.sprites))
                    newAnubis = self.Anubis()
                    self.spawn(newAnubis)
                elif self.age == 2:
                    newEarthworm = 'earthworm'+ str(len(self.sprites))
                    newEarthworm = self.EarthWorm()
                    self.spawn(newEarthworm)
                elif self.age == 3:
                    newDoppelSlime = 'doppelslime'+ str(len(self.sprites))
                    newDoppelSlime = self.DoppelSlime()
                    self.spawn(newDoppelSlime)
                elif self.age == 4:
                    newAngel = 'angel'+ str(len(self.sprites))
                    newAngel = self.Angel()
                    self.spawn(newAngel)
            # second button
            elif (.12 * self.width) <= event.x <= (.2 * self.width):
                if self.age == 0:
                    newOwl = 'owl' + str(len(self.sprites))
                    newOwl = self.Owl()
                    self.spawn(newOwl)
                elif self.age == 1:
                    newKnight = 'knight'+ str(len(self.sprites))
                    newKnight = self.Knight()
                    self.spawn(newKnight)
                elif self.age == 2:
                    newGolem = 'golem'+ str(len(self.sprites))
                    newGolem = self.Golem()
                    self.spawn(newGolem)
                elif self.age == 3:
                    newSlayer = 'slayer'+ str(len(self.sprites))
                    newSlayer = self.Slayer()
                    self.spawn(newSlayer)
                elif self.age == 4:
                    newBoss = 'boss'+ str(len(self.sprites))
                    newBoss = self.Boss()
                    self.spawn(newBoss)
            # third button
            elif (.23 * self.width) <= event.x <= (.31 * self.width):
                if self.age == 0:
                    newPeacock = 'peacock' + str(len(self.sprites))
                    newPeacock = self.Peacock()
                    self.spawn(newPeacock)
                elif self.age == 1:
                    newSlime = 'slime'+ str(len(self.sprites))
                    newSlime = self.Slime()
                    self.spawn(newSlime)
                elif self.age == 2:
                    newPhoenix = 'phoenix'+ str(len(self.sprites))
                    newPhoenix = self.Phoenix()
                    self.spawn(newPhoenix)
                elif self.age == 3:
                    newWhale = 'whale'+ str(len(self.sprites))
                    newWhale = self.Whale()
                    self.spawn(newWhale)
                elif self.age == 4:
                    newOvermind = 'overmind'+ str(len(self.sprites))
                    newOvermind = self.Overmind()
                    self.spawn(newOvermind)
            # fourth button
            elif (.34 * self.width) <= event.x <= (.42 * self.width):
                if self.age == 0:
                    newRat = 'rat' + str(len(self.sprites))
                    newRat = self.Rat()
                    self.spawn(newRat)
                elif self.age == 1:
                    newSpore = 'spore ' + str(len(self.sprites))
                    newSpore = self.Spore()
                    self.spawn(newSpore)
                elif self.age == 2:
                    newWerewolf = 'werewolf'+ str(len(self.sprites))
                    newWerewolf = self.WereWolf()
                    self.spawn(newWerewolf)
                elif self.age == 3:
                    newWyvern = 'wyvern'+ str(len(self.sprites))
                    newWyvern = self.Wyvern()
                    self.spawn(newWyvern)
                elif self.age == 4:
                    newSpike = 'spike'+ str(len(self.sprites))
                    newSpike = self.Spike()
                    self.spawn(newSpike)

    # function creates the sprites for newly summoned units and updates the old sprites if they change action
    # modified version of the sprite animations at https://www.cs.cmu.edu/~112/notes/notes-animations-part3.html
    def Animate(self):
        for count in range(len(self.alive)):
            unit = self.alive[count]
            pic = self.sheets[unit.spritesheet]
            (start,end) = unit.action()
            unitSprite = []
            for i in range(start,end):
                sprite = pic.crop((0 + 512 * (i % 9) , 0 + 512 * (i // 9),\
                        512 + 512 * (i % 9), 512 + 512 * (i //9 ) ))
                sprite = self.scaleImage(sprite, (self.height / 700 + self.width / 1400) / 6)
                sprite = sprite.transpose(Image.FLIP_LEFT_RIGHT)
                unitSprite.append(sprite)
            if count >= len(self.sprites):
                self.sprites.append(unitSprite)
            else:
                self.sprites[count] = unitSprite
    
    def enemyAnimate(self):
        for count in range(len(self.enemyAlive)):
            unit = self.enemyAlive[count]
            pic = self.sheets[unit.spritesheet]
            (start,end) = unit.action()
            unitSprite = []
            for i in range(start,end):
                sprite = pic.crop((0 + 512 * (i % 9) , 0 + 512 * (i // 9),\
                        512 + 512 * (i % 9), 512 + 512 * (i //9 ) ))
                sprite = self.scaleImage(sprite, (self.height / 700 + self.width / 1400) / 6)
                unitSprite.append(sprite)
            if count >= len(self.enemySprites):
                self.enemySprites.append(unitSprite)
            else:
                self.enemySprites[count] = unitSprite

    #similar to animate function above but for the two bases, no need to constantly update like above
    def baseAnimate(self):
        pic = self.loadImage("Assets/Backgrounds/allyPortal.png") 
        allyBaseSprites = []
        for i in range(4):
            sprite = pic.crop((0 + 512 * i  , 0 + 512 * (i//3), 512 + 512 * i , 512 + 512 * (i//3) ))
            sprite = self.scaleImage(sprite, (self.height / 700 + self.width / 1400) / 4) 
            allyBaseSprites.append(sprite)   
        self.baseSprites.append(allyBaseSprites)    
        pic2 = self.loadImage("Assets/Backgrounds/enemyPortal.png")     
        enemyBaseSprites = []   
        for i in range(4):
            sprite = pic2.crop((0 + 512 * i  , 0 + 512 * (i//3), 512 + 512 * i , 512 + 512 * (i//3) ))
            sprite = self.scaleImage(sprite, (self.height / 700 + self.width / 1400) / 4)  
            sprite = sprite.transpose(Image.FLIP_LEFT_RIGHT) 
            enemyBaseSprites.append(sprite)
        self.baseSprites.append(enemyBaseSprites)

    def enemyAI(self):
        if (len(self.enemyAlive) < 5):
            num = random.randint(0,3)
            if self.enemyAge == 0:
                if num == 0:
                    newBat = 'bat' + str(len(self.enemySprites))
                    newBat = self.Bat()
                    self.enemySpawn(newBat)
                elif num == 1:
                    newOwl = 'owl'+ str(len(self.enemySprites))
                    newOwl = self.Owl() 
                    self.enemySpawn(newOwl)
                elif num == 2:
                    newPeacock = 'peacock'+ str(len(self.enemySprites))
                    newPeacock = self.Peacock()
                    self.enemySpawn(newPeacock)
                elif num == 3:
                    newRat = 'rat'+ str(len(self.sprites))
                    newRat = self.Rat()
                    self.enemySpawn(newRat) 

    # Loads and imports different images for the icons of the units 
    def iconLoader(self):
        path = 'Assets/Sprites'
        for folder in os.listdir(path):
            images = os.listdir(path + '/' + folder)
            for spritesheets in images:
                sheet = self.loadImage(path + '/' + folder + '/' + spritesheets)
                self.sheets.append(sheet)
                icon = sheet.crop((0,0,512,512))
                icon = sprite = self.scaleImage(icon, (self.height / 700 + self.width / 1400) / 12)
                self.icons.append(icon)

    # distance between two units
    def dist(self,x1,x2):
        return (x1 - 512 * ((self.height / 700 + self.width / 1400) / 12) - \
            x2 - 512 * ((self.height / 700 + self.width / 1400) / 12))

    def movement(self):
        # makes sure units don't overlap
        for unit in range(len(self.alive)):
            self.spriteCounters[unit] = (1 + self.spriteCounters[unit]) % len(self.sprites[unit])
            # makes sure units don't overlap 
            if unit == 0 or (self.dist(self.absSpriteLocation[unit-1],self.absSpriteLocation[unit]) > self.alive[unit].moveSpeed):
                self.absSpriteLocation[unit] += self.alive[unit].moveSpeed
                self.relSpriteLocation[unit] += self.alive[unit].moveSpeed
        for unit in range(len(self.enemyAlive)):
            self.enemySpriteCounters[unit] = (1 + self.enemySpriteCounters[unit]) % len(self.enemySprites[unit])
            if unit == 0 or (self.dist(self.enemyAbsSpriteLocation[unit],self.enemyAbsSpriteLocation[unit-1]) > self.enemyAlive[unit].moveSpeed):
                self.enemyAbsSpriteLocation[unit] -= self.enemyAlive[unit].moveSpeed
                self.enemyRelSpriteLocation[unit] -= self.enemyAlive[unit].moveSpeed
        
    def timerFired(self):
        self.background = self.background.resize((self.width,self.height))
        self.enemyAI()
        self.movement()
        self.baseCounter = (1 + self.baseCounter) % 3
        self.money += 1
        self.enemyMoney += 1

    # instructions for drawing the UI
    def interface(self,canvas): 
        canvas.create_image(self.width/2, self.height/2, image=ImageTk.PhotoImage(self.background))
        # this draws the buttons for summoning the unit
        for unit in range(4):
            canvas.create_rectangle((.01 + .11 * unit) * self.width, .85 * self.height, (.09 + .11 * unit) * self.width, .99 * self.height, fill = "Teal")
            canvas.create_image((.05 + .11 * unit) * self.width, .88 * self.height, image = ImageTk.PhotoImage(self.icons[4 * self.age + unit]))
            canvas.create_rectangle((.01  + .11 * unit) * self.width, .95 * self.height, (.09 + .11 * unit) * self.width, .99 * self.height, fill = "White")
        # this draws the evolve button 
        if self.age < 5:
            canvas.create_rectangle(.75 * self.width, .05 * self.height, .85 * self.width, .15 * self.height, fill = "White" )
        canvas.create_text(.05 * self.width, .1 * self.height, text = f'${self.money}', font = "Helvetica 25 bold")  

    def redrawAll(self,canvas):
        self.interface(canvas)
        # ally and enemy base
        canvas.create_image(self.allyBase.relPos, .68 * self.height, \
            image=ImageTk.PhotoImage(self.baseSprites[0][self.baseCounter]))
        canvas.create_image(self.enemyBase.relPos, .68 * self.height, \
            image=ImageTk.PhotoImage(self.baseSprites[1][self.baseCounter]))
        # this draws the sprites of the units
        for sprite in range(len(self.sprites)):
            unit = self.sprites[sprite]
            canvas.create_image(self.relSpriteLocation[sprite], .72 * self.height, \
                image=ImageTk.PhotoImage(unit[self.spriteCounters[sprite]]))
        for sprite in range(len(self.enemySprites)):
            unit = self.enemySprites[sprite]
            canvas.create_image(self.enemyRelSpriteLocation[sprite], .72 * self.height, \
                image=ImageTk.PhotoImage(unit[self.enemySpriteCounters[sprite]]))
                        
MyApp(width=1400, height=700)