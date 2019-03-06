import random
import word_operations

def make_random_ints_no_dups(num, lower_bound, upper_bound):
   """
     Generate a list containing num random ints between
     lower_bound and upper_bound. upper_bound is an open bound.
     The result list cannot contain duplicates.
   """
   result = []              #Checks the list every single iteration if the candidate is already present
   rng = random.Random()
   for i in range(num):
        while True:
            candidate = rng.randrange(lower_bound, upper_bound)
            if candidate not in result:
                break
        result.append(candidate)        #Fills the 'result' list with unique candidates on every iteration
   return result

xs = make_random_ints_no_dups(5, 1, 10000000)
print(xs)




import time

def do_my_sum(xs):
    sum = 0
    for v in xs:
        sum += v
    return sum

sz = 10000000
testdata = range(sz)

t0 = time.clock()
my_result = do_my_sum(testdata)
t1 = time.clock()
print("my_result    = {0} (time taken = {1:.4f} seconds)"
        .format(my_result, t1-t0))

t2 = time.clock()
their_result = sum(testdata)
t3 = time.clock()
print("their_result = {0} (time taken = {1:.4f} seconds)"
        .format(their_result, t3-t2))


from unit_tester import test


import calendar


cal = calendar.TextCalendar()
cal.setfirstweekday(3)
cal.pryear(2019)                    # exercise 1
cal.prmonth(2019, 11)               # exercise 2
print(calendar.isleap(2019))         # exercies 3


import calendar

d = calendar.LocaleTextCalendar(6, "Macedonian")    # exercise 4
d.pryear(2012)



def myreplace(old, new, s):
    """ Replace all occurrences of old with new in s. """
    result = new.join(s.split(old))
    return result


def cleanword(s):
    punctuation = "!\"#$%&'()*+,./:;<=>?@[\\]^_`{|}~"
    result = ""
    for i in s:
        if i not in punctuation:
            result += i
    return result

def has_dashdash(s):
    dash = "-"
    result = 0
    for i in s:
        if dash in i:
            result += 1
    if result != 2:
        return False
    else:
        return True

def extract_words(s):
    clean = cleanword(s)
    g = clean.lower()
    if has_dashdash(s) == True:
        h = " ".join(g.split("--"))
        return h.split()
    else:
        return g.split()

def wordcount(s, l):
    count = 0
    for i in l:
        if i == s:
            count += 1
    return count


def wordset(s):
    result = []
    for i in s:
        if i not in result:
            result.append(i)
        result.sort()
    return result


def longestword(l):
    if l == []:
        return 0
    else:
        result = []
        for i in l:
            result.append(len(i))
        result.sort()
        return result[-1]


#test(cleanword("what?") == "what")
#test(cleanword("'now!'") == "now")
#test(cleanword("?+='w-o-r-d!,@$()'") ==  "word")

#test(has_dashdash("distance--but"))
#test(not has_dashdash("several"))
#test(has_dashdash("spoke--"))
#test(has_dashdash("distance--but"))
#test(not has_dashdash("-yo-yo-"))

#test(extract_words("Now is the time!  'Now', is the time? Yes, now.") == ['now','is','the','time','now','is','the','time','yes','now'])
#test(extract_words("she tried to curtsey as she spoke--fancy") == ['she','tried','to','curtsey','as','she','spoke','fancy'])


#test(wordcount("now", ["now","is","time","is","now","is","is"]) == 2)
#test(wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
#test(wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
#test(wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)

#test(wordset(["now", "is", "time", "is", "now", "is", "is"]) ==
#      ["is", "now", "time"])
#test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) ==
#      ["I", "a", "am", "is"])
#test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) ==
#      ["a", "am", "are", "be", "but", "is", "or"])

#test(longestword(["a", "apple", "pear", "grape"]) == 5)
#test(longestword(["a", "am", "I", "be"]) == 2)
#test(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
#test(longestword([ ]) == 0)

