# DMX Control
# By Jared Strain
# Last Edit: 06032018

'''
Function to load a list of DMX values from ENTTEC DMXUSB PRO

'''
# Import Statements
import serial, time, os

class DMX:
    def __init__(self, port):
        self.serialInput = serial.Serial(port)
        self.buffer = []

    # Function : Load light settings into a list
    def loadDMXList(self):
        '''
        Finds beginning and end of DMX sequence
        in serial input and returns channel values as a list.
        '''
        DMXOPEN = chr(126)
        DMXCLOSE = chr(231)
        searching = True

        while searching:
            # Flush Input Buffer
            self.serialInput.flushInput()

            # Find Opening Byte
            opening = 0
            while opening != DMXOPEN:
                opening = self.serialInput.read()

            # Read System Message: See ENTTEC DMXUSB PRO API
            systemMessage = self.serialInput.read()

            # Read Message Length
            dataLen = ord(bytearray(self.serialInput.read()))
            print dataLen
            dataLenB = ord(bytearray(self.serialInput.read()))
            print dataLenB

            # Read data into buffer
            if dataLen:
                Buffer = bytearray(self.serialInput.read(dataLen))
                LSB = True
            else:
                Buffer = bytearray(self.serialInput.read(dataLenB))
                LSB = False

            final = self.serialInput.read()
            if final == DMXCLOSE:
                searching = False

        self.buffer = Buffer
