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
    searching = True
    
    while searching:
        # Flush Input Buffer
        serialInput.flushInput()
        
        # Find Opening Byte
        opening = 0
        while opening != DMXOPEN:
            opening = serialInput.read()

        # Read System Message: See ENTTEC DMXUSB PRO API
        systemMessage = serialInput.read()

        # Read Message Length
        dataLen = int(serialInput.read())
        dataLenB = int(serialInput.read())

        # Read data into buffer
        if dataLen:
            Buffer = serialInput.read(dataLen)
            LSB = True
        else:
            Buffer = serialInput.read(dataLenB)
            LSB = False

        final = serialInput.read()
        if final == DMXCLOSE:
            searching = False
    
    return Buffer

# Found Cue function
def foundCue(DMXList, lightNumber, lightLevel):
    # Searches DMXList
    # If lightNumber is at lightLevel: return true
