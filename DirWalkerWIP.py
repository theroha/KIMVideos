#!/usr/bin/python3
"""
Kansas In Miniature Video Player for Raspbian

This purpose of this program is to read a directory of videos
into a list and play videos using OMXPlayer.

Videos should be placed in /home/pi/Videos
"""

import omxplayer, sys, os
from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep

VIDEOS_PATH = '/home/pi/Videos'

contentList = os.walk(VIDEOS_PATH)
dirList = []
fileDict = {'root': list()}

for item in contentList:
    itemPath = VIDEOS_PATH + '/' + item
    print(itemPath)
    if os.path.isdir(itemPath):
        dirList.append(itemPath)
        fileDict[itemPath] = list()
    if os.path.isfile(itemPath):
        fileDict['root'].append(itemPath)
        print(fileDict)

for item in fileDict:
    print(item)
    hold = []
    for file in fileDict[item]:
        print(file)
        print(fileDict)
        if item != 'root':
            filePath = item + '/' + file
            print(filePath)
            if os.path.isfile(filePath):
                print(True)
                hold.append(filePath)
                print(fileDict)
            else: print(False)
    fileDict[item].extend(hold)
print(fileDict)
