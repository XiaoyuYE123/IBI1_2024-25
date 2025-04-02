import re
seq = 'GTGGTGTGTCTGTTCTGAGAGGGCCTAA'
matches= re.findall(r'GT.+AG',seq)
a = 0
for line in matches:
    if len(line) > a:
        a = len(line)
        largest = line
print('The largest intron is:',largest,'with length:',a)

        
        