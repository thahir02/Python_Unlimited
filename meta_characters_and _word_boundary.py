'''
Meta Charater:
Metacharacters are special symbols in regular expressions (regex) that do not match themselves literally, but instead instruct the regex engine to perform specific pattern-matching behaviors.
The table below breaks down the most common metacharacters, their functions, and exact behavior examples:
Core RegEx Metacharacters :-
| Metacharacter | Description                                                                | Pattern Example | Matches             | Does Not Match |
-------------------------------------------------------------------------------------------------------------------------------------------------------
| `.`           | Matches any single character except a newline.                             | `c.t`           | "cat", "cot", "c9t" | "coot", "ct"   |
| `^`           | Matches the start of a string.                                             | `^Hello`        | "Hello world"       | "Say Hello"    |
| `$`           | Matches the end of a string.                                               | `end$`          | "The end"           | "The ending"   |
| `*`           | Matches 0 or more occurrences of the preceding character.                  | `lo*w`          | "lw", "low", "loow" | "law"          |
| `+`           | Matches 1 or more occurrences of the preceding character.                  | `lo+w`          | "low", "loow"       | "lw"           |
| `?`           | Matches 0 or 1 occurrence of the preceding character (optional item).      | `favou?r`       | "favor", "favour"   | "favouur"      |
| `[ ]`         | Defines a character set; matches any single character inside the brackets. | `c[aeiou]t`     | "cat", "cut"        | "cot", "coot"  |
| `[^ ]`        | Negated character set; matches any character not inside the brackets.      | `c[^aeiou]t`    | "cbt", "c9t"        | "cat", "cut"   |
| `\|`          | Alternation operator; acts like a logical OR.                              | `cat\|dog`      | "cat", "dog"        | "bird"         |
| `\`           | Escapes a metacharacter to treat it as a literal symbol.                   | `cat\.`         | "cat."              | "cat", "cats"  |
| `( )`         | Groups multiple tokens together to create a substring capsule.             | `(ha)+`         | "ha", "haha"        | "h"            |
| `{m,n}`       | Matches the preceding item at least m times and at most n times.           | `a{2,3}`        | "aa", "aaa"         | "a", "aaaa"    |

Character Shorthand Metacharacters :-
  These backslash-escaped sequences represent predefined categories of characters:
    \d matches any decimal digit (equivalent to [0-9]).
      Example: '''
        \d{3} matches "123" but not "abc".
    #\D matches any non-digit character (equivalent to [^0-9]).
      #Example: 
        \D matches "A", "!", or "** **".
    #\w matches any alphanumeric word character, including letters, numbers, and underscores.
      #Example: 
        \w+ matches "user_123".
    #\s matches any whitespace character like spaces, tabs, or line breaks.
      #Example: 
        cat\syeet matches "cat yeet".

'''
Here is a detailed guide to Python regular expression (regex) meta-characters, anchors, and specialized combinations.

    Base Meta-characters :-
      . matches any character except a newline.
      \ escapes special characters or signals special sequences.
      | acts as an OR operator.* matches zero or more repetitions.
      ? matches zero or one repetition.+ matches one or more repetitions.
      {} specifies explicit repetition counts or ranges.
      ^ matches the start of a string.$ matches the end of a string.
    Example :- '''
      import re
      # Dot (.)
      print(re.findall(re.escape('.'), "a.c"))     # Output: ['.'] (escaped)
      print(re.findall(r"a.c", "abc a-c a\nc"))     # Output: ['abc', 'a-c']
      # Alternation (|)
      print(re.findall(r"cat|dog", "the cat and dog"))  # Output: ['cat', 'dog']
      # Quantifiers (*, ?, +, {})
      print(re.findall(r"ca*t", "ct cat caat"))     # Output: ['ct', 'cat', 'caat']
      print(re.findall(r"ca?t", "ct cat caat"))     # Output: ['ct', 'cat']
      print(re.findall(r"ca+t", "ct cat caat"))     # Output: ['cat', 'caat']
      print(re.findall(r"a{2,3}", "a aa aaa aaaa")) # Output: ['aa', 'aaa', 'aaa']
