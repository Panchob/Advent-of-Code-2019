# Day 7

Instructions at: https://adventofcode.com/2019/day/7

The second part of this one took me a while to understand...

Until this point I was using my inctCode reader as a main function in a pyhton file and it worked just fine. But for part 2, the memory must not change for each amplifier until each one executed all instructions. It is probably still doable by hardcoding something (or not), but since I will problably have to use my Intcode Computer again, doing a refactor now will save me time later (I hope).

The easiest way I found to do that is using [OOP](https://en.wikipedia.org/wiki/Object-oriented_programming) and initialize IntCode "programs" with a memory, instruction pointer and a state. With that I just have to loop on each amplifier and each sequence of phases (thanks Itertools) and stop when everything hit the "stop" instruction.
