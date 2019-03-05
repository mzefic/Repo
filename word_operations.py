def myreplace(old, new, s):
    """ Replace all occurrences of old with new in s. """
    result = new.join(s.split(old))
    return result

def cleanword(s):
    """ Removes punctuations from a string """
    punctuation = "!\"#$%&'()*+,./:;<=>?@[\\]^_`{|}~"
    result = ""
    for i in s:
        if i not in punctuation:
            result += i
    return result

def has_dashdash(s):
    """ Removes dashes from a string """
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
    """ Cleans the string from punctuations, lowercases it and removes dashes """
    clean = cleanword(s)
    g = clean.lower()
    if has_dashdash(s) == True:
        h = " ".join(g.split("--"))
        return h.split()
    else:
        return g.split()

def wordcount(s, l):
    """ Counts how many times a given word appears in a list """
    count = 0
    for i in l:
        if i == s:
            count += 1
    return count


def wordset(s):
    """ Removes string duplicates in a list, and then alphabetically sorts them """
    result = []
    for i in s:
        if i not in result:
            result.append(i)
        result.sort()
    return result


def longestword(l):
    """ Counts the words in a string and prints the longest one """
    if l == []:
        return 0
    else:
        result = []
        for i in l:
            result.append(len(i))
        result.sort()
        return result[-1]