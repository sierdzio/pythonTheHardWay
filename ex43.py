#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Gothons from Percal 25 :-)

class Engine (object):
    def __init__(self, sceneMap):
        self.map = sceneMap

    def play(self):
        currentScene = self.map.begin()

        while (self.map.hasFinished == False):
            currentScene = self.map.nextScene(currentScene)
            currentScene.enter()

class Map(object):
    def __init__(self, startSceneName):
        self.startScene = startSceneName
        self.hasFinished = False

        death = Death()
        centralCorridor = CentralCorridor()
        laserWeaponArmory = LaserWeaponArmory()
        theBridge = TheBridge()
        escapePod = EscapePod()
        self.scenes = {death.name() : death,
                       centralCorridor.name() : centralCorridor,
                       laserWeaponArmory.name() : laserWeaponArmory,
                       theBridge.name() : theBridge,
                       escapePod.name() : escapePod}

    def nextScene(self, sceneName):
        outcome = self.scenes[sceneName].enter()
        if (outcome == -1 or outcome == None):
            self.hasFinished = True
        return outcome

    def begin(self):
        return self.nextScene(self.startScene)

    def hasFinished(self):
        return self.hasFinished

class Scene(object):
    def name(self):
        return self.__class__.__name__

    def enter(self):
        pass

class Death(Scene):
    def enter(self):
        pass

class CentralCorridor(Scene):
    def enter(self):
        pass

class LaserWeaponArmory(Scene):
    def enter(self):
        pass

class TheBridge(Scene):
    def enter(self):
        pass

class EscapePod(Scene):
    def enter(self):
        pass

# Test area:
map = Map('CentralCorridor')
game = Engine(map)
game.play()
