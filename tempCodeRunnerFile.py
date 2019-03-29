f = open("test.txt", "r")
s = f.readline()
s.split("\n")
if "snake" in s:
    print(s)
f.close