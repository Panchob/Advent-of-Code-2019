import sys
import os
# Add the parent directory to the path
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from intcode.intCode_compiler import Intcode

class Computer:
    def __init__(self):
         self.receivedPackets = []
         self.intcode = Intcode("input.txt")
    
    def boot(self, address):
        self.intcode.run(address)
    

class Packet:
    def __init__(self, x, y, time):
        self.x = x
        self.y = y
        self.time = time

class Network:

    def  __init__(self, size):
       self.computers = [Computer() for _ in range(50)]
      
       self.time = 0

    def bootAll(self):
        for address in range(len(self.computers)):
            self.computers[address].boot(address)


    def communicate(self):
        found = False
        while not found:
            for computer in self.computers:
                currentPacket = None
                packets = computer.receivedPackets
                out = []
                res = None
                
                # TODO: extract
                if packets and packets[0].time <= self.time:
                    currentPacket = computer.receivedPackets.pop(0)

                # TODO: DRY
                if currentPacket:
                    res = computer.intcode.run(currentPacket.x)
                    if res != None:
                        out.append(res)
                    res = computer.intcode.run(currentPacket.y)
                    if res != None:
                        out.append(res) 
                else:
                    res = computer.intcode.run(-1)
                    if res != None:
                        out.append(res) 

                out.extend(computer.intcode.getOutput())
                # TODO: extract
                i = 0
                delay = 1
                if out :
                    while i < len(out):
                        address = out[i]
                        x = out[i + 1]
                        y = out[i + 2]

                        if address == 255:
                            print("FOUND IT:", y)
                            found = True
                            break

                        i += 3

                        packet = Packet(x, y, self.time + delay)
                        delay += 1

                        self.computers[address].receivedPackets.append(packet)
            self.time += 1


if __name__ == "__main__":
    n = Network(50)
    n.bootAll()
    n.communicate()