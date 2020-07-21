import sys
import os
# Add the parent directory to the path
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from intcode.intCode_compiler import Intcode

# In a list since other option is [x, y]
DEFAULT_INPUT = [-1]

class Computer(Intcode):
    def __init__(self, file):
         super().__init__(file)
         self.__packets = []


    def receivePacket(self, packet):
        self.__packets.append(packet)
    

    def getFirstPacket(self, time):
        if self.__packets and self.__packets[0].isUsable(time):
            return self.__packets.pop(0)
    

    def createPacket(self, input, time):
        packet = None

        for i in input:
            address = self.run(i)
        
        if address:
            x = self.run()
            y = self.run()
            packet = Packet(address, x, y, time)
        
        return packet
        

class Packet:
    def __init__(self, address, x, y, time):
        self.__address = address
        self.__x = x
        self.__y = y
        self.__time = time


    def __repr__(self):
        return 'Packet(Address: %i, x: %i, y: %i)' % (self.__address, self.__x, self.__y)


    def isUsable(self, time):
        return self.__time <= time


    def getXY(self):
        return [self.__x, self.__y]


    def addDelay(self, delay):
        self.__time += delay


    def getAddress(self):
        return self.__address


class Network:
    def  __init__(self, size):
       self.__computers = [Computer("input.txt") for _ in range(50)]
       self.__time = 0


    def bootAll(self):
        for address in range(len(self.__computers)):
            self.__computers[address].run(address)


    def communicate(self):
        found = False
        while not found:
            for computer in self.__computers:
                currentPacket = computer.getFirstPacket(self.__time)
            
                if currentPacket:
                    packetToSend = computer.createPacket(currentPacket.getXY(), self.__time)
                else:
                    packetToSend = computer.createPacket(DEFAULT_INPUT, self.__time)

                found = self.send(packetToSend)

                if found: 
                    break

            self.__time += 1


    def send(self, packet):
        if packet:
            address = packet.getAddress()

            if address == 255:
                print("FOUND IT:", packet)
                return True

            self.__computers[address].receivePacket(packet)
        return False


if __name__ == "__main__":
    n = Network(50)
    n.bootAll()
    n.communicate()