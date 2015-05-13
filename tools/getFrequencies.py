import sys
import collections

if len(sys.argv) < 2:
    print("Please pass filename as command line argument")
    sys.exit()
elif len(sys.argv) > 3:
    print("Too many arguments!")
    sys.exit()
readFilename = sys.argv[1]
print("Getting frequencies for file " + readFilename)
readFile = open(readFilename, 'r')
if len(sys.argv) == 3:
    writeFile = sys.argv[2]
lines = []
for line in readFile:
    lines.append(line)
if len(lines) > 1:
    print("Your file had newlines in it, I'm not dealing with those, do it yourself")
    sys.exit()
counts = collections.defaultdict(int)
for c in lines[0]:
    counts[c] += 1
for c in counts:
    print(c, counts[c])
