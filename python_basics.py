# Nine major data types in pyhton

# - Booleans - True or False
# - Numbers - Any number or floating point
# - Strings - Must contain '' or ""
# - Bytes and byte arrays - 
# - None - use to defined a variable but dont want add a value for later use
# Lists-managing collections - simialr to an array
# Tuples-managing collections
# Sets-managing collections
# Dictionaries-managing collections-give ability to have key value pairs

# Example using boleans, numbers,


# meal_completed = True 
# sub_total = 100
# tip = sub_total * 0.2
# print(sub_total)

# ----------------------------------------------------------------------------------

# a variable is a programming construct that allows you to store different types of data

# name = 'Kristen'
# post_count = 42

# print(name)
# print(post_count)
# a_long_sentence_with_words = ''

# ---------------------------------------------------------------------------
# Python Strings Basics
# The \ has the same principle as a single quote.

# sentence = 'The quick brown fox jumped over the lazy dogs' # Single quote

# sentence_two = "That is my dog's bowl " #  Double quotes

# print(sentence)

# -------------------------------------------------------------------------------
# Case Functions Examples

# sentence = 'the quick brown fox jumped'.title()
# print(sentence)

# sentence = 'the Quick Brown fOx jumped'
# print(sentence.lower())

# """
# str.upper()
# Return a copy of the string with all the cased characters [4] converted to uppercase. Note that s.upper().isupper() might be False > if s contains uncased characters or if the Unicode category of the resulting character(s) is not “Lu” (Letter, uppercase), but e.g. > “Lt” (Letter, titlecase).

# str.capitalize()
# Return a copy of the string with its first character capitalized and the rest lowercased.

# str.lower()
# Return a copy of the string with all the cased characters [4] converted to lowercase.
# """


# ---------------------------------------------------------------------------------------

# NOTES# The quick brown fox jumped

# # T => 0    every first element has an index of zero to start
# # h => 1
# # e => 2
# # ' ' => 3   the space is index of three-python counts spaces as well

# starter_sentence = 'The quick brown fox jumped'
# #in brackets you pass in what ever index you want to use [ ]
# #Immutability means you can't change an element-can't alter the string once it's created
# #RANGES
# #to be brought the T [0:3] would start at 0 and go to the 3rd index number-in this case it will end at 3rd index and show The
# new_sentence = 'Thy' + starter_sentence[3:] #to change-start with saying Thy then pull in the starter 

# print(new_sentence)

# ---------------------------------------------------------------------------------------------