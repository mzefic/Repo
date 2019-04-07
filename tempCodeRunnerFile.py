#13.11.4
f = open("test1.txt", "r")
s = open("test2.txt", "w")
t = str
while True:
    g = f.readline()
    if len(g) == 0:
        break
    x = g.split(" ")
    y = ' '.join(x[1:])
    s.write(y)
f.close
s.close