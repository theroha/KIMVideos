# DMX Control
# By Jared Strain
# Last Edit: 06032018

'''
Function to load a list of DMX values from ENTTEC DMXUSB PRO

'''
# Import Statements
import serial, time, os

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
        dataLen = ord(bytearray(serialInput.read()))
        print dataLen
        dataLenB = ord(bytearray(serialInput.read()))
        print dataLenB

        # Read data into buffer
        if dataLen:
            Buffer = bytearray(serialInput.read(dataLen))
            LSB = True
        else:
            Buffer = bytearray(serialInput.read(dataLenB))
            LSB = False

        final = serialInput.read()
        if final == DMXCLOSE:
            searching = False
    
    return Buffer
