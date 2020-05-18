# Day 3

[Instructions](https://adventofcode.com/2019/day/3)

I felt a little bump in difficulty for this one. What helped me was to write my test beforehand so I didn't have to worry about parsing the input file and just use data structures that I wanted.

I know it's possible to solve this with calculating distances between lines, but I decided to just enumerate every positions and find intersections (by using list intersection... I know, smart). It worked and from there part two was a piece of cake since I only had to return the index of the first intersection.
