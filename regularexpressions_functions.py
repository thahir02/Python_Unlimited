'''
Python's RegularExpression(re) module allows exactly two types of data: Strings (str) and Bytes (bytes).You cannot mix them. The data type of your pattern must perfectly match the data type of your text.

1. String Type (Most Common)Both the regex pattern and the text being searched are standard Unicode strings.
Example:- '''
import re
pattern = r"\d+"  # String
text = "The year is 2026."  # String
print(re.findall(pattern, text))  # Works perfectly
''''
2. Bytes Type (For Binary Data)Both the regex pattern and the text being searched are raw bytes. 
  This is used when reading binary files, images, or network packets. You define bytes using a b prefix (e.g., b"pattern").
Example:-'''
import re
pattern_bytes = b"\d+"  # Bytes
text_bytes = b"The year is 2026."  # Bytes
print(re.findall(pattern_bytes, text_bytes))  # Works perfectly
'''
❌ What Happens If You Mix Them?If you try to use a string pattern on bytes data, or vice versa, Python will raise a TypeError.
Example :-'''
import re
# This will CRASH with a TypeError: cannot use a string pattern on a bytes-like object
re.findall(r"\d+", b"The year is 2026.")

'''
The types of functions used in regular expressions :-
In Python's built-in re module, regular expressions are essential tools for Artificial Intelligence (AI), Natural Language Processing (NLP), and LLM data cleansing. 
They process unstructured text into standardized data.
Here is how match(), search(), group(), sub(), subn(), and split() operate with examples.

match() and search() :-
  These functions look for a specific pattern in text but start their scan from different positions.
  match() checks for a pattern only at the very beginning of the string.
  search() scans the entire string and returns the first occurrence of the pattern.
  Both return a Match object if successful, or None if no match is found.
  Example :-
'''
import re
text = "AI agents are transforming software development."
# re.match() looks at the start of the string
print(re.match(r"agents", text))  # Output: None (because "agents" is not at the beginning)
# re.search() scans the entire string
result = re.search(r"agents", text)
print(result)  # Output: <re.Match object; span=(3, 9), match='agents'>
'''
group() :-
  The group() method extracts the actual matched text from a successful Match object.
  group(0) or group() returns the entire matched string.
  group(1), group(2), etc., extract specific substrings isolated by parentheses () (capturing groups).
  Example :-
'''
import re
# AI Prompt extraction example
text = "System Prompt: You are a helpful assistant."
# Group 1 captures the label, Group 2 captures the instruction
match_obj = re.search(r"(System Prompt): (.*)", text)
if match_obj:
    print(match_obj.group(0))  # Output: "System Prompt: You are a helpful assistant."
    print(match_obj.group(1))  # Output: "System Prompt"
    print(match_obj.group(2))  # Output: "You are a helpful assistant."
'''
sub() and subn() :-
  These functions find patterns and substitute them with a new string. They are widely used to sanitize training data (e.g., removing private information, URLs, or HTML tags).
  sub() returns only the modified string.
  subn() returns a tuple containing the modified string and the total number of substitutions made.
  Example :-
'''
import re
# Cleaning a chat log to protect user privacy
chat_log = "User contact is user1@email.com. Agent contact is support@email.com."
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
# re.sub() replaces all emails with a placeholder
clean_text = re.sub(email_pattern, "[REDACTED_EMAIL]", chat_log)
print(clean_text) 
# Output: "User contact is [REDACTED_EMAIL]. Agent contact is [REDACTED_EMAIL]."
# re.subn() does the same but counts the changes
clean_text_tuple = re.subn(email_pattern, "[REDACTED_EMAIL]", chat_log)
print(clean_text_tuple) 
# Output: ('User contact is [REDACTED_EMAIL]. Agent contact is [REDACTED_EMAIL].', 2)
'''
split() :-
  The split() function splits a string into a list of substrings wherever the regex pattern matches. This is useful for tokenizing text into sentences or words based on irregular punctuation.
  Example :-
'''
import re
# Tokenizing an LLM output by punctuation or special symbols
raw_output = "Step1: Parse data; Step2: Embed vectors; Step3: Query database."
# Split by a colon, a semicolon, or a period, followed by optional spaces
tokens = re.split(r"[:;.]\s*", raw_output)
print(tokens)
# Output: ['Step1', 'Parse data', 'Step2', 'Embed vectors', 'Step3', 'Query database', '']


'''
Quick Reference Summary
| **Function** | **Primary Use Case in AI/NLP**                                                | **Pattern / Syntax**                    | **Returns**                      | **Example**                       |
| ------------ | ----------------------------------------------------------------------------- | --------------------------------------- | -------------------------------- | --------------------------------- |
| `match()`    | Verifying if a text block starts with specific metadata tags.                 | `re.match(pattern, string)`             | Match object or `None`           | `re.match(r"^Title", text)`       |
| `search()`   | Locating the first instance of a keyword or entity anywhere in text.          | `re.search(pattern, string)`            | Match object or `None`           | `re.search(r"AI", text)`          |
| `group()`    | Isolating and pulling out structural pieces of text (e.g., entity names).     | `match.group()`                         | String                           | `match.group(1)`                  |
| `sub()`      | Data cleaning, anonymization, and removing HTML formatting.                   | `re.sub(pattern, replacement, string)`  | Modified string                  | `re.sub(r"<.*?>", "", html_text)` |
| `subn()`     | Data cleaning with auditing metrics (knowing how many fixes occurred).        | `re.subn(pattern, replacement, string)` | Tuple `(Modified String, Count)` | `re.subn(r"\d", "#", text)`       |
| `split()`    | Tokenization of custom log lines, system prompts, or multi-hop agent scripts. | `re.split(pattern, string)`             | List of strings                  | `re.split(r",\s*", text)`         |
'''
  

