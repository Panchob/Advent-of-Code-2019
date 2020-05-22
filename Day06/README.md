# Day 6

[Instructions](https://adventofcode.com/2019/day/6)

This day is a perfect example on how simple a problem can be if you apply the right mindset (which I did not do for like 2 hrs). The problem describes orbits between objects in space. This can be imaged this way:

```
        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I
```

With "COM" being the center of mass (no parents).

Well... this a tree, with nodes and all the logic behind it. With that in mind, algorithms to count all child elements in a tree is pretty easy to replicate, thanks to my out of this world google skills (its been a long time since a worked with a tree structure ok...). For part two, I tough I would have to use Dijkstra' algorithm, but a "simple" deep first search worked. This might mean that not all input will work with my solution. But I'll live with it for now :).
