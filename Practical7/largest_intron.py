import re
# This program finds the largest intron in a given DNA sequence
# it starts with 'GT' and ends with 'AG'
# it uses regular expressions to find all matches of a specific pattern
seq = 'GTGGTGTGTCTGTTCTGAGAGGGCCTAA'
matches= re.findall(r'GT.+AG',seq)
a = 0
# The variable 'a' is used to keep track of the length of the longest match
# The variable 'largest' is used to keep track of the longest match
# The program iterates through all matches and updates 'a' and 'largest' if a longer match is found
for line in matches:
    if len(line) > a:
        a = len(line)
        largest = line
print('The largest intron is:',largest,'with length:',a)

        
        