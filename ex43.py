#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Gothons from Percal 25 :-)

class Engine (object):
    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Map(object):
    def __init__(self, startScene):
        pass

    def nextScene(self, sceneName):
        pass

    def openingScene(self):
        pass

class Scene(object):
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
map = Map('centralCorridor')
game = Engine(map)
game.play()
