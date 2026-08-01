'''
Object Pattern :-
  The Pattern Object approach in Python (specifically within the re module) involves pre-compiling a regular expression string into a reusable regex object using re.compile(). 
  This object contains built-in methods like .search(), .match(), and .findall(), making your code cleaner and more efficient when reusing the same pattern multiple times.
You can use regular expressions in Python through two different approaches:
Examples :- '''
#----------------1--------------------
import re
text = "The quick brown fox jumps over the lazy dog."
pattern_string = r"fox"
# 1. Functional Approach (Compile on the fly)
if re.search(pattern_string, text):
    print("Found!")
# 2. Pattern Object Approach (Pre-compiled)
regex_object = re.compile(pattern_string)
if regex_object.search(text):
    print("Found!")
#----------------2-------------------
#approach - 1
import re
s='9494369389 73868157'
regex=r'\d{10}' #check wheather the number is 10 digits
print(re.search(regex,s))
print(re.findall(regex,s))
#---------------3--------------------
#approach - 2
import re
s='9494369389 73868157'
res=re.compile(r'\d{10}') #check wheather the number is 10 digits
print(res.search(s))
print(res.findall(s))

'''
Common Object Methods
  Once you create a pattern object using pattern = re.compile(r'\d+'), you can call these primary methods directly on it:
    pattern.match(): Checks for a match only at the beginning of the string.pattern.
    search(): Scans the entire string for the first match.pattern.
    findall(): Finds all matching substrings and returns them as a list.
    pattern.finditer(): Returns an iterator yielding match objects for all matches.pattern.
    sub(): Replaces occurrences of the pattern with a replacement string.
'''
