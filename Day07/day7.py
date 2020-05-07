from intCode_compiler import Intcode
import sys
import os
import itertools


def amplifiers(code, sequence):
   # Initialize each amps whith curent phase
   # sequence.
   amps = []
   for number in sequence:
      amp = Intcode(code)
      amp.run(int(number))
      amps.append(amp)
   return amps

#Part one
def outputSignal(intCode, signal):
   ans = []
   sequences = itertools.permutations(signal)
   for seq in sequences:
      amps = amplifiers(intCode, seq)
      out = 0
      for amp in amps:
            out = amp.run(out)
      ans.append(out)
   return max(ans)

#Part two
def outputSignalWithFeedbackLoop(l, p):
   ans = []
   sequences = itertools.permutations(signal)
   for seq in sequences:
      amps = amplifiers(intCode, seq)
      out = 0
      currentAmp = amps[0]
      i = 0
      while  not currentAmp.stopped:
         # My elegant way to loop back to the first amplifier
            if i == len(seq):
               i = 0
            currentAmp = amps[i]
            out = currentAmp.run(out)
            i += 1
      ans.append(out)
   return max(ans)

   

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
      intCode = f.read().split(",")
      intCode = list(map(int, intCode))

      signal = ['4','3', '2', '1','0']
      print("Output signal after running once:", outputSignal(intCode, signal))
      
      signal = ['9','8', '7', '6','5']
      print("Output signal after running the feedback loop:", outputSignalWithFeedbackLoop(intCode, signal))
      