#!/usr/bin/python
# coding: iso-8859-1
import re
longString = "orem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

def firstSpace(source): #function returns first space after 15 characters in source
    spaces = [m.start() for m in re.finditer(" ", source)]
    return min(x for x in spaces if x > 20)

def returnSearchResult(substring, source): #returns a few characters before the search and a few characters after the search
    occurences = [m.start() for m in re.finditer(substring, source)]
    result = []
    for occurence in occurences:
        left = (source[:occurence])[::-1] # reversed string until occurence
        right = source[occurence:] # string after occurence
        first_spaces = [firstSpace(left), firstSpace(right)]
        left_text, right_text = left[:first_spaces[0]], right[:(first_spaces[0]-1)]
        left_text = left_text[::-1] #reverses string back to normal
        result.append("{0} {1}".format(left_text, right_text)) #adds this to list of search results
    return result

if __name__ == "__main__":
    substring = str(input("Input substring: "))
    result = returnSearchResult(substring, longString)
    print(result)

#not done: proper error handling for firstSpace (no min)
#space recognition still has bugs
