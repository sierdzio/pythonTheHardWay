#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Gothons from Percal 25 :-)

class Engine (object):
    def __init__(self, sceneMap):
        self.map = sceneMap

    def play(self):
        currentScene = self.map.begin()

        while (self.map.hasFinished == False):
            currentScene = self.map.nextScene(currentScene, self.map.carryMessage)

        print "-=# The game has finished #=-"

class Map(object):
    def __init__(self, startSceneName):
        self.startScene = startSceneName
        self.hasFinished = False
        self.carryMessage = None

        death = Death()
        centralCorridor = CentralCorridor()
        laserWeaponArmory = LaserWeaponArmory()
        theBridge = TheBridge()
        escapePod = EscapePod()
        self.scenes = {
                          death.name() : death,
                          centralCorridor.name() : centralCorridor,
                          laserWeaponArmory.name() : laserWeaponArmory,
                          theBridge.name() : theBridge,
                          escapePod.name() : escapePod
                      }

    def nextScene(self, sceneName, carryMessage = None):
        currentScene = self.scenes[sceneName]
        outcome = currentScene.enter(carryMessage)
        self.carryMessage = currentScene.carryMessage

        if (outcome == -1 or outcome == None):
            self.hasFinished = True
        return outcome

    def begin(self):
        return self.nextScene(self.startScene)

    def hasFinished(self):
        return self.hasFinished

class Scene(object):
    def __init__(self):
        self.carryMessage = None

    def name(self):
        return self.__class__.__name__

    def enter(self, carryMessage = None):
        pass

class Death(Scene):
    def enter(self, carryMessage = None):
        if (carryMessage != None):
            print carryMessage
        print "Game over, your character has died"

class CentralCorridor(Scene):
    def enter(self, carryMessage = None):
        print """
        You are in the central corridor of the space ship that is being overrun by Gothons.
        One of them is currently standing in front of you. He is pointing a gun at you
        and looks furious. There is a big red lever just to the right-hand side of you.
        In panic, you have forgotten what it is for. You have a good book in your hand
        - the famous guide to the galaxy.

        What is your plan?
        1. Turn the lever and see what happens.
        2. Chuck the book into the Gothon.
        3. Jump about in weightless environment in the general direction of the Gothon.
        4. Scream and try to hide.
        """

        result = int(raw_input("> "))

        if (result == 1):
            self.carryMessage = "You have turned the lever and suddenly the pressure in the cabin" \
            "drops. The Gothon is sucked into the void, but so, sadly, are you."
            return "Death"

        return "TheBridge"

class LaserWeaponArmory(Scene):
    def enter(self, carryMessage = None):
        print "You are in the armory. Lot's of laser guns in here"

class TheBridge(Scene):
    def enter(self, carryMessage = None):
        print "You are on the bridge"

class EscapePod(Scene):
    def enter(self, carryMessage = None):
        print "You are on the escape pod"

# Test area:
map = Map('CentralCorridor')
game = Engine(map)
game.play()
