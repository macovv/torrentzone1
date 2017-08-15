# -*- coding: utf-8 -*-

from random import  randint

class titleSearcher:

    def search(self):
        titles = ['welcome in torrentzone', "yokuso ni torrentzone", "torrentzone - dzikie pizdeczki",
         "torrentzone - nieziemskie kurwiska", "torrentzone - zjedz kremowke", "torrentzone - nowy steam",
         "torrentzone - twoje legalne źródło", "torrentzone - prawa autorkie to to co lubię","torrentzone - zawsze się trochę piracie",
         "torrentzone - mały torrent jeszcze nikomu krzywdy nie zrobił",
          "torrentzone - podziel się", "torrentzone - dla ciebie, dla rodziny","torrentzone - pobieraj i bzikaj", "torrentzone - nawet boge nie pomoże"]
        i = randint(0, len(titles)-1)
        return titles[i]