'''
    Character Classes & Sets
      [] matches any single character inside the brackets.
      [^] matches any single character NOT inside the brackets.
      [-] matches a literal hyphen if placed first or last.
      \w matches any alphanumeric character plus underscore 
      [a-zA-Z0-9_].\W matches any non-alphanumeric character 
      [^a-zA-Z0-9_].\d matches any decimal digit [0-9].
      \D matches any non-digit character [^0-9].
      \s matches any whitespace character (space, tab, newline).
      \S matches any non-whitespace character.
     Example :- '''
      # Sets and Ranges
      print(re.findall(r"[aeiou]", "apple"))        # Output: ['a', 'e']
      print(re.findall(r"[^aeiou]", "apple"))       # Output: ['p', 'p', 'l']
      print(re.findall(r"[-az]", "a-z"))            # Output: ['a', '-', 'z']
      # Shorthand Classes
      print(re.findall(r"\d+", "ID: 456, Val: 12")) # Output: ['456', '12']
      print(re.findall(r"\w+", "Hello_123!"))       # Output: ['Hello_123']
      print(re.findall(r"\s+", "a \t \b b"))        # Output: [' \t ']
'''
    Word Boundaries (\b and \B)
        A word boundary \b is a zero-width assertion. It represents the position between a word character (\w) and a non-word character (\W or string boundaries).
      Before nothing (Start of word): Position has a non-word character on the left and a word character on the right.
      After nothing (End of word): Position has a word character on the left and a non-word character on the right.
      Before and after nothing (Isolated word): Word is bounded on both sides by non-word characters or string limits.
      \B matches any position that is NOT a word boundary (e.g., inside the middle of a word).
      Example :- '''
        # \b Before nothing / Start of word
        print(re.findall(r"\bcat", "cat category scatter")) 
        # Output: ['cat', 'cat'] (matches 'cat' and the start of 'category')
        # \b After nothing / End of word
        print(re.findall(r"cat\b", "cat category scatter")) 
        # Output: ['cat'] (matches 'cat' but not 'category' or 'scatter')
        # \b Isolated word (Before and after nothing)
        print(re.findall(r"\bcat\b", "the cat sat")) 
        # Output: ['cat']
        # \B Middle of a word / Non-boundary
        print(re.findall(r"\Bcat\B", "scatted category cat")) 
        # Output: ['cat'] (only matches 'cat' inside 'scatted')
'''
    Complex Structural
      CombinationsCombining structural anchors, sets, and quantifiers creates precise pattern boundaries.
        ^[]+ matches a string that begins with one or more characters from the specified set.
        ^[]$ matches a string containing only characters from the specified set from start to finish.
        \b[]{} matches a word that begins with a specific number of characters from the defined set.
        []{},[] matches a specific number of characters from the first set, followed by a comma, followed by a character from the second set.
      Example :- '''
        # ^[]+ : Must start with the class characters
        print(re.match(r"^[A-Z]+", "HELLO world"))     # Output: <Match object; span=(0, 5)>
        print(re.match(r"^[A-Z]+", "hello WORLD"))     # Output: None
        # ^[]$ : Exact string match of class characters
        pattern = r"^[0-9]+$"
        print(re.match(pattern, "12345"))             # Output: <Match object; span=(0, 5)>
        print(re.match(pattern, "123a45"))            # Output: None
        # \b[]{} : Word starting with a set sequence length
        # Matches words starting with exactly 3 lowercase vowels/consonants in a specific range
        print(re.findall(r"\b[a-c]{3}\w*", "cab cap apple")) 
        # Output: ['cab', 'cap'] ('apple' does not start with a, b, or c 3 times)
        # []{},[] : Structured sequence matching
        # Matches exactly 2 digits, a comma, then one uppercase letter
        print(re.findall(r"[0-9]{2},[A-Z]", "12,A 45,B 1,C")) 
        # Output: ['12,A', '45,B']





