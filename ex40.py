#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def singMeASong(self):
        for line in self.lyrics:
            print line

happyBday = Song(["Happy birthday to you",
                  "I don't want to get sued",
                  "So I'll stop right there"])

bullsOnParade = Song(["They rally around the family",
                      "With pockets full of shells"])

happyBday.singMeASong()
bullsOnParade.singMeASong()
