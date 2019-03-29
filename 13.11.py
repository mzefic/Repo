myfile = open("test.txt", "w")
myfile.write("My first file written from Python\n")
myfile.write("---------------------------------\n")
myfile.write("Hello, world!\n")
myfile.close()


f = open("test.txt", "r")
xs = f.readlines()
f.close()
" ".join(xs)
print(xs)

f = open("test.txt")
content = f.read()
f.close

words = content.split()
print("There are {0} words in the file.".format(len(words)))

f = open(r"C:\Users\mzef\Downloads\receipts.zip", "rb")
g = open(r"C:\Users\mzef\Downloads\receipts - Copy.zip", "wb")

while True:
    buf = f.read(1024)
    if len(buf) == 0:
        break
    g.write(buf)

f.close
g.close

import urllib.request

def retrieve_page(url):
    """ Retrieve the contents of a web page.
        The contents is converted to a string before returning it.
    """
    my_socket = urllib.request.urlopen(url)
    dta = str(my_socket.readall())
    my_socket.close()
    return dta

the_text = retrieve_page("https://www.w3.org/TR/PNG/iso_8859-1.txt")
print(the_text)



f = open("test.txt", "r")
s = f.read()
f.close()
f = open("newtext.txt", "w")
lines = s.split("\n")
f.write('\n'.join(lines[::-1]))
f.close


f = open("test.txt", "r")
s = f.readline()
s.split("\n")
if "snake" in s:
    print(s)
f.close
while True:
    if len(s) == 0:
        break
    if g in s:
        print(s)
f.close