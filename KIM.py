#!/usr/bin/python3
# Kansas In Miniature Movie Control
# By Jared Strain
# Last Edit: 04052018

'''
Video controls for the drive-in theater as part of Kansas In Miniature.

Listens for DMX signals and plays movies if the diorama is in night.

Movies are loaded from 

'''
# Import Statements
import DMX
from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep

VIDEO_PATH = #video path
SERIAL_PORT = #serial port
LIGHT = # light to search on

class video(OMXPlayer)
    def __init__(self, videoPath):
        OMXPlayer.__init__(self, videoPath, args=['-b'])
        sleep(0.2)
        self.mute()
        self.fullscreen()
        self.pause()
        self.hide_video()
    def play(self):
        self.show_video()
        self.play()
    def pause(self):
        self.pause()
        self.hide_video()
    

# Found Cue function
def foundCue(DMXList, lightNumber, lightLevel):
    # Searches DMXList
    # If lightNumber is at lightLevel: return true
    
    if DMXList[lightNumber] == lightLevel:
        return True:
    else: return False
    
player = video(VIDEO_PATH) # Load and hide video
ser = DMX.serial.Serial(SERIAL_PORT) # Open serial port

while not foundCue(DMX.loadDMXList(ser), LIGHT, 0): # loop until indicated light goes dark
    
player.play()
while foundCue(DMX.loadDMXList(ser), LIGHT, 0): # wait for light to come back on
    
player.pause()
