# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 14:32:48 2018

@author: b
"""
import random, pylab

class Drunk(object):
    def __init__(self, name = None):
        """Assumes name is a str"""
        self.name = name

    def __str__(self):
        if self != None:
            return self.name
        return 'Anonymous'
