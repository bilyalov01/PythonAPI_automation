f = open('pass.txt', 'r')
for line in f:
    line = line.replace('\n', '.')
    print(line)
f.close()
