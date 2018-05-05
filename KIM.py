# Kansas In Miniature Movie Control
# By Jared Strain
# Last Edit: 04052018

'''
Video controls for the drive-in theater as part of Kansas In Miniature.

Listens for DMX signals and plays movies if the diorama is in night.

Movies are loaded from 

'''
# Import Statements
import serial, time, os
from omxplayer.player import OMXPlayer

def loadSerialBuffer(serialInput, start, end):
    '''
    Reads in serial values from the buffer and
    searches for the start and end values.
    All values between start and end are returned as a list.
    '''
    Buffer = []
    holder = ''

    while holder != start:
        holder = serialInput.read(1)

    Buffer.append(holder)
    
    while holder != end:
        holder = serialInput.read(1)
        Buffer.append(holder)

    return Buffer

# Function : Load light settings into a list
def loadDMXList(serialInput):
    '''
    Finds beginning and end of DMX sequence
    in serial input and returns channel values as a list.
    '''
    DMXOPEN = chr(126)
    DMXCLOSE = chr(231)
    
    return loadSerialBuffer(serialInput, DMXOPEN, DMXCLOSE)

# Found Cue function
def foundCue(lightBuffer, lightNumber, lightLevel):
    # Searches lightBuffer
    # If lightNumber is at lightLevel: return true
