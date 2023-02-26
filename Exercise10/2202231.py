# Exercises

# 1. PascalCase to snake_case
# pascal_case = 'ThisIsAReallyLongStringThatIsFunToConvert'
#
# word_starts=[]
# for i, letter in enumerate(pascal_case):
#     if letter.isupper():
#         word_starts.append(i)
#
# words = []
#
# for i, word_start in enumerate(word_starts):
#     if i + 1 >= len(word_starts):
#         break
#
#     word = pascal_case[word_start:word_starts[i+1]]
#     words.append(word.lower())
#
# words.append(pascal_case[word_starts[-1]:].lower())
# print('_'.join(words))

# 2. snake_case to PascalCase
# var = 'this_is_a_really_long_string_that_is_fun_to_convert'
# res = var.replace("_",' ').title().replace(' ', '')
# print(res)
# print(var.replace('_',''))
#
# 3. Is one an anagram of the other?
var2 = 'wholesome python activity'
var3 = 'Woven Polytheistic Mat Toy'


if (sorted(var2.lower())) == (sorted(var3.lower())):
    print('Anagram')
else:
    print('Not an anagram')



# Q2
#
# import re
# name = 'CamelCaseName'
# name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
# print(name)  # camel_case_name